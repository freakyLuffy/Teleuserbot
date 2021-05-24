from start import client
from telethon import events
@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def my_event_handler(event):
    if event.chat_id not in white:
        await client.send_message(event.chat_id,CUSTOM_TEXT['pm'])