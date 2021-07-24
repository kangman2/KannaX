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

__all__ = ["send_msg", "reply_last_msg", "edit_last_msg", "del_last_msg", "end"]


def _log(func):
    def wrapper(text, log=None, tmp=None):
        if log and callable(log):
            if tmp:
                log(tmp, text)
            else:
                log(text)
        func(text)
    return wrapper


def _send_data(*args) -> None:
    with open("logs/logbot.stdin", 'a') as l_b:
        l_b.write(f"{' '.join(args)}\n")


@_log
def send_msg(text: str, log=None, tmp=None) -> None:  # pylint: disable=unused-argument
    """ enviar mensagem """
    _send_data("sendMessage", text)


@_log
def reply_last_msg(text: str, log=None, tmp=None) -> None:  # pylint: disable=unused-argument
    """ responder a última mensagem """
    _send_data("replyLastMessage", text)


@_log
def edit_last_msg(text: str, log=None, tmp=None) -> None:  # pylint: disable=unused-argument
    """ editar a última mensagem """
    _send_data("editLastMessage", text)


def del_last_msg() -> None:
    """ apagar a última mensagem """
    _send_data("deleteLastMessage")


def end() -> None:
    """ terminar sessão de bot """
    _send_data("quit")
