""" setup auto pm message """

# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.
#
# Editado por fnixdev

import asyncio
from typing import Dict

from kannax import Config, Message, filters, get_collection, kannax
from kannax.utils import SafeDict
from kannax.utils.extras import reported_user_image

CHANNEL = kannax.getCLogger(__name__)
SAVED_SETTINGS = get_collection("CONFIGS")
ALLOWED_COLLECTION = get_collection("PM_PERMIT")
PMPERMIT_MSG = {}


pmCounter: Dict[int, int] = {}
allowAllFilter = filters.create(lambda _, __, ___: Config.ALLOW_ALL_PMS)
noPmMessage = bk_noPmMessage = (
    "▫️ `This is  A.I. Security Protocol` [▫️](https://telegra.ph/file/5807c69bf40fb39621b4a.mp4)\n\n"
    "__Hey {mention}.__\n"
    "__Meu mestre não aceita mensagem de estranhos.__\n"
    "__Espere até que ele aprove você 😊.__"
)
blocked_message = bk_blocked_message = "**You were automatically blocked**"


async def _init() -> None:
    global noPmMessage, blocked_message  # pylint: disable=global-statement
    async for chat in ALLOWED_COLLECTION.find({"status": "allowed"}):
        Config.ALLOWED_CHATS.add(chat.get("_id"))
    _pm = await SAVED_SETTINGS.find_one({"_id": "PM GUARD STATUS"})
    if _pm:
        Config.ALLOW_ALL_PMS = bool(_pm.get("data"))
    _pmMsg = await SAVED_SETTINGS.find_one({"_id": "CUSTOM NOPM MESSAGE"})
    if _pmMsg:
        noPmMessage = _pmMsg.get("data")
    _blockPmMsg = await SAVED_SETTINGS.find_one({"_id": "CUSTOM BLOCKPM MESSAGE"})
    if _blockPmMsg:
        blocked_message = _blockPmMsg.get("data")


@kannax.on_cmd(
    "allow",
    about={
        "header": "allows someone to contact",
        "description": "Ones someone is allowed, "
        "KannaX will not interfere or handle such private chats",
        "usage": "{tr}allow [username | userID]\nreply {tr}allow to a message, "
        "do {tr}allow in the private chat",
    },
    allow_channels=False,
    allow_via_bot=False,
)
async def allow(message: Message):
    """allows to pm"""
    userid = await get_id(message)
    if userid:
        if userid in pmCounter:
            del pmCounter[userid]
        Config.ALLOWED_CHATS.add(userid)
        a = await ALLOWED_COLLECTION.update_one(
            {"_id": userid}, {"$set": {"status": "allowed"}}, upsert=True
        )
        if a.matched_count:
            await message.edit("`Já aprovado para mensagem privada`", del_in=3)
        else:
            await (await kannax.get_users(userid)).unblock()
            await message.edit("`Aprovado para mensagem privada`", del_in=3)

        if userid in PMPERMIT_MSG:
            await kannax.delete_messages(userid, message_ids=PMPERMIT_MSG[userid])
            del PMPERMIT_MSG[userid]

    else:
        await message.edit(
            "Preciso responder a um usuário ou fornecer o nome de usuário/id ou estar em um chat privado",
            del_in=3,
        )


@kannax.on_cmd(
    "nopm",
    about={
        "header": "Activates guarding on inbox",
        "description": "Ones someone is allowed, "
        "KannaX will not interfere or handle such private chats",
        "usage": "{tr}nopm [username | userID]\nreply {tr}nopm to a message, "
        "do {tr}nopm in the private chat",
    },
    allow_channels=False,
    allow_via_bot=False,
)
async def denyToPm(message: Message):
    """disallows to pm"""
    userid = await get_id(message)
    if userid:
        if userid in Config.ALLOWED_CHATS:
            Config.ALLOWED_CHATS.remove(userid)
        a = await ALLOWED_COLLECTION.delete_one({"_id": userid})
        if a.deleted_count:
            await message.edit("`Proibido para mensagem privada`", del_in=3)
        else:
            await message.edit("`Nada foi mudado`", del_in=3)
    else:
        await message.edit(
            "Preciso responder a um usuário ou fornecer o nome de usuário/id ou estar em um chat privado",
            del_in=3,
        )


async def get_id(message: Message):
    userid = None
    if message.chat.type in ["private", "bot"]:
        userid = message.chat.id
    if message.reply_to_message:
        userid = message.reply_to_message.from_user.id
    if message.input_str:
        user = message.input_str.lstrip("@")
        try:
            userid = (await kannax.get_users(user)).id
        except Exception as e:
            await message.err(str(e))
    return userid


@kannax.on_cmd(
    "pmguard",
    about={
        "header": "Switchs the pm permiting module on",
        "description": "This is switched off in default. "
        "You can switch pmguard On or Off with this command. "
        "When you turn on this next time, "
        "the previously allowed chats will be there !",
    },
    allow_channels=False,
)
async def pmguard(message: Message):
    """enable or disable auto pm handler"""
    global pmCounter  # pylint: disable=global-statement
    if Config.ALLOW_ALL_PMS:
        Config.ALLOW_ALL_PMS = False
        await message.edit("`PM_guard ativado`", del_in=3, log=__name__)
    else:
        Config.ALLOW_ALL_PMS = True
        await message.edit("`PM_guard desativado`", del_in=3, log=__name__)
        pmCounter.clear()
    await SAVED_SETTINGS.update_one(
        {"_id": "PM GUARD STATUS"},
        {"$set": {"data": Config.ALLOW_ALL_PMS}},
        upsert=True,
    )


@kannax.on_cmd(
    "setpmmsg",
    about={
        "header": "Sets the reply message",
        "description": "You can change the default message which kannax gives on un-invited PMs",
        "flags": {"-r": "reset to default"},
        "options": {
            "{fname}": "add first name",
            "{lname}": "add last name",
            "{flname}": "add full name",
            "{uname}": "username",
            "{chat}": "chat name",
            "{mention}": "mention user",
        },
    },
    allow_channels=False,
)
async def set_custom_nopm_message(message: Message):
    """setup custom pm message"""
    global noPmMessage  # pylint: disable=global-statement
    if "-r" in message.flags:
        await message.edit("`Custom NOpm message reset`", del_in=3, log=True)
        noPmMessage = bk_noPmMessage
        await SAVED_SETTINGS.find_one_and_delete({"_id": "CUSTOM NOPM MESSAGE"})
    else:
        string = message.input_or_reply_raw
        if string:
            await message.edit("`Custom NOpm message saved`", del_in=3, log=True)
            noPmMessage = string
            await SAVED_SETTINGS.update_one(
                {"_id": "CUSTOM NOPM MESSAGE"}, {"$set": {"data": string}}, upsert=True
            )
        else:
            await message.err("invalid input!")


@kannax.on_cmd(
    "setbpmmsg",
    about={
        "header": "Sets the block message",
        "description": "You can change the default blockPm message "
        "which kannax gives on un-invited PMs",
        "flags": {"-r": "reset to default"},
        "options": {
            "{fname}": "add first name",
            "{lname}": "add last name",
            "{flname}": "add full name",
            "{uname}": "username",
            "{chat}": "chat name",
            "{mention}": "mention user",
        },
    },
    allow_channels=False,
)
async def set_custom_blockpm_message(message: Message):
    """setup custom blockpm message"""
    global blocked_message  # pylint: disable=global-statement
    if "-r" in message.flags:
        await message.edit("`Custom BLOCKpm message reset`", del_in=3, log=True)
        blocked_message = bk_blocked_message
        await SAVED_SETTINGS.find_one_and_delete({"_id": "CUSTOM BLOCKPM MESSAGE"})
    else:
        string = message.input_or_reply_raw
        if string:
            await message.edit("`Custom BLOCKpm message saved`", del_in=3, log=True)
            blocked_message = string
            await SAVED_SETTINGS.update_one(
                {"_id": "CUSTOM BLOCKPM MESSAGE"},
                {"$set": {"data": string}},
                upsert=True,
            )
        else:
            await message.err("invalid input!")


@kannax.on_cmd(
    "vpmmsg",
    about={"header": "Displays the reply message for uninvited PMs"},
    allow_channels=False,
)
async def view_current_noPM_msg(message: Message):
    """view current pm message"""
    await message.edit(f"--current PM message--\n\n{noPmMessage}")


@kannax.on_cmd(
    "vbpmmsg",
    about={"header": "Displays the reply message for blocked PMs"},
    allow_channels=False,
)
async def view_current_blockPM_msg(message: Message):
    """view current block pm message"""
    await message.edit(f"--current blockPM message--\n\n{blocked_message}")


@kannax.on_filters(
    ~allowAllFilter
    & filters.incoming
    & filters.private
    & ~filters.bot
    & ~filters.me
    & ~filters.service
    & ~Config.ALLOWED_CHATS,
    allow_via_bot=False,
    group=-1,
)
async def uninvitedPmHandler(message: Message):
    """pm message handler"""
    user_dict = await kannax.get_user_dict(message.from_user.id)
    user_dict.update({"chat": message.chat.title or "this group"})
    if message.from_user.is_verified:
        return
    if message.from_user.id in pmCounter:
        if pmCounter[message.from_user.id] > 3:
            del pmCounter[message.from_user.id]
            # await message.reply(blocked_message)
            report_img_ = await reported_user_image(message.from_user.first_name)
            await kannax.send_photo(
                message.chat.id, report_img_, caption=blocked_message
            )
            await message.from_user.block()
            await asyncio.sleep(1)
            await CHANNEL.log(
                f"#BLOCKED\n{user_dict['mention']} foi bloqueado devido a spam no pm do meu mestre!! "
            )
        else:
            pmCounter[message.from_user.id] += 1
            await message.reply(
                f"Você tem {pmCounter[message.from_user.id]} de 4 **Avisos**\n"
                "Por favor, espere até ser aprovado para pm!",
                del_in=5,
            )
    else:
        pmCounter.update({message.from_user.id: 1})
        PMPERMIT_MSG[message.from_user.id] = (
            await message.reply(
                noPmMessage.format_map(SafeDict(**user_dict))
                + "\n`- Protected by KannaX`"
            )
        ).message_id
        await asyncio.sleep(1)
        await CHANNEL.log(f"#NEW_MESSAGE\n{user_dict['mention']} enviou uma mensagem para você")


@kannax.on_filters(
    ~allowAllFilter & filters.outgoing & filters.private & ~Config.ALLOWED_CHATS,
    allow_via_bot=False,
)
async def outgoing_auto_approve(message: Message):
    """outgoing handler"""
    userID = message.chat.id
    if userID in pmCounter:
        del pmCounter[userID]
    Config.ALLOWED_CHATS.add(userID)
    await ALLOWED_COLLECTION.update_one(
        {"_id": userID}, {"$set": {"status": "allowed"}}, upsert=True
    )
    user_dict = await kannax.get_user_dict(userID)
    await CHANNEL.log(f"**#AUTO_APPROVED**\n{user_dict['mention']}")
