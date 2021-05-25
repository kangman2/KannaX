# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

from kannax import Message, kannax


@kannax.on_cmd(
    "s",
    about={"header": "search commands in KannaX", "examples": "{tr}s wel"},
    allow_channels=False,
)
async def search(message: Message):
    cmd = message.input_str
    if not cmd:
        await message.err(text="Enter any keyword to search in commands")
        return
    found = [i for i in sorted(list(kannax.manager.enabled_commands)) if cmd in i]
    out_str = "    ".join(found)
    if found:
        out = f"**--I found ({len(found)}) commands for-- : `{cmd}`**\n\n`{out_str}`"
    else:
        out = f"__command not found for__ : `{cmd}`"
    await message.edit(text=out, del_in=0)
