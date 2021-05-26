# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.


class StopConversation(Exception):
    """raise if conversation has terminated"""


class ProcessCanceled(Exception):
    """raise if thread has terminated"""


class KannaXBotNotFound(Exception):
    """raise if kannax bot not found"""