from Pucles.Parse import addCommand,Client
from Pucles.MongoDB import MongoClient
import datetime


@addCommand('register')
async def start(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    if queryU == None:
        MongoClient().register_user(message.from_user.id,'User',0,60,0,None,datetime.datetime.now().timestamp())

        await message.reply('𝑻𝒖 𝒓𝒆𝒈𝒊𝒔𝒕𝒓𝒐 𝒇𝒖𝒆 𝒖𝒏 𝒆𝒙𝒊𝒕𝒐 ✅') 

        texy = f"""𝑵𝒖𝒆𝒗𝒐 𝒖𝒔𝒆𝒓 𝑹𝒆𝒈𝒊𝒔𝒕𝒓𝒂𝒅𝒐 𝑻𝒖𝒎𝒃𝒂𝒅𝒐_𝑪𝑯𝑲
𝑼𝒔𝒆𝒓: @{message.from_user.username}
𝑰𝑫: {message.from_user.id}"""

        await Client.send_message(_,chat_id=-1002189313728,text=texy)
    else:
        await message.reply('𝒀𝒂 𝒕𝒆 𝒆𝒏𝒄𝒖𝒆𝒏𝒕𝒓𝒂𝒔 𝑹𝒆𝒈𝒊𝒔𝒕𝒓𝒂𝒅𝒐')


