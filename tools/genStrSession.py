# pylint: disable=invalid-name, missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "KannaX",
            api_id=int(os.environ.get("API_ID") or input("Insira Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Insira Telegram API HASH: ")
    ) as kannax:
        print("\nprocessando...")
        await kannax.send_message(
            "me", f"#KannaX #HU_STRING_SESSION\n\n```{await kannax.export_session_string()}```")
        print("Pronto !, string de sessão foi enviada para mensagens salvas!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
