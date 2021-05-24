from start import client
from telethon import events
@client.on(events.NewMessage(outgoing=True, pattern="^!n.*",))
async def note(event):
    msg=event.raw_text[2:]
    try:
        message = (await event.get_reply_message()).id
        print(message)
        await client.delete_messages(event.input_chat,event.id)
        print(msg)
        response=f'{CUSTOM_TEXT[msg]}'
        await client.send_message(event.chat_id,response,reply_to=message)
    except AttributeError:
        await client.delete_messages(event.input_chat,event.id)
        print(msg)
        response=f'{CUSTOM_TEXT[msg]}'
        await client.send_message(event.chat_id,response)