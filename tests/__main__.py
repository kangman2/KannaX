# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

import os

from kannax import kannax


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../kannax/plugins/unofficial") else 'main'
    await kannax.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    kannax.begin(_worker())
    print('KannaX test has been finished!')
