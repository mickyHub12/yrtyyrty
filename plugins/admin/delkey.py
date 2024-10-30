from Pucles.Parse import addCommand, Client
from Pucles.MongoDB import MongoClient

@addCommand('dkey')
def delete_key_command(_, message):
    client = MongoClient()
    
    # Verifica si el usuario es un administrador
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
        return message.reply('𝑼𝒔𝒆 /delete_key 𝑲𝒆𝒚')

    key = data[1].strip()  # Elimina espacios adicionales

    # Verifica si la clave está en la colección 'keys'
    key_in_keys = client.key_query(key)
    if key_in_keys:
        # Intenta eliminar la clave de la colección 'keys'
        result = client.delete_key(key)
        if result:
            message.reply(f"""𝑲𝒆𝒚 𝑬𝒍𝒊𝒎𝒊𝒏𝒂𝒅𝒶 𝑺𝒖𝒄𝒄𝒆𝒔𝒇𝒖𝒍𝒍 ❌
◃──────────────────────▹
𝑲𝒆𝒚: <code>{key}</code>
◃──────────────────────▹""")
            # Enviar una notificación al canal de administración
            message_text = f"𝑬𝒍 𝒂𝒅𝒎𝒊𝒏 {message.from_user.first_name} - @{message.from_user.username} 𝑬𝒍𝒊𝒎𝒊𝒏𝒐 𝒍𝒂 𝒌𝒆𝒚:\n\n<code>{key}</code> ❌"
            Client.send_message(_, chat_id=-1002162268729, text=message_text)
            return

    # Verifica si la clave está asociada a algún usuario en la colección 'users'
    user_with_key = client.users.find_one({'key': key})
    if user_with_key:
        # Elimina la clave del usuario
        client.users.update_one({'user_id': user_with_key['user_id']}, {'$unset': {'key': ''}})
        message.reply(f"""𝑲𝒆𝒚 𝑬𝒍𝒊𝒎𝒊𝒏𝒂𝒅𝒶 𝑺𝒖𝒄𝒄𝒆𝒔𝒇𝒖𝒍𝒍 ❌
◃──────────────────────▹
𝑲𝒆𝒚: <code>{key}</code>
◃──────────────────────▹""")
        # Enviar una notificación al canal de administración
        message_text = f"𝑬𝒍 𝒂𝒅𝒎𝒊𝒏 {message.from_user.first_name} - @{message.from_user.username} 𝑬𝒍𝒊𝒎𝒊𝒏𝒐 𝒍𝒂 𝒌𝒆𝒚:\n\n<code>{key}</code> ❌"
        Client.send_message(_, chat_id=-1002162268729, text=message_text)
        return

    # Si la clave no está en ninguna colección
    message.reply("❗️𝑲𝒆𝒚 𝑵𝒐 𝑬𝒙𝒊𝒔𝒕𝒆")
