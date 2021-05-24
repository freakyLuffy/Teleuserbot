from start import client
from telethon import events
from pbwrap import Pastebin


@client.on(events.NewMessage(outgoing=True, pattern="^!paste$"))
async def paste(event):
    pb=Pastebin("5PaG-csPUl7H7cgZktaHvULrLUaHMepZ")
    msg=await event.get_reply_message()
    first_name=msg.sender.first_name
    
    user_link=f'tg://user?id={msg.sender.id}'
    print(user_link)
    response=f'[{first_name}]({user_link}), your wall of text is moved to `\U0001F447` {link}\n\nPlease use a online pasting service to send your code when it\'s too lengthy. Next time ,you will be warned!'
    await event.edit(response)