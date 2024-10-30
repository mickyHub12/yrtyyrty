import os
from Pucles.Parse import addCommand, generate_key
from Pucles.MongoDB import MongoClient
import requests

@addCommand('key')
def panel(_, message):
    client = MongoClient()
    
    queryU = client.user_query(message.from_user.id)
    if queryU is None:
        return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /register 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado':
        return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤.')
    
    queryS = client.seller(message.from_user.id)
    if not queryS:
        return message.reply('❗️𝑺𝒐𝒍𝒐 𝒂𝒅𝒎𝒊𝒏')

    data = message.text.split(' ')
    if len(data) < 2:
        return message.reply('𝑼𝒔𝒆 /key 𝑫𝒊𝒂𝒔 ')

    key = generate_key()
    days = int(data[1])
    
    # Guarda la clave en la base de datos
    client.save_key(key, days)

    # Envía el mensaje al mismo chat
    message_text = f"""𝑮𝒆𝒏𝒆𝒓𝒂𝒅𝒂 𝑺𝒖𝒄𝒄𝒆𝒔𝒇𝒖𝒍𝒍 ❇️
◃──────────────────────▹
𝑲𝒆𝒚: <code>{key}</code>
𝑼𝒔𝒐: <code>Premium</code>
𝑫𝒊𝒂𝒔: <code>{days}</code>
𝑮𝒆𝒏𝒆𝒓𝒐 𝑼𝒔𝒆𝒓: @{message.from_user.username} <code>[{queryU['rango']}]</code>
◃──────────────────────▹ """

    # Envía el mensaje al mismo chat donde se ejecutó el comando
    try:
        message.reply(message_text)
        # Enviar el log al grupo de Telegram
        enviar_log_telegram(key, days, message.from_user.username, queryU['rango'])
    except Exception as e:
        return message.reply(f'❗️Error al enviar mensaje: {str(e)}')

def enviar_log_telegram(key, days, username, rango):
    # Aquí es donde enviarás el mensaje de log al grupo de Telegram
    bot_token = os.getenv('BOT_TOKEN')  # Asumiendo que estás cargando el token desde una variable de entorno
    chat_id = -1002189313728  # Reemplaza con tu chat_id real del grupo
    
    log_message = f"""📝 <b>𝑳𝒐𝒈 𝒅𝒆 𝑮𝒆𝒏𝒆𝒓𝒂𝒄𝒊𝒐𝒏 𝒅𝒆 𝑲𝒆𝒚</b>
    𝑲𝒆𝒚: <code>{key}</code>
    𝑫𝒊𝒂𝒔: {days}
    𝑼𝒔𝒖𝒂𝒓𝒊𝒐: @{username}
    𝑹𝒂𝒏𝒈𝒐: <code>{rango}</code>
    """
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': log_message,
        'parse_mode': 'HTML'
    }
    
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f'Error al enviar log al grupo: {response.text}')
