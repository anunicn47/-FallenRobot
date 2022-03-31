import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/9f73400daaeb3f25581a6.jpg",
    "https://telegra.ph/file/7d643f401e5f48ad492c0.jpg",
    "https://telegra.ph/file/a0110920f2c74e1488c9e.jpg",
    "https://telegra.ph/file/45fb4f43583abfff076e8.jpg",
    "https://telegra.ph/file/0c7a0cc3213d0e58785c1.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ꜰᴀʟʟᴇɴ ✘ ʀᴏʙᴏᴛ​~🇮🇩**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [Ananya](https://t.me/an_unic_orn_47)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/anu_music00bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/an_unic_orn_47")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
