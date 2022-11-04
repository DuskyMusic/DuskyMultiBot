from pyrogram import filters
from pyrogram import Client
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.fsub import ForceSub


@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    FSub = await ForceSub(motech, msg)
    if FSub == 400:
        return
    if msg.forward_from:
        text = "<u>Forward Information 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>🤖 Bot Info</u>"
        else:
            text += "<u>👤User Info</u>"
        text += f'\n\n👨‍💼 Name : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\n🔗 UserName : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>\n\n💫DC : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\n🆔 ID : `{msg.forward_from["id"]}`\n\n\n\n💫DC : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"!Error <b><i>{hidden}</i></b> !Error",
                quote=True,
            )
        else:
            text = f"<u>Forward Information 👀</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>📢 Channel</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ Group</u>"
            text += f'\n\n📃 Name {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\n➡️ From : @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 ID : `{msg.forward_from_chat["id"]}`\n\n💫DC : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\n🆔 ID `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)









