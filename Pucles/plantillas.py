from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

start_cmand = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("CHK_BOT", url="https://t.me/Tumbado_chk_bot"),
                                    InlineKeyboardButton("PLANES", url="https://t.me/Tumbado_chk_bot")],
                                    [InlineKeyboardButton("OWNER", url='https://t.me/Jose_t2')]
                                    ])

cmds_cmand = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("GATEWAYS", callback_data="gates"),
                                    InlineKeyboardButton("HERRAMIENTAS", callback_data="tools"),]])

gatewys_cmds_buton = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("AUTH", callback_data="auth"),
                                    InlineKeyboardButton("CCN", callback_data="ccn")],
                                    [InlineKeyboardButton("CHARGED", callback_data="charged"),
                                    InlineKeyboardButton("BACK", callback_data="back")]])

tools_cmds_buton = keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="back")]])

back_cmds_buton = InlineKeyboardMarkup([[
                                    InlineKeyboardButton("GATEWAYS", callback_data="gates"),
                                    InlineKeyboardButton("TOOLS", callback_data="tools"),]])

charged1_button = InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="gates")]])

mas_button =  InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="gates")]])

auth_button =  InlineKeyboardMarkup([[InlineKeyboardButton("BACK", callback_data="gates")]])


start_text = """ 𝑻𝒖𝒎𝒃𝒂𝒅𝒐 𝑪𝒉𝒌
◃───────────────────▹
𝑼𝒔𝒆𝒓: @{}
𝑰𝑫: <code>{}</code>
𝑮𝒂𝒕𝒆𝒔 𝑷𝒂𝒓𝒂 𝒑𝒐𝒅𝒆𝒓 𝒏𝒂𝒗𝒆𝒈𝒂𝒓 𝒖𝒔𝒂 𝒆𝒍 𝒄𝒐𝒎𝒂𝒏𝒅𝒐 /cmds
𝑫𝒊𝒔𝒇𝒓𝒖𝒕𝒂 𝒕𝒖 𝑬𝒔𝒕𝒂𝒏𝒄𝒊𝒂
◃───────────────────▹
𝑪𝒖𝒂𝒓𝒒𝒖𝒊𝒆𝒓 𝒑𝒓𝒐𝒃𝒍𝒆𝒎𝒂 𝒐 𝒃𝒖𝒈 𝒅𝒆𝒍 𝒃𝒐𝒕 𝒓𝒆𝒑𝒐𝒓𝒕𝒂𝒓 𝒂 @Nova_satured
"""

cmmds_text = """
◃───────────────────▹
𝑮𝒂𝒕𝒆𝒔 𝑶𝒏𝒍𝒊𝒏𝒆✅ = 7
𝑮𝒂𝒕𝒆𝒔 𝑶𝒇𝒇𝒍𝒊𝒏𝒆❌ = 2
◃───────────────────▹
𝑮𝒂𝒕𝒆𝒔 𝑨𝒖𝒕𝒉 = 5
𝑮𝒂𝒕𝒆𝒔 𝑭𝒓𝒆𝒆 = 1
𝑮𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒓𝒈𝒆𝒓 = 1
𝑮𝒂𝒕𝒆𝒔 𝑪𝑪𝑵 = 0
𝑮𝒂𝒕𝒆𝒔 𝑴𝒂𝒔𝒊𝒗𝒆 = 0
◃───────────────────▹
𝑶𝒘𝒏𝒆𝒓:@Jose_t2"""


gates_boton_text = '''
◃───────────────────▹
𝑮𝒂𝒕𝒆𝒔 𝑶𝒏𝒍𝒊𝒏𝒆✅ 
◃───────────────────▹
𝑮𝒂𝒕𝒆𝒔 𝑨𝒖𝒕𝒉 = 5
𝑮𝒂𝒕𝒆𝒔 𝑭𝒓𝒆𝒆 = 1
𝑮𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒓𝒈𝒆𝒓 = 1
𝑮𝒂𝒕𝒆𝒔 𝑪𝑪𝑵 = 0
𝑮𝒂𝒕𝒆𝒔 𝑴𝒂𝒔𝒊𝒗𝒆 = 0
◃───────────────────▹
𝑶𝒘𝒏𝒆𝒓:@Jose_t2'''

tools_boton_text = '''
𝑻𝒐𝒐𝒍𝒔
◃───────────────────▹
𝑮𝒆𝒏 | /gen
𝑭𝒐𝒓𝒎𝒂𝒕: /gen 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
◃───────────────────▹
𝑬𝒙𝒕𝒓𝒂 | /extra
𝑭𝒐𝒓𝒎𝒂𝒕: /extra 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
◃───────────────────▹
𝑹𝒂𝒏𝒅 | /rand
𝑭𝒐𝒓𝒎𝒂𝒕: /rand us
◃───────────────────▹
𝑩𝒊𝒏 | /bin
𝑭𝒐𝒓𝒎𝒂𝒕: /bin cc   
◃───────────────────▹'''

charged1_text = '''
𝑮𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒓𝒈𝒆𝒓   
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /pp
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /pp 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽 
[❟❛❟]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Paypal 01.00$
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹'''

mass_text = ''' ''' #gates masschk

auth_text = '''
𝑮𝒂𝒕𝒆𝒔 𝑨𝒖𝒕𝒉   
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /br
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /br 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Braintree Auth
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /bra
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /bra C𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽 
[❟❛❟]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Braintree AVS 
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /st
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /st 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Stripe
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /fw
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /fw 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽 
[❟❛❟]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Payflow
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹      
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /vbv
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /vbv 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑭𝒓𝒆𝒆
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: 3D 
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /b3
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /b3 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑭𝒓𝒆𝒆
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Braintree auth
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅   
◃───────────────────▹ 
'''

free_text = '''
𝑮𝒂𝒕𝒆𝒔 𝑭𝒓𝒆𝒆
◃───────────────────▹      
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /vbv
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /vbv 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑭𝒓𝒆𝒆
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: 3D 
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /b3
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /b3 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑭𝒓𝒆𝒆
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Braintree auth
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: ON!✅   
◃───────────────────▹ 
'''

ccn_text = '''
𝑮𝒂𝒕𝒆𝒔 𝑪𝑪𝑵      
◃───────────────────▹
[❟❛❟]𝑪𝒐𝒎𝒎𝒂𝒏𝒅: /sh
[❟❛❟]𝑭𝒐𝒓𝒎𝒂𝒕: /sh 𝑪𝑪|𝑴𝑴|𝒀𝒀|𝑪𝑽𝑽
[❟❛❟]𝑼𝒔𝒆 = 𝑷𝒓𝒆𝒎𝒊𝒖𝒎
[❟❛❟]𝑮𝒂𝒕𝒆𝒘𝒂𝒚: Shopify 12.00$
[❟❛❟]𝑺𝒕𝒂𝒕𝒖𝒔: OFF! ❌
◃───────────────────▹'''