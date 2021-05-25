# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# This file is part of < https://github.com/fnixdev/KannaX > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# All rights reserved.

from kannax.logger import logging  # noqa
from kannax.config import Config, get_version  # noqa
from kannax.core import (  # noqa
    KannaX, filters, Message, get_collection, pool)

kannax = KannaX()  # kannax is the client name
