from start import client
from modules import codeforces,delete,notes,hastebin,pin,pm,user,spam
white=[1296026566,867524384,1022865230]
from telethon import TelegramClient,events
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



client.start().run_until_disconnected()


