from start import client
from telethon import events
import aiohttp


@client.on(events.NewMessage(outgoing=True, pattern="^!paste$"))
async def haste(event):
    msg=(await event.get_reply_message())
    content=msg.message
    async with aiohttp.ClientSession() as session:
        async with session.post("https://hastebin.com/documents",data=content.encode('utf-8')) as post:
            post = await post.json()
    link="https://hastebin.com/{}".format(post['key'])
    first_name=msg.sender.first_name
    user_link=f'tg://user?id={msg.sender.id}'
    print(user_link)
    response=f'Hey [{first_name}]({user_link}), your wall of text is moved to `\U0001F447` {link}\n\nPlease use a online pasting service to send your code when it\'s too lengthy. Next time ,you will be warned!\nHere\'s a list of few: - \n- https://del.dog\n- https://dpaste.org\n- https://linkode.org\n- https://hastebin.com\n- https://bin.kv2.dev\n- pastebin.com'
    await event.edit(response) 