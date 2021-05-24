@client.on(events.NewMessage(outgoing=True, pattern="^.f.*"))
async def cff(event):
    hd=event.raw_text.split()[1]
    try:
        response = requests.get(f'https://codeforces.com/api/user.status?handle={hd}&from=1&count=100')
        js=(response.json())
        dct={}
        target=5
        link='https://codeforces.com/problemset/problem/'
        for i in js['result']:
            if i['verdict']=='OK':
                try:
                    dct[str(i['problem']['contestId'])+str(i['problem']['index'])]=[i['problem']['name'],i['problem']['rating'],link+str(i['problem']['contestId'])+'/'+str(i['problem']['index'])]
                except KeyError:
                    dct[str(i['problem']['contestId'])+str(i['problem']['index'])]=[i['problem']['name'],'',link+str(i['problem']['contestId'])+'/'+str(i['problem']['index'])]
            
                    
            if len(dct)==target:
                break
        s=''
        for i in dct:
            s+=f'[{dct[i][0]}]({dct[i][2]}) '+f',rating=`{dct[i][1]}`\n'
        response=f'User **{hd}**\'s last five successful submissions are:\n{s}'
        await event.edit(response,link_preview=False)
    except KeyError:
        response_string=f"Handle **{hd}** doesn't exist:/"
        await event.edit(response_string)

@client.on(events.NewMessage(outgoing=True, pattern="^.cf.*"))
async def cf(event):
    hd=event.raw_text.split()[1]
    response = requests.get('https://codeforces.com/api/user.info?handles='+hd)
    js=(response.json())
    try:
        dct=js['result'][0]
        handle=dct['handle']
        maxr=dct['maxRating']
        maxrr=dct['maxRank']
        cur_rank=dct['rank']
        rating=dct['rating']
        friends=dct['friendOfCount']
        org=dct.get('organization','')
        response_string = ("**Codeforces handle:** {}\n**Current rank**: {}\n**Current rating:** `{}`\n**Max rating:** `{}`\n**Max rank:** {}\n**Friend of:** `{}`\n**Organization: **{}".format(handle,cur_rank,rating,maxr,maxrr,friends,org))
        await event.edit(response_string)
    except KeyError:
        response_string=f"Handle **{hd}** doesn't exist:/"
        await event.edit(response_string)