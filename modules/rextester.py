from start import client
from telethon import events
@client.on(events.NewMessage(outgoing=True, pattern="^!b.*"))
async def convo(event):
    message=(await event.get_reply_message()).message
    a=[]
    lang=event.raw_text.split()[1]
    async with client.conversation('@rextester_bot') as conv:
        msg1 = await conv.send_message('/'+lang+'\n'+message)
        #msg1 = await conv.send_message(message)
        msg2 = (await conv.get_response()).message.split('\n')
        text=''
        ok=0;
        msg=''
        note=0
        if len(msg2)>1:
            print('gfgg')
            for i in msg2:
                if i=='Note:' or i=='Tip:':
                    note=1
                    a.append('`')
                    break
                if ok:
                    a.append(i)
                if i=='Result:': 
                    a.append('**Result:**`')
                    ok=1
                elif i=='Errors:':
                    a.append('**Errors:**`')
                    ok=1
            if note==0:
                a.append('`')
            msg='\n'.join(a)
            #print(msg)
        else:
            msg='Error:` Unknown language`'
        await event.edit(msg)
