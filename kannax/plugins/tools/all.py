# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

from kannax import Message, kannax

from .. import get_all_plugins


@kannax.on_cmd("all", about={"header": "list all plugins in plugins/ path"})
async def getplugins(message: Message):
    raw_ = get_all_plugins()
    out_str = f"**--({len(raw_)}) Plugins Available!--**\n\n"
    for plugin in ("/".join(i.split(".")) for i in raw_):
        out_str += f"    `{plugin}.py`\n"
    await message.edit(text=out_str, del_in=0)
