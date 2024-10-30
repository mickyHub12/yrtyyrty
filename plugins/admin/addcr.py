
from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient


@addCommand('addcr')
def panel(_, message):    
    try:
        if MongoClient().grupo_query(message.chat.id) == None: return message.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU == None: return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /register 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
        if queryU['rango'] == 'Baneado': return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤.')
    
        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: return message.reply('❗️𝑺𝒐𝒍𝒐 𝒂𝒅𝒎𝒊𝒏')

        data = message.text.split(' ')
        if len(data) < 3: return message.reply('𝑼𝒔𝒂 /addcr 𝑰𝑫 𝑪𝒓𝒆𝒅𝒊𝒕𝒐𝒔')

        MongoClient().addcr(int(data[1]), int(data[2]))
        message.reply(f'𝑺𝒆 𝒂𝒈𝒓𝒆𝒈𝒂𝒓𝒐𝒏 {data[2]} 𝑪𝒓𝒆𝒅𝒊𝒕𝒐𝒔 𝒂 {data[1]}')

    except:     message.reply('𝑼𝒔𝒖𝒂𝒓𝒊𝒐 𝒏𝒐 𝒆𝒏𝒄𝒐𝒏𝒕𝒓𝒂𝒅𝒐.')
    