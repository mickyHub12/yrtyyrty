from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient
import datetime

@addCommand(['my','me','info','yo'])
def bin(_, message):
    # Obtener el ID y nombre de usuario del mensaje original
    target_user_id = message.from_user.id
    target_username = message.from_user.username
    
    # Verificar si el mensaje es una respuesta a otro mensaje
    if message.reply_to_message:
        target_user_id = message.reply_to_message.from_user.id
        target_username = message.reply_to_message.from_user.username
    # Verificar si se proporcionó un ID de usuario como argumento
    elif message.text.strip().split()[1:]:
        target_user_id = int(message.text.strip().split()[1])
        # Obtener el nombre de usuario a partir del ID de usuario
        user_info = _.get_chat(target_user_id)
        target_username = user_info.username

    queryU = MongoClient().user_query(target_user_id)
    if queryU is None: 
        return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /start 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado': 
        return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤.')

    tiempo = datetime.datetime.fromtimestamp(queryU['fecha_registro'])
    data = f'<code>{tiempo.day}/{tiempo.month}/{tiempo.year}</code>'

    if queryU['since'] is None:
        since = 'Sin plan'
    else:
        tiempo = datetime.datetime.fromtimestamp(queryU['since'])
        fecha_actual = datetime.datetime.now()
        fecha_futura = datetime.datetime(tiempo.year, tiempo.month, tiempo.day)
        diferencia = fecha_futura - fecha_actual
        since = f'{diferencia.days} 𝑫𝒊𝒂𝒔 𝑹𝒆𝒔𝒕𝒂𝒏𝒕𝒆𝒔'

    message.reply(f"""<b>𝑷𝒆𝒓𝒇𝒊𝒍
𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆: @{target_username}
𝑰𝑫:<code>{target_user_id}</code>
𝑹𝒂𝒏𝒈𝒐:<code>{queryU['rango']}</code>
𝑷𝒍𝒂𝒏:<code>{queryU['plan']}</code>
𝑨𝒏𝒕𝒊𝑺𝒑𝒂𝒎:<code>{queryU['antispam']}</code>
𝑪𝒓𝒆𝒅𝒊𝒕𝒐𝒔:<code>{queryU['creditos']}</code>
𝑫𝒊𝒂𝒔:<code>{since}</code>""")
