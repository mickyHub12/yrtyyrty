from Pucles.Parse import addCommand
from Pucles.MongoDB import MongoClient
import datetime

@addCommand(['id','idchat'])
def bin(_, m):
    cc = f'𝑰𝑫:<code>{m.from_user.id}</code>\n𝑪𝒉𝒂𝒕:<code>{m.chat.id}</code>'
    m.reply(cc)