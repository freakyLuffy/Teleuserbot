@client.on(events.NewMessage(outgoing=True, pattern="^.bf.*"))
async def cfff(event):
    url='https://codeforces.com/api/user.rating?handle='
    hd=event.raw_text.split()[1]
    response = requests.get('https://codeforces.com/api/user.info?handles='+hd)
    js=(response.json())
    try:
        dct=js['result'][0]
        print(type(dct))
    except KeyError:
        pass