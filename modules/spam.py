from start import client
from telethon import events
@client.on(events.NewMessage(outgoing=True, pattern="^!s.*"))
async def spam(event):
    msg_id=event.id
    chat_id=event.chat_id
    await client.delete_messages(event.input_chat, msg_id)
    print(chat_id)
    words=event.raw_text.split()
    num=int(words[2])
    text=words[1]
    for i in range(num):
        await client.send_message(chat_id,text)