# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.
#
# Editado por fnixdev

from kannax import Config, Message, kannax


@kannax.on_cmd("string", about={"header": "Geradores de StringSession"})
async def see_string(message: Message):
    """see string"""
    output = f"""    
**Hey**, __I am using__  **KannaX** 🥰
    
    __kawaii userbot__
• **REPL** : [Gerar String](https://replit.com/@fnixdev/StringSessionKX) (Recomendado)
• **Pyrogram Bot** : [Gerar String](https://t.me/genStr_Bot)
"""
    await message.edit(output)
