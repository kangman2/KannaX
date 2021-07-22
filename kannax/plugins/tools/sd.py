# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

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
