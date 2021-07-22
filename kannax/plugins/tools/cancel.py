# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

from kannax import Message, kannax


@kannax.on_cmd("cancel", about={"header": "Reply this to message you want to cancel"})
async def cancel_(message: Message):
    replied = message.reply_to_message
    if replied:
        replied.cancel_the_process()
        await message.edit("`added your request to the cancel list`", del_in=5)
    else:
        await message.edit("`reply to the message you want to cancel`", del_in=5)
