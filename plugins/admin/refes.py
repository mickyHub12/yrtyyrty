from pyrogram import Client, filters

# Define el ID del canal donde se enviarán los mensajes
CANAL_ID = '@refes_tumbado'

@Client.on_message(filters.command("refe", prefixes=[".", "/"]) & filters.reply)
async def forward_message(client, message):
    if message.reply_to_message:
        original_message = message.reply_to_message

        try:
            # Reenvía el mensaje original al canal especificado
            await client.copy_message(
                chat_id=CANAL_ID,
                from_chat_id=original_message.chat.id,
                message_id=original_message.id
            )

            # Elimina el mensaje que contiene el comando `.refe`
            await message.delete()

        except Exception as e:
            # Maneja cualquier error durante el reenvío
            await message.reply_text(f"❗️Error al reenviar el mensaje: {str(e)}")
    else:
        # Si el comando no es una respuesta a un mensaje, envía una advertencia
        await message.reply_text("Este comando solo funciona como respuesta a otro mensaje.")