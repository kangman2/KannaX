# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

from kannax import Config, Message, kannax


@kannax.on_cmd("repo", about={"header": "link e detalhes do repositório"})
async def see_repo(message: Message):
    """see repo"""
    output = f"• **repo** : [KannaX]({Config.UPSTREAM_REPO})"
    await message.edit(output)
