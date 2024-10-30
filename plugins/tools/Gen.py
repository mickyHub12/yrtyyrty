import time
import re
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from Pucles.MongoDB import MongoClient
from pyrogram import Client, filters
from Pucles.gen import cc_gen
from Pucles.Parse import addCommand

@addCommand('gen')
def bin(_, message):
    queryU = MongoClient().user_query(message.from_user.id)
    
    if queryU is None:
        return message.reply('𝙐𝙨𝙚 𝙚𝙡 𝙘𝙤𝙢𝙖𝙣𝙙𝙤 /start 𝙥𝙖𝙧𝙖 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙘𝙤')
    if queryU['rango'] == 'Baneado':
        return message.reply('𝙀𝙨𝙩𝙖𝙨 𝘽𝙖𝙣𝙚𝙖𝙙𝙤')

    if MongoClient().grupo_query(message.chat.id) is None:
        return message.reply('❗️𝙐𝙣𝙖𝙪𝙩𝙝𝙤𝙧𝙞𝙯𝙚𝙙 𝘾𝙝𝙖𝙩')
    username = message.from_user.username
    user_id = message.from_user.id  
    global input

    if message.reply_to_message:
        input = re.findall(r'[0-9x]+', message.reply_to_message.text)
    else:
        input = re.findall(r'[0-9x]+', message.text)

    if not input:
        message.reply("""
❗️Use /gen 478291:
◃───────────────────▹
Comando Invalido ⚠️
◃───────────────────▹
❗️Use /gen CC|MM|YY|CVV""")
        return

    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input) == 2:
        cc = input[0]
        mes = input[1][0:2]
        ano = 'x'
        cvv = 'x'
    elif len(input) == 3:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = 'x'
    elif len(input) == 4:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]

    if len(input[0]) < 6:
        return message.reply(F"""
❗️Use /gen 478291:
◃───────────────────▹
Comando Invalido ⚠️
◃───────────────────▹
❗️Use /gen CC|MM|YY|CVV""", quote=True)

    if mes != 'x':
        mes_int = int(mes)
    else:
        mes_int = None

    if ano != 'x':
        ano_int = int('20' + ano) if len(ano) == 2 else int(ano)
    else:
        ano_int = None

    current_year = int(time.strftime("%Y"))
    current_month = int(time.strftime("%m"))

    if ano_int is not None and ((ano_int < current_year) or (ano_int == current_year and mes_int is not None and mes_int < current_month)):
        return message.reply('<b>❗️Error: Proporcione Bien los digitos BIN ⚠️</b>', quote=True)

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = cc_gen(cc, mes, ano, cvv)

    extra = str(cc) + 'xxxxxxxxxxxxxxxxxxxxxxx'
    if mes == 'x':
        mes_2 = 'rnd'
    else:
        mes_2 = mes
    if ano == 'x':
        ano_2 = 'rnd'
    else:
        ano_2 = ano
    if cvv == 'x':
        cvv_2 = 'rnd'
    else:
        cvv_2 = cvv

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='RE-GEN', callback_data=f"regen|{cc}|{mes}|{ano}|{cvv}|{user_id}")]
        ]
    )

    bins = message.text.split('gen ')
    func = requests.get(f'https://bins.antipublic.cc/bins/{bins[1]}')

    message.reply(f"""
𝑮𝒆𝒏𝒆𝒓𝒂𝒅𝒐𝒓 𝑫𝒆 𝑻𝒂𝒓𝒋𝒆𝒕𝒂𝒔
◃───────────────────▹
<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>
𝑩𝒊𝒏 = <code>{func.json()['bin']}</code>
𝑰𝒏𝒇𝒐 = <code>{func.json()['brand']}</code> - <code>{func.json()['type']}</code> - <code>{func.json()['level']}</code>
𝑪𝒐𝒖𝒏𝒕𝒓𝒚 = <code>{func.json()['country_flag']} | {func.json()['country']} | {func.json()['country_name']}</code>
𝑩𝒂𝒏𝒌 = <code>{func.json()['bank']}</code>
◃───────────────────▹
""", reply_markup=buttons)

@Client.on_callback_query(filters.regex(r"^regen\|"))
def on_regen(client, callback_query: CallbackQuery):
    data = callback_query.data.split("|")
    cc = data[1]
    mes = data[2]
    ano = data[3]
    cvv = data[4]
    original_user_id = int(data[5])  

    if callback_query.from_user.id != original_user_id:
        callback_query.answer("❗️Usa tu propio menú", show_alert=True)
        return

    if mes != 'x':
        mes_int = int(mes)
    else:
        mes_int = None

    if ano != 'x':
        ano_int = int('20' + ano) if len(ano) == 2 else int(ano)
    else:
        ano_int = None

    current_year = int(time.strftime("%Y"))
    current_month = int(time.strftime("%m"))

    if ano_int is not None and ((ano_int < current_year) or (ano_int == current_year and mes_int is not None and mes_int < current_month)):
        callback_query.answer('<b>❗️Error: Proporcione Bien los digitos BIN ⚠️</b>', show_alert=True)
        return

   
    func = requests.get(f'https://bins.antipublic.cc/bins/{cc}')
    bin_info = func.json()

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = cc_gen(cc, mes, ano, cvv)

    full_text = f"""
𝑮𝒆𝒏𝒆𝒓𝒂𝒅𝒐𝒓 𝑫𝒆 𝑻𝒂𝒓𝒋𝒆𝒕𝒂𝒔
◃───────────────────▹
<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>
𝑩𝒊𝒏 = <code>{func.json()['bin']}</code>
𝑰𝒏𝒇𝒐 = <code>{func.json()['brand']}</code> - <code>{func.json()['type']}</code> - <code>{func.json()['level']}</code>
𝑪𝒐𝒖𝒏𝒕𝒓𝒚 = <code>{func.json()['country_flag']} | {func.json()['country']} | {func.json()['country_name']}</code>
𝑩𝒂𝒏𝒌 = <code>{func.json()['bank']}</code>
◃───────────────────▹
"""

    callback_query.message.edit_text(full_text, reply_markup=callback_query.message.reply_markup)
