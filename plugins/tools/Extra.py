import time
import random
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Pucles.Parse import addCommand
from Pucles.gen import cc_gen
from Pucles.MongoDB import MongoClient


@addCommand('extra')
def extra(_, message):    

    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU == None: return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /start 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado': return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤')
    
    if MongoClient().grupo_query(message.chat.id) == None: return message.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')

    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]
    yo = BIN[0:9]
    que = yo

    req = requests.get(
                    f"https://bins.antipublic.cc/bins/{BIN}").json()
                
    level = req['level']
    type = req['type']
    brand = req['brand']
    country = req['country']
    country_name = req['country_name']
    country_flag = req['country_flag']
    
    que = BIN   
    
    hola0 = (random.randint(2024, 2030))
    hola1 = (random.randint(2024, 2030))
    hola2 = (random.randint(2024, 2030))
    hola3 = (random.randint(2024, 2030))
    hola4 = (random.randint(2024, 2030))
    hola5 = (random.randint(2024, 2030))
    hola6 = (random.randint(2024, 2030))
    hola7 = (random.randint(2024, 2030))
    hola8 = (random.randint(2024, 2030))
    hola9 = (random.randint(2024, 2030))
    si0 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si1 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si2 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si3 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si4 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si5 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si6 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si7 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si8 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si9 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    
    

    extra0 = (random.randrange(100000, 950000, 3))
    extra9 = (random.randrange(100000, 950000, 3))
    extra1 = (random.randrange(100000, 950000, 3))
    extra2 = (random.randrange(100000, 950000, 3))
    extra3 = (random.randrange(100000, 950000, 3))
    extra4 = (random.randrange(100000, 950000, 3))
    extra5 = (random.randrange(100000, 950000, 3))
    extra6 = (random.randrange(100000, 950000, 3))
    extra7 = (random.randrange(100000, 950000, 3))
    extra8 = (random.randrange(100000, 950000, 3))
    

    message.reply(f"""<b>
𝙀𝙭𝙩𝙧𝙖𝙨 𝙀𝙣 𝘿𝘽 🚀
◃───────────────────▹
<code>{que}{extra0}xxxx|{si0}|{hola0}|rnd</code>
<code>{que}{extra9}xxxx|{si1}|{hola1}|rnd</code>
<code>{que}{extra1}xxxx|{si2}|{hola2}|rnd</code>
<code>{que}{extra2}xxxx|{si3}|{hola3}|rnd</code>
◃───────────────────▹
𝑩𝒊𝒏 = <code>{BIN}</code>         
𝑰𝒏𝒇𝒐 = <code>{level} - {type} - {brand}</code>
𝑪𝒐𝒖𝒏𝒕𝒓𝒚 = <code>{country} - {country_name} - {country_flag}</code>
""")
   








    