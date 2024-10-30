from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient

@addCommand('claim')
def bin(_, message):
    client = MongoClient()
    
  
    queryU = client.user_query(message.from_user.id)
    if queryU is None:
        return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /register 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')

    if queryU['rango'] == 'Baneado':
        return message.reply('Usuario baneado no puede usarme.')

    data = message.text.split(' ')
    if len(data) < 2:
        return message.reply('𝙐𝙨𝙚 /claim Tumbado_Chk-xxxxxxx-PREMIUM ')

    querk = client.key_query(data[1])
    if querk is None:
        return message.reply('❗️𝑳𝒂 𝒌𝒆𝒚 𝒏𝒐 𝒔𝒆 𝒆𝒏𝒄𝒐𝒏𝒕𝒓𝒐 𝒆𝒏 𝒍𝒂 𝑫𝑩.')

    if querk['key'] == data[1]:
        client.addpremium(message.from_user.id, querk['dias'])
        client.delete_key(querk['key'])
        client.save_grupos(message.from_user.id, querk['dias'])

        # Usa el chat_id del mensaje original
        chat_id = message.chat.id

        key_info_message = f'''Key 𝑪𝒂𝒏𝒋𝒆𝒂𝒅𝒂:
𝑼𝒔𝒆𝒓: @{message.from_user.username}
𝑰𝑫: {message.from_user.id}
𝑲𝒆𝒚: {data[1]}
𝑫𝒊𝒂𝒔: {querk['dias']}
        '''
        
        try:
            message._client.send_message(chat_id, key_info_message)
        except Exception as e:
            return message.reply(f'❗️Error al enviar mensaje: {str(e)}')

        return message.reply(f'''𝑹𝒆𝒆𝒅𝒆𝒎 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍 ❇️
◃──────────────────────▹ 
𝑲𝒆𝒚: <code>{data[1]}</code>
𝑼𝒔𝒐: <code>Premium</code>
𝑫𝒂𝒚𝒔: <code>{querk['dias']}</code>
𝑺𝒕𝒂𝒕𝒖𝒔: @{message.from_user.username} <code>[Premium]</code>
◃──────────────────────▹''')
    else:
        return message.reply('❗️𝑲𝒆𝒚 𝒏𝒐 𝑽𝒂𝒍𝒊𝒅𝒂')
