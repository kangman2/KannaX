# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

import asyncio
import random

from pyrogram.errors.exceptions import FloodWait

from kannax import Message, kannax


@kannax.on_cmd(
    "type", about={"header": "Simulate a typewriter", "usage": "{tr}type [text]"}
)
async def type_(message: Message):
    text = message.input_str
    if not text:
        await message.err("input not found")
        return
    s_time = 0.1
    typing_symbol = "|"
    old_text = ""
    await message.edit(typing_symbol)
    await asyncio.sleep(s_time)
    for character in text:
        s_t = s_time / random.randint(1, 100)
        old_text += character
        typing_text = old_text + typing_symbol
        try:
            await asyncio.gather(
                message.try_to_edit(typing_text, sudo=False),
                asyncio.sleep(s_t),
                message.try_to_edit(old_text, sudo=False),
                asyncio.sleep(s_t),
            )
        except FloodWait as x_e:
            await asyncio.sleep(x_e.x)
