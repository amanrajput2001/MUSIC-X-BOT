from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
š š§šµš¶š šš šš±šš®š»š°š² š§š²š¹š²š“šæš®šŗ š ššš¶š° šš¼š \nšŗš„šš» š¢š» š£šæš¶šš®šš² š©š£š¦ š¦š²šæšš²šæ \nš¼šš²š²š¹ šš¶š“šµ š¤šš®š¹š¶šš š ššš¶š° šš» šš šššÆšš„šØš©šš šš² @itsamanrajput
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā°š¢šš»š²šæā±", url="https://t.me/itsamanrajput")
                  ],[
                    InlineKeyboardButton(
                        "ā°š¦šš½š½š¼šæšā±", url="https://t.me/bestfrnsforever"
                    ),
                    InlineKeyboardButton(
                        "ā°ššæš¼šš½ā±", url="https://t.me/bestfrnsforever"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ā°š¦š¼ššæš°š²ā±", url="https://municipa.li/"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ššššš ššš šššššš ššš šš\nš šššš šššššš šš <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š¼š¦šš½š½š¼šæš", url="https://t.me/bestfrnsforever")
                ]
            ]
        )
   )
