# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import base64
import datetime
import os
import textwrap
from shutil import copyfile

import aiofiles
from PIL import Image, ImageDraw, ImageFont

from kannax import Config, Message, get_collection, kannax

SAVED_SETTINGS = get_collection("CONFIGS")
UPDATE_PIC = False
BASE_PIC = "resources/base_profile_pic.jpg"
MDFY_PIC = "resources/mdfy_profile_pic.jpg"
LOG = kannax.getLogger(__name__)


async def _init() -> None:
    global UPDATE_PIC  # pylint: disable=global-statement
    data = await SAVED_SETTINGS.find_one({"_id": "UPDATE_PIC"})
    if data:
        UPDATE_PIC = data["on"]
        if not os.path.exists(BASE_PIC):
            with open(BASE_PIC, "wb") as media_file_:
                media_file_.write(base64.b64decode(data["media"]))


@kannax.on_cmd(
    "autopic",
    about={
        "header": "definir foto de perfil",
        "usage": "{tr}autopic\n{tr}autopic [image path]\nset timeout using {tr}sapicto",
    },
    allow_channels=False,
    allow_via_bot=False,
)
async def autopic(message: Message):
    global UPDATE_PIC  # pylint: disable=global-statement
    await message.edit("`processando...`")
    if UPDATE_PIC:
        if isinstance(UPDATE_PIC, asyncio.Task):
            UPDATE_PIC.cancel()
        UPDATE_PIC = False
        await SAVED_SETTINGS.update_one(
            {"_id": "UPDATE_PIC"}, {"$set": {"on": False}}, upsert=True
        )
        await asyncio.sleep(1)
        await message.edit("`definindo foto antiga...`")
        await kannax.set_profile_photo(photo=BASE_PIC)
        await message.edit(
            "a atualização automática da foto do perfil foi **interrompida**", del_in=5, log=__name__
        )
        return
    image_path = message.input_str
    store = False
    if os.path.exists(BASE_PIC) and not image_path:
        pass
    elif not image_path:
        profile_photo = await kannax.get_profile_photos("me", limit=1)
        if not profile_photo:
            await message.err("desculpe, não consegui encontrar nenhuma foto!")
            return
        await kannax.download_media(profile_photo[0], file_name=BASE_PIC)
        store = True
    else:
        if not os.path.exists(image_path):
            await message.err("caminho de entrada não encontrado!")
            return
        if os.path.exists(BASE_PIC):
            os.remove(BASE_PIC)
        copyfile(image_path, BASE_PIC)
        store = True
    data_dict = {"on": True}
    if store:
        async with aiofiles.open(BASE_PIC, "rb") as media_file:
            media = base64.b64encode(await media_file.read())
        data_dict["media"] = media
    await SAVED_SETTINGS.update_one(
        {"_id": "UPDATE_PIC"}, {"$set": data_dict}, upsert=True
    )
    await message.edit(
        "a atualização automática da foto do perfil foi **iniciada**", del_in=3, log=__name__
    )
    UPDATE_PIC = asyncio.get_event_loop().create_task(apic_worker())


@kannax.add_task
async def apic_worker():
    user_dict = await kannax.get_user_dict("me")
    user = "@" + user_dict["uname"] if user_dict["uname"] else user_dict["flname"]
    count = 0
    while UPDATE_PIC:
        if not count % Config.AUTOPIC_TIMEOUT:
            img = Image.open(BASE_PIC)
            i_width, i_height = img.size
            s_font = ImageFont.truetype("resources/font.ttf", int((35 / 640) * i_width))
            l_font = ImageFont.truetype("resources/font.ttf", int((50 / 640) * i_width))
            draw = ImageDraw.Draw(img)
            current_h, pad = 10, 0
            for user in textwrap.wrap(user, width=20):
                u_width, u_height = draw.textsize(user, font=l_font)
                draw.text(
                    xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                    text=user,
                    font=l_font,
                    fill=(255, 255, 255),
                )
                current_h += u_height + pad
            tim = datetime.datetime.now(
                tz=datetime.timezone(datetime.timedelta(minutes=30, hours=5))
            )
            date_time = (
                f"DATA: {tim.day}.{tim.month}.{tim.year}\n"
                f"TIME: {tim.hour}:{tim.minute}:{tim.second}\n"
                "UTC-3:00"
            )
            d_width, d_height = draw.textsize(date_time, font=s_font)
            draw.multiline_text(
                xy=(
                    (i_width - d_width) / 2,
                    i_height - d_height - int((20 / 640) * i_width),
                ),
                text=date_time,
                fill=(255, 255, 255),
                font=s_font,
                align="center",
            )
            img.convert("RGB").save(MDFY_PIC)
            await kannax.set_profile_photo(photo=MDFY_PIC)
            os.remove(MDFY_PIC)
            LOG.info("foto do perfil foi atualizada!")
        await asyncio.sleep(1)
        count += 1
    if count:
        LOG.info("a atualização da foto do perfil foi interrompida!")
