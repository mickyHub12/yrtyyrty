import time
import requests
from Pucles.Parse import addCommand, find_cards, antispam
from Pucles.MongoDB import MongoClient
from Gates.braintree_avs import BraintreeAuthWoo

@addCommand('bra')
def panel(_, message):
    if MongoClient().grupo_query(message.chat.id) == None: return message.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')

    queryU = MongoClient().user_query(message.from_user.id)
    if queryU is None:
        return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /register 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado':
        return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤.')
    if queryU['plan'] == 'Free':
        return message.reply('𝑺𝒐𝒍𝒐 𝒖𝒔𝒐 𝑷𝒓𝒆𝒎𝒊𝒖𝒎')
    if antispam(queryU['antispam'], message):
        return

    comando_info = MongoClient().collection_cuatro.find_one({"comando": "/bra"})
    
    if comando_info is None or comando_info.get('estado') != '✅':
        return message.reply(f"""
[ᚠ]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /bra
[ᚠ]𝑭𝒐𝒓𝒎𝒂𝒕: /bra C𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽 
[ᚠ]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[ᚠ]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Braintree AVS 
[ᚠ]𝑺𝒕𝒂𝒕𝒖𝒔: OFF!❌
""")

    ini = time.time()
    if message.reply_to_message:
        cc = find_cards(message.reply_to_message.text)
    else:
        cc = find_cards(message.text)

    if '<b>ingrese la ccs.</b>' in cc:
        return message.reply(f"""
[ᚠ]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /bra
[ᚠ]𝑭𝒐𝒓𝒎𝒂𝒕: /bra C𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽 
[ᚠ]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[ᚠ]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Braintree AVS 
[ᚠ]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
""")

    ccs = '{}|{}|{}|{}'.format(cc[0],cc[1], cc[2],cc[3])
    texto_1 = message.reply(f'''
Braintree AVS 
◃──────────────────────▹
[ᚠ]𝑪𝒂𝒓𝒅: <code>{ccs}</code>
[ᚠ]𝑺𝒕𝒂𝒕𝒖𝒔: Processing...
[ᚠ]𝑪𝒉𝒆𝒄𝒌𝒆𝒅 𝑩𝒚 @{message.from_user.username}
◃──────────────────────▹''')
    bins = message.text.split(' ')  
    chk = BraintreeAuthWoo().main(ccs)
    func = requests.get(f'https://bins.antipublic.cc/bins/{bins[1]}')
    fin  = time.time()
    return texto_1.edit_text(f"""
Braintree Auth
◃──────────────────────▹
[ᚠ]𝑪𝒂𝒓𝒅: <code>{ccs}</code>
[ᚠ]𝑺𝒕𝒂𝒕𝒖𝒔: <code>{chk[0]}</code>
[ᚠ]𝑹𝒆𝒔𝒑𝒐𝒏𝒔𝒆: <code>{chk[1]}</code>
◃──────────────────────▹
[ᚠ]𝑩𝒊𝒏: <code>{cc[0][:6]}</code>
[ᚠ]𝑩𝒂𝒏𝒌: <code>{func.json()['bank']}</code>
[ᚠ]𝑰𝒏𝒇𝒐: <code>{func.json()['brand']}-{func.json()['level']}-{func.json()['type']}</code>
[ᚠ]𝑪𝒐𝒖𝒏𝒕𝒓𝒚: <code>[{func.json()['country_flag']}] | {func.json()['country']} | {func.json()['country_name']}</code>
◃──────────────────────▹
[ᚠ]𝑻/𝒕: <code>{fin-ini:0.4f}</code>
[ᚠ]𝑪𝒉𝒆𝒄𝒌 𝑩𝒚: @{message.from_user.username} <code>[{queryU['rango']}]</code>""")

