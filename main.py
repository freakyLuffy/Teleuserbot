from start import client
from modules import codeforces,delete,notes,hastebin,pin,pm,user,spam,rextester
white=[]
from telethon import TelegramClient,events
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



client.start().run_until_disconnected()


