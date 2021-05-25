# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Messages']

from .send_message import SendMessage
from .edit_message_text import EditMessageText
from .send_as_file import SendAsFile


class Messages(SendMessage, EditMessageText, SendAsFile):
    """ methods.messages """
