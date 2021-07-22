# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

import asyncio
from datetime import datetime

from kannax import Message, kannax


@kannax.on_cmd(
    "ping",
    about={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
    },
    group=-1,
)
async def pingme(message: Message):
    start = datetime.now()
    if "-a" in message.flags:
        await message.edit("`!....`")
        await asyncio.sleep(0.3)
        await message.edit("`..!..`")
        await asyncio.sleep(0.3)
        await message.edit("`....!`")
        end = datetime.now()
        t_m_s = (end - start).microseconds / 1000
        m_s = round((t_m_s - 0.6) / 3, 3)
        await message.edit(f"**🏓 Average Pong!**\n`{m_s} ms`")
    else:
        await message.edit("`Pong!`")
        end = datetime.now()
        m_s = (end - start).microseconds / 1000
        await message.edit(f"**🏓 Pong!**\n`{m_s} ms`")
