# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

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
