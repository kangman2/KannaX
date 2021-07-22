""" setup gmute """

# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved

import asyncio

from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
)
from pyrogram.types import ChatPermissions

from kannax import Config, Message, filters, get_collection, kannax

GMUTE_USER_BASE = get_collection("GMUTE_USER")
CHANNEL = kannax.getCLogger(__name__)
LOG = kannax.getLogger(__name__)


@kannax.on_cmd(
    "gmute",
    about={
        "header": "Silenciar um usuário globalmente",
        "description": "Adiciona usuário à sua lista de GMute",
        "examples": "{tr}gmute [userid|responda um usuario] [razão para gmute] (obrigatório)",
    },
    allow_channels=False,
    allow_bots=False,
)
async def gmute_user(msg: Message):
    """Silenciar um usuário globalmente"""
    await msg.edit("`Silenciando este usuário globalmente...`")
    user_id, reason = msg.extract_user_and_text
    if not user_id:
        await msg.edit(
            "`nenhum user_id válido ou mensagem especificada,`"
            "`não use .help gmute para mais informações. "
            "Porque ninguém vai te ajudar`(｡ŏ_ŏ) ⚠"
        )
        return
    get_mem = await msg.client.get_user_dict(user_id)
    firstname = get_mem["fname"]
    if not reason:
        await msg.edit(
            f"**#Abrtado**\n\n**GMuting** of [{firstname}](tg://user?id={user_id}) "
            "`Abortado, Nenhum motivo de GMute fornecido pelo usuário`",
            del_in=5,
        )
        return
    user_id = get_mem["id"]
    if user_id == msg.from_user.id:
        await msg.err(r"Lol. Por que eu me mutaria ¯\(°_o)/¯")
        return
    if user_id in Config.SUDO_USERS:
        await msg.edit(
            "`Esse usuário está na minha Lista de Sudo, portanto, não posso GMutá-lo.`\n\n"
            "**Dica:** `Remova-os da Lista de Sudo e tente novamente. (¬_¬)`",
            del_in=5,
        )
        return
    found = await GMUTE_USER_BASE.find_one({"user_id": user_id})
    if found:
        await msg.edit(
            "**#GMuted**\n\n`Este usuário já existe na minha lista de GMute.`\n"
            f"**Razão para GMute:** `{found['reason']}`"
        )
        return
    await asyncio.gather(
        GMUTE_USER_BASE.insert_one(
            {"firstname": firstname, "user_id": user_id, "reason": reason}
        ),
        msg.edit(
            r"\\**#GMuted_User**//"
            f"\n\n**Primeiro Nome:** [{firstname}](tg://user?id={user_id})\n"
            f"**ID de Usuario:** `{user_id}`\n**Razão:** `{reason}`"
        ),
    )
    chats = await kannax.get_common_chats(user_id)
    for chat in chats:
        try:
            await chat.restrict_member(user_id, ChatPermissions())
            await CHANNEL.log(
                r"\\**#Antispam_Log**//"
                f"\n**Usuario:** [{firstname}](tg://user?id={user_id})\n"
                f"**ID de usuario:** `{user_id}`\n"
                f"**Chat:** {chat.title}\n"
                f"**ID do chat:** `{chat.id}`\n"
                f"**Razão:** `{reason}`\n\n$GMUTE #id{user_id}"
            )
        except (ChatAdminRequired, UserAdminInvalid):
            pass
    if msg.reply_to_message:
        await CHANNEL.fwd_msg(msg.reply_to_message)
        await CHANNEL.log(f"$GMUTE #prid{user_id} ⬆️")
    LOG.info("G-Muted %s", str(user_id))


@kannax.on_cmd(
    "ungmute",
    about={
        "header": "Remover mute um usuário globalmente",
        "description": "Remove um usuário da sua lista de GMute",
        "examples": "{tr}ungmute [userid|responda um usuario]",
    },
    allow_channels=False,
    allow_bots=False,
)
async def ungmute_user(msg: Message):
    """desmuta um usuário globalmente"""
    await msg.edit("`UnGMuting esse usuario...`")
    user_id, _ = msg.extract_user_and_text
    if not user_id:
        await msg.err("user-id não encontrado")
        return
    get_mem = await msg.client.get_user_dict(user_id)
    firstname = get_mem["fname"]
    user_id = get_mem["id"]
    found = await GMUTE_USER_BASE.find_one({"user_id": user_id})
    if not found:
        await msg.err("Usuário não encontrado na minha lista de GMute")
        return
    await asyncio.gather(
        GMUTE_USER_BASE.delete_one(found),
        msg.edit(
            r"\\**#GMuted_User**//"
            f"\n\n**Primeiro Nome:** [{firstname}](tg://user?id={user_id})\n"
            f"**ID de Usuario:** `{user_id}`\n**Razão:** `{reason}`"
        ),
    )
    chats = await kannax.get_common_chats(user_id)
    for chat in chats:
        try:
            await chat.unban_member(user_id)
            await CHANNEL.log(
                r"\\**#Antispam_Log**//"
                f"\n**Usuario:** [{firstname}](tg://user?id={user_id})\n"
                f"**ID de usuario:** `{user_id}`\n"
                f"**Chat:** {chat.title}\n"
                f"**ID do chat:** `{chat.id}`\n"
            )
        except (ChatAdminRequired, UserAdminInvalid):
            pass
    LOG.info("UnGMuted %s", str(user_id))


@kannax.on_cmd(
    "gmlist",
    about={
        "header": "Obtenha uma lista de usuários GMuted",
        "description": "Obtenha uma lista atualizada de usuários GMuted por você.",
        "examples": "{tr}gmlist",
    },
    allow_channels=False,
)
async def list_gmuted(msg: Message):
    """visualiza usuários gmutados"""
    users = ""
    async for c in GMUTE_USER_BASE.find():
        users += "**Usuario** : " + str(c["firstname"])
        users += "\n**ID de usuario** : " + str(c["user_id"])
        users += "\n**Reason para GMuted** : " + str(c["reason"]) + "\n\n"
    await msg.edit_or_send_as_file(
        f"**--Lista de usuários Gmuted--**\n\n{users}"
        if users
        else "`Gmute List vazia`"
    )


@kannax.on_filters(
    filters.group & filters.new_chat_members, group=1, check_restrict_perm=True
)
async def gmute_at_entry(msg: Message):
    """lidar com gmute"""
    chat_id = msg.chat.id
    for user in msg.new_chat_members:
        user_id = user.id
        first_name = user.first_name
        gmuted = await GMUTE_USER_BASE.find_one({"user_id": user_id})
        if gmuted:
            await asyncio.gather(
                msg.client.restrict_chat_member(chat_id, user_id, ChatPermissions()),
                msg.reply(
                    r"\\**#𝑿_Antispam**//"
                    "\n\nUsuário globalmente silenciado detectado neste bate-papo.\n\n"
                    f"**Usuario:** [{first_name}](tg://user?id={user_id})\n"
                    f"**ID:** `{user_id}`\n**Razão:** `{gmuted['reason']}`\n\n"
                    "**Ação:** Mutado",
                    del_in=10,
                ),
                CHANNEL.log(
                    r"\\**#Antispam_Log**//"
                    "\n\n**GMuted User $SPOTTED**\n"
                    f"**Usuario:** [{first_name}](tg://user?id={user_id})\n"
                    f"**ID:** `{user_id}`\n**Razão:** {gmuted['reason']}\n**Ação:** "
                    f"Mutado em {msg.chat.title}"
                ),
            )
    msg.continue_propagation()
