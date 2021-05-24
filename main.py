from telethon import TelegramClient,events
import random
import subprocess
import os
import requests, json
from codeforces import codeforces
from pbwrap import Pastebin
from config import details

white=[]

CUSTOM_TEXT={
            }

client = TelegramClient('hima', api_id, api_hash)
client.start()
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
@client.on(events.NewMessage(outgoing=True,pattern="^!py.*"))
async def normal_handler(event):
    chunks=event.raw_text.split('\n')
    chunks=chunks[1:]
    #await event.reply(str(random.randint(1, 6)))
    this_folder = os.path.dirname(os.path.realpath(__file__))
    code_file = "code.py"

    #chunks=["print(\"hello\")","for i in range(10):\n   print(i)"]
    with open(f"{this_folder}/{code_file}", "w") as f_code:
        for chunk in chunks:
            f_code.write(f"{chunk}\n")
    errors=""
    s=""
    result = subprocess.run(["python",  "./"+code_file], capture_output=True, text=True)
    f=open("C:\\Users\\Himanshu\\Desktop\\tel.txt",'r')
    print(result.stderr)
    for i in result.stdout:
        s+=i
    for i in result.stderr:
        errors+=i
    if s=='':
        s='\n'
    if errors=='':
        errors=' '
    source ='\n'.join(chunks)
    response_string ="**Source:**\n`{}`\n\n**Result:** `{}`\n**Stderr:** `{}`".format(source,s,errors)
    await event.edit(response_string)


@client.on(events.NewMessage(outgoing=True, pattern="^e!dle", func=lambda e: e.is_reply)) 
async def purge(event):
  print(event)
  reply =await  event.get_reply_message()
  temp = [event.id]
  for msg in await client.get_messages(event.input_chat, min_id=reply.id-1, max_id=event.id):
    temp.append(msg.id)
  await client.delete_messages(event.input_chat, temp)

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


@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def my_event_handler(event):
    if event.chat_id not in white:
        await client.send_message(event.chat_id,CUSTOM_TEXT['pm'])


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

@client.on(events.NewMessage(outgoing=True, pattern="^!paste$"))
async def paste(event):
    pb=Pastebin(your_pastebin_developer_api)
    msg=await event.get_reply_message()
    first_name=msg.sender.first_name
    
    user_link=f'tg://user?id={msg.sender.id}'
    print(user_link)
    response=f'[{first_name}]({user_link}), your wall of text is moved to `\U0001F447` {link}\n\nPlease use a online pasting service to send your code when it\'s too lengthy. Next time ,you will be warned!'
    await event.edit(response)

@client.on(events.NewMessage(outgoing=True, pattern="^.dl$"))
async def dl(event):
  ids=[event.id]
  ids.append(event.reply_to_msg_id)
  await client.delete_messages(event.input_chat, ids)
  

        
  #await client.delete_messages(event.input_chat, ids)


        
    
@client.on(events.NewMessage(outgoing=True, pattern="^.d$"))
async def d(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
            first_name=message.sender.first_name
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
            first_name=message.forward.sender.first_name
    await target.edit("**Username:**{} \n**First Name:** {} \n**User ID:** `{}`".format(name,first_name, user_id))


client.run_until_disconnected()

