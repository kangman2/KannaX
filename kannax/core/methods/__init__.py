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

__all__ = ['Methods']

from .chats import Chats
from .decorators import Decorators
from .messages import Messages
from .users import Users
from .utils import Utils


class Methods(Chats, Decorators, Messages, Users, Utils):
    """ kannax.methods """
