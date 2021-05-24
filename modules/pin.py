from start import client
from telethon import events
@client.on(events.NewMessage(outgoing=True, pattern="^.pin$"))
async def pin(event):
    my_id=event.id
    print(event.chat_id)
    msg_id=event.reply_to_msg_id
    await client.delete_messages(event.input_chat, event.id)
    await client.pin_message(event.chat_id,msg_id)

@client.on(events.NewMessage(outgoing=True, pattern="^.unpin$"))
async def unpin(event):
    print(event.chat_id)
    await client.delete_messages(event.input_chat, event.id)
    await client.unpin_message(event.chat_id)