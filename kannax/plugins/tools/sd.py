# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.
#
# Editado por fnixdev

from kannax import Message, kannax


@kannax.on_cmd(
    "sd (?:(\\d+)?\\s?(.+))",
    about={
        "header": "make self-destructable messages",
        "usage": "{tr}sd [test]\n{tr}sd [timeout in seconds] [text]",
    },
)
async def selfdestruct(message: Message):
    seconds = int(message.matches[0].group(1) or 0)
    text = str(message.matches[0].group(2))
    await message.edit(text=text, del_in=seconds)
