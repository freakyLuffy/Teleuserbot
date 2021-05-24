from start import client
from modules import codeforces,delete,notes,pastebin,pin,pm,user,spam
white=[1296026566,867524384,1022865230]
CUSTOM_TEXT={'en':'Speak English!',
             'pass':'you need to pass the test. leave the group and join again,a test button will appear on your screen. give that test, score well and get passed.',
             'ask':'Don\'t ask to ask',
             'pur':'What\'s',
             'link':'https://t.me/joinchat/VCUDq5aOJsF1WmEK',
             'pm':'Hello there! Welcome to Hima\'s **PM**.\n Why would I **block** you?\n 1. I would **block** you for sending me a **Hi/Hello** in my PM!\n 2. I would **block** you for not stating the purpose of the PM!\n Before continuing , make sure you have agreed to the above terms:)'
             }

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client.start().run_until_disconnected()

