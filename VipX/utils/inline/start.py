from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕹 𝐀𝐃𝐃 𝐌𝐄 𝐋𝐎𝐍𝐃𝐔 ☹︎🕹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋𝐅𝐄𝐀𝐓𝐔𝐑𝐄🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️𝐒𝐄𝐓𝐓𝐈𝐍𝐆⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="✚  𝐀𝐃𝐃 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏  ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="♦️𝐆𝐑𝐎𝐔𝐏♦️", url=f"https://t.me/{GROUP_USERNAME}",
            ),
            InlineKeyboardButton(
                text="♦️𝐌𝐎𝐑𝐄♦️", url=f"https://t.me/{CHANNEL_USERNAME}",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ 𝐇𝐄𝐋𝐏 ⚙️", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
