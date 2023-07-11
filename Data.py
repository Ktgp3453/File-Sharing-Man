# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
 ├ /start - Start Bot
 ├ /about - About this Bot
 ├ /help - Help for this Bot Command
 ├ /ping - To check bot is alive
 └ /uptime - To see bot status
 
 ❏ Command For BOT Admin
 ├ /logs - To view bot logs
 ├ /setvar - To set var with command dibot
 ├ /delvar - To delete var with the command dibot
 ├ /getvar - To see one of the vars with the boot command
 ├ /users - To view bot user statistics
 ├ /batch - To link more than one file
 ├ /speedtest - To Test the bot server speed
 └ /broadcast - To send broadcast messages to bot users

👨‍💻 Developed by </b><a href='https://t.me/Lunatic0de/101'>@Lunatic0de</a>\n
😶‍🌫️ Translated by </b><a href='https://t.me/Ktgp_3453'>@Ktgp_3453</a>
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help and Commands", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About Me", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} is a Telegram Bot to save Posts or Files that can be accessed through Specific Links.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man v4</a>

👨‍💻 Developed by </b><a href='https://t.me/Lunatic0de/101'>@Lunatic0de</a>\n
😶‍🌫️ Translated by </b><a href='https://t.me/Ktgp_3453'>@Ktgp_3453</a>
"""
