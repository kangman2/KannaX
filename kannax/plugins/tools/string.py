# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

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
