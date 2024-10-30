from Pucles.Parse import addCommand, Client
from Pucles.MongoDB import MongoClient
from Pucles.plantillas import start_cmand, start_text
import datetime

@addCommand('start')
async def start(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    if queryU is None:
        # Register the user if not already registered
        MongoClient().register_user(
            message.from_user.id,
            'User',
            0,
            60,
            0,
            None,
            datetime.datetime.now().timestamp()
        )
        texy = f"""
NUEVO USUARIO REGISTRADO EN ASUS CHK
NAME: {message.from_user.first_name}
USER: @{message.from_user.username}
ID: {message.from_user.id}"""
        await Client.send_message(_, chat_id= -4573603239, text=texy)

 
    await Client.send_photo(
        _,
        chat_id=message.chat.id,
        caption=start_text.format(message.from_user.username, message.from_user.id),
        reply_markup=start_cmand,
        reply_to_message_id=message.id,
        photo='https://i.imgur.com/9csgHMQ.jpeg'
)
