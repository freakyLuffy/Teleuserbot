from start import client
from telethon import events
@client.on(events.NewMessage(outgoing=True, pattern="^.d$"))
async def d(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            name = "**" + message.sender.username + "**"
            first_name=message.sender.first_name
        else:
            user_id = message.forward.sender.id
            name = "*" + message.forward.sender.username + "*"
            first_name=message.forward.sender.first_name
    await target.edit("**Username:**{} \n**First Name:** {} \n**User ID:** `{}`".format(name,first_name, user_id))
