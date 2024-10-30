from Pucles.Parse import addCommand,Client
from Pucles.plantillas import cmds_cmand,cmmds_text

@addCommand(['cmd','cmds', 'gate', 'gates'])
async def cmds(_, message):

    await Client.send_photo(_,
                                chat_id=message.chat.id,
                                caption=cmmds_text.format(message.from_user.username,message.from_user.id),
                                reply_markup=cmds_cmand, 
                                reply_to_message_id=message.id,
                                photo='https://i.imgur.com/9csgHMQ.jpeg')
