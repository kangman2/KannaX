# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

__all__ = ['Methods']

from .chats import Chats
from .decorators import Decorators
from .messages import Messages
from .users import Users
from .utils import Utils


class Methods(Chats, Decorators, Messages, Users, Utils):
    """ kannax.methods """
