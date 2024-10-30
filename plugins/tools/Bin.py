import requests
from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient


@addCommand('bin')
def bin(_, message):    
    
    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU == None: return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /start 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado': return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤')
    

    if MongoClient().grupo_query(message.chat.id) == None: return message.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')
    
    try:
        BIN = message.text[len("/bin"):11].strip()
        
        if len(BIN) < 6:
            message.reply(f"""
❗️Use /bin 478291:
◃───────────────────▹
Comando Invalido ⚠️
◃───────────────────▹
❗️Use /bin CC|MM|YY|CVV""")
            return
            
        if not BIN:
            message.reply("❗️Use /bin 478291")
            return
        
        func = requests.get(f'https://bins.antipublic.cc/bins/{BIN[:6]}')

        if "{'Status': 'NOT FOUND'}" in func.text: return message.reply('❗️𝑩𝒊𝒏 𝑰𝒏𝒄𝒐𝒓𝒓𝒆𝒄𝒕𝒐')
        else:
            texto = f'''
𝑩𝒊𝒏 𝑳𝒐𝒐𝒌𝒖𝒑
◃───────────────────▹
𝑩𝒊𝒏 = <code>{BIN[:6]}</code> 
𝑵𝒊𝒗𝒆𝒍 = <code>{func.json()['level']}</code>
𝑻𝒚𝒑𝒆 ➛ <code>{func.json()['type']}</code>
𝑩𝒓𝒂𝒏𝒅 ➛ <code>{func.json()['brand']}</code>
𝑩𝒂𝒏𝒌 ➛ <code>{func.json()['bank']}</code>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➛ <code>{func.json()['country']}</code> | <code>{func.json()['country_name']}</code> | <code>{func.json()['country_flag']}</code>
◃───────────────────▹'''
            message.reply(texto)

    except: message.reply("""❗️Use /bin 478291:
◃───────────────────▹
Comando Invalido ⚠️
◃───────────────────▹
❗️Use /bin CC|MM|YY|CVV""")
