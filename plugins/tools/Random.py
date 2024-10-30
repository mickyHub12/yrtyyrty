import requests
from time import sleep
from Pucles.Parse import addCommand

from Pucles.MongoDB import MongoClient

@addCommand('rand')
def bin(_, m):    

    queryU = MongoClient().user_query(m.from_user.id)
    
    if queryU == None: return m.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /start 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado': return m.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤')
    
    
    if MongoClient().grupo_query(m.chat.id) == None: return m.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')
    
    infake = m.text[len("/rand"):]

    print(infake)
    
    if not infake: return m.reply("""
<code>/rand AU </code> = 𝑨𝑼𝑺𝑻𝑹𝑨𝑳𝑰𝑨 
<code>/rand BR </code> = 𝑩𝑹𝑨𝑺𝑰𝑳
<code>/rand CA </code> = 𝑪𝑨𝑵𝑨𝑫𝑨
<code>/rand CH </code> = 𝑺𝑼𝑰𝒁𝑨 
<code>/rand DE </code> = 𝑨𝑳𝑬𝑴𝑨𝑵𝑰𝑨 
<code>/rand DK </code> = 𝑫𝑰𝑵𝑨𝑴𝑨𝑹𝑪𝑨 
<code>/rand ES </code> = 𝑺𝑷𝑨𝑰𝑵 
<code>/rand FI </code> = 𝑭𝑰𝑹𝑳𝑨𝑵𝑫𝑨
<code>/rand FR </code> = 𝑭𝑹𝑨𝑵𝑪𝑰𝑨 
<code>/rand GB </code> = 𝑹𝑬𝑰𝑵𝑶 𝑼𝑵𝑰𝑫𝑶
<code>/rand IE </code> = 𝑰𝑹𝑳𝑨𝑵𝑫𝑨
<code>/rand IN </code> = 𝑰𝑵𝑫𝑰𝑨
<code>/rand IR </code> = 𝑰𝑹𝑨𝑵
<code>/rand MX </code> = 𝑴𝑬𝑿𝑰𝑪𝑶 
<code>/rand NL </code> = 𝑵𝑬𝑻𝑯𝑬𝑹𝑳𝑨𝑵𝑫𝑺
<code>/rand RS </code> = 𝑺𝑬𝑹𝑽𝑰𝑨
<code>/rand TR </code> = 𝑻𝑼𝑹𝑸𝑼𝑰𝑨
<code>/rand UA </code> = 𝑼𝑲𝑹𝑨𝑵𝑰𝑨
<code>/rand US </code> = 𝑬𝑺𝑻𝑨𝑫𝑶𝑺 𝑼𝑵𝑰𝑫𝑶𝑺""")

    edit1 =  m.reply_text("𝑻𝒖𝒔 𝒅𝒂𝒕𝒐𝒔 𝒔𝒆 𝒆𝒔𝒕𝒂𝒏 𝑮𝒆𝒏𝒆𝒓𝒂𝒏𝒅𝒐")
     
    spli = infake.split()
    infake = spli[0]

    infake_api = requests.get(f'https://randomuser.me/api/?nat={infake}').json()

    name = infake_api["results"][0]["name"]
    gender = infake_api["results"][0]["gender"]
    age = infake_api["results"][0]["dob"]["age"]
    birthdate = infake_api["results"][0]["dob"]["date"]
    street = infake_api["results"][0]["location"]["street"]['number']
    street1 = infake_api["results"][0]["location"]["street"]['name']
        
    city = infake_api["results"][0]["location"]["city"]
    state = infake_api["results"][0]["location"]["state"]
    postal = infake_api["results"][0]["location"]["postcode"]
    email = infake_api["results"][0]["email"]
    country =infake_api["results"][0]["location"]["country"]


    edit1.edit(f"""
𝑮𝒆𝒏𝒆𝒓𝒂𝒅𝒐𝒓 𝒅𝒆 𝑫𝒂𝒕𝒐𝒔
◃───────────────────▹
𝑵𝒐𝒎𝒃𝒓𝒆 : <code>{name["first"]} {name["last"]}</code>
𝑮𝒆𝒏𝒆𝒓𝒐 :<code> {gender}</code>
𝑬𝒅𝒂𝒅 :<code> {age}</code>
◃───────────────────▹
𝑪𝒐𝒖𝒏𝒕𝒓𝒚 :<code> {country}</code>
𝑺𝒕𝒓𝒆𝒆𝒕 :<code> {street}- {street1}</code>
𝑪𝒊𝒕𝒚 :<code> {city}</code>
𝑺𝒕𝒂𝒕𝒆 : <code>{state}</code>
𝑪.𝑷 :<code> {postal}</code>
◃───────────────────▹
""")
    
