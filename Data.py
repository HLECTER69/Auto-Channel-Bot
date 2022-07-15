from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🤙Hey {},

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

💡 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲 : ❣️ ∂εcσ∂εɾ รεεɱαɳ ❣️
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("👑 sᴜᴘᴘᴏʀᴛ 👑", url="https://t.me/mkv_blasters")],
        [
            InlineKeyboardButton("🔮ʜᴇʟᴘ🔮", callback_data="help"),
            InlineKeyboardButton("🍻 ᴀʙᴏᴜᴛ 🍻", callback_data="about")
        ],
        [InlineKeyboardButton("🤖ᴜᴘᴅᴀᴛᴇs🤖", url="https://t.me/mkv_bots")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram channel automation bot by <a href=https://t.me/mkv_blasters><b>𝙼𝙺𝚅 𝙱𝙻𝙰𝚂𝚃𝙴𝚁𝚂</b></a>

🔮Source Code : [Click Here](https://t.me/themastertheblaster)

💡Framework : [Pyrogram](docs.pyrogram.org)

🔊Language : [Python](www.python.org)

💠Developer : <a href=https://t.me/themastertheblaster>❣️ ∂εcσ∂εɾ รεεɱαɳ ❣️</a>
    """
