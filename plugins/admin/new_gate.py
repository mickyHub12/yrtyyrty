from pyrogram import Client
from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient

@addCommand('addgateway')
def registrar_comando(_, message):    
    try:
        if MongoClient().grupo_query(message.chat.id) == None: return message.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')
        queryU = MongoClient().user_query(message.from_user.id)
        if queryU is None: 
            return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /register 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
        if queryU['rango'] == 'Baneado': 
            return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤.')

        queryS = MongoClient().seller(message.from_user.id)
        if queryS == False: 
            return message.reply('❗️𝑺𝒐𝒍𝒐 𝒂𝒅𝒎𝒊𝒏')

        args = message.text.split(' ')
        if len(args) < 3: 
            return message.reply('𝑼𝒔𝒂 /addgateway /𝑵𝒐𝒎𝒃𝒓𝒆 /𝑵𝒐𝒎𝒃𝒓𝒆')

        comando, nombre = args[1:]

        MongoClient().collection_cuatro.insert_one({
            "comando": comando,
            "nombre": nombre,
            "gate": "ON✅",
            "estado": "✅",
        })

        message.reply(f'𝑺𝒆 𝑨𝒈𝒓𝒆𝒈𝒐 𝒆𝒍 𝑮𝒂𝒕𝒆𝒘𝒂𝒚: 𝑵𝒐𝒎𝒃𝒓𝒆: {nombre}, 𝑪𝒐𝒎𝒂𝒏𝒅𝒐: {comando}, 𝑺𝒕𝒂𝒕𝒖𝒔: ON✅')

    except Exception as e:     
        message.reply(f'Error: {str(e)}')



