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
        text = "<u>Forward Information π</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>π€ Bot Info</u>"
        else:
            text += "<u>π€User Info</u>"
        text += f'\n\nπ¨βπΌ Name : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\nπ UserName : @{msg.forward_from["username"]} \n\nπ ID : <code>{msg.forward_from["id"]}</code>\n\nπ«DC : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\nπ ID : `{msg.forward_from["id"]}`\n\n\n\nπ«DC : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"!Error <b><i>{hidden}</i></b> !Error",
                quote=True,
            )
        else:
            text = f"<u>Forward Information π</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>π’ Channel</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>π£οΈ Group</u>"
            text += f'\n\nπ Name {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\nβ‘οΈ From : @{msg.forward_from_chat["username"]}'
                text += f'\n\nπ ID : `{msg.forward_from_chat["id"]}`\n\nπ«DC : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\nπ ID `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)









