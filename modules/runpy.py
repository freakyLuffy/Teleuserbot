import subprocess
import os
from start import client
from telethon import events

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
    f=open("result.txt",'r')
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