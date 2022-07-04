import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/bot-07-04-7",
        caption=f"""**━━━━━━━━━━━━━━━━━
✨ Hello I am very fast and Simple Music player bot  Developed By Shubham
━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ Add me To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("Commands", url="https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"),
            InlineKeyboardButton("Developer", url="https://t.me/DevShubh1203")
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive", "Shubham", "/repo"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
     ),
  ) 


# @Client.on_message(commandpro(["/updates", "Channel", "/openbaby"]) & filters.group & ~filters.edited)
# async def help(client: Client, message: Message):
#     await message.reply_photo(
#         photo=f"https://te.legra.ph/file/e866cd93108978ef6faef.jpg",
#         caption=f"""""",
#         reply_markup=InlineKeyboardMarkup(
#             [
#                 [
#                     InlineKeyboardButton(
#                         "ᴊᴏɪɴ ᴛʜᴇsᴇ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ", url=f"https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw")
#                 ]
#             ]
#         ),
#     )
