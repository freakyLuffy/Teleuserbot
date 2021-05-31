from start import client
for_lis=[]
@client.on(events.NewMessage(outgoing=True, pattern="^fdl$"))
async def ddd(target):
    message = (await target.get_reply_message())
    await client.delete_messages(target.input_chat, target.id)
    await client.forward_messages(for_lis[0], message.id, target.chat_id) 

@client.on(events.NewMessage(outgoing=True, pattern="^fdp$"))
async def ddd(target):
    message = (await target.get_reply_message())
    await client.delete_messages(target.input_chat, target.id)
    await client.forward_messages(for_lis, message.id, target.chat_id) 