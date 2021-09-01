from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an open-source @EllycarlMusicbot, I let you play music in your group's voice chat.

The commands I currently support are:

/play - yanıtlanan ses dosyasını veya YouTube videosunu oynatın
/pause - ses akışını duraklat
/resume - ses akışını devam ettir
/skip - mevcut ses akışını atla
/mute - kullanıcı robotunu sessize alır
/unmute - userbot'un sesini açar
/stop - kuyruğu temizleyin ve kullanıcı robotunu aramadan çıkarın
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/Smailesi"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/Kizilsancakbilgi"
                    )
                ]
            ]
        )
    )
