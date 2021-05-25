from start import client
import requests
from telethon import events
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
                    dct[str(i['problem']['contestId'])+str(i['problem']['index'])]=[i['problem']['name'],'?',link+str(i['problem']['contestId'])+'/'+str(i['problem']['index'])]
            
                    
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
        print('ffdfdf')
    except KeyError:
        response_string=f"Handle **{hd}** doesn't exist:/"
        await event.edit(response_string)

@client.on(events.NewMessage(outgoing=True, pattern="^!bf.*"))
async def cfff(event):
    url='https://codeforces.com/api/user.rating?handle='
    hd=event.raw_text.split()[1]
    #print(hd)
    response = requests.get(url+hd)
    js=(response.json())
    try:
        dct=js['result']
        max_rank=-1
        min_rank=10000000
        max_cont=''
        min_cont=''
        max_id=''
        min_id=''
        for i in dct:
                #print(i)
            if i['rank']>max_rank:
                max_cont=i['contestName']
                max_rank=i['rank']
                max_id=i['contestId']
                    #print(max_cont)
            if i['rank']<min_rank:
                min_cont=i['contestName']
                min_rank=i['rank']
                min_id=i['contestId']
                max_rank=max(max_rank,i['rank'])
                min_rank=min(min_rank,i['rank'])
        url1='https://codeforces.com/api/contest.status?contestId={}&from=1&count=20&handle={}'
        response1 = requests.get(url1.format(max_id,hd))
        response2 = requests.get(url1.format(min_id,hd))
        js1=response1.json()
        js2=response2.json()
        dct1=js1['result']
        dct2=js2['result']
        has={}
        has1={}
        question_solved1=0
        question_solved2=0
        for i in dct1:
            if i['verdict']=='OK' and i['author']['participantType']=='CONTESTANT':
                has['contestId'+i['problem']['index']]=1
        for i in dct2:
            if i['verdict']=='OK' and i['author']['participantType']=='CONTESTANT':
                has1['contestId'+i['problem']['index']]=1
        #print(len(has),len(has1))
        question_solved1=len(has)
        question_solved2=len(has1)
        reponse3=f'User **{hd}** has achieved highest rank `{min_rank}` during round **{min_cont}** with `{question_solved2}` problem/problems solved\n'+f'User **{hd}** has achieved lowest rank `{max_rank}` during round **{max_cont}** with `{question_solved1}` problem/problems solved\n'
        await event.edit(reponse3)
    except KeyError:
        await event.edit(f'Handle {hd} doesn\'t exist :/')
        
    
    
                            

    print(max_rank,min_rank,max_cont)

    


