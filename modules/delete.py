from start import client
from telethon import events
@client.on(events.NewMessage(outgoing=True, pattern="^.dl$"))
async def dl(event):
  ids=[event.id]
  ids.append(event.reply_to_msg_id)
  await client.delete_messages(event.input_chat, ids)