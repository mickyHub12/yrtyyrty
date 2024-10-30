
from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient


@addCommand('addgp')
def panel(_, message):    
    try:
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU == None: return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /register 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
        if queryU['rango'] == 'Baneado': return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤.')
    
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: return message.reply('❗️𝑺𝒐𝒍𝒐 𝒂𝒅𝒎𝒊𝒏')

        data = message.text.split(' ')
        if len(data) < 3: return message.reply('𝑼𝒔𝒂 /addgp 𝑰𝑫 𝑫𝒊𝒂𝒔')

        MongoClient().save_grupos(int(data[1]), int(data[2]))
        message.reply(f'𝑺𝒆 𝒉𝒂𝒏 𝒂𝒈𝒓𝒆𝒈𝒂𝒅𝒐 𝒅𝒊𝒂𝒔 {data[2]} 𝑷𝒂𝒓𝒂 𝒆𝒍 𝑪𝒉𝒂𝒕 : {data[1]}')

    
    except:     message.reply('𝑼𝒔𝒖𝒂𝒓𝒊𝒐 𝒏𝒐 𝒆𝒏𝒄𝒐𝒏𝒕𝒓𝒂𝒅𝒐.')
    