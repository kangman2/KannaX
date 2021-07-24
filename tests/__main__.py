# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.
#
# Editado por fnixdev

import os

from kannax import kannax


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../kannax/plugins/unofficial") else 'main'
    await kannax.send_message(chat_id, f'`{type_} build concluida !`')

if __name__ == "__main__":
    kannax.begin(_worker())
    print('O teste KannaX foi concluído!')
