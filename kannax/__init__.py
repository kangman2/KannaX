# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

from kannax.logger import logging  # noqa
from kannax.config import Config, get_version  # noqa
from kannax.core import (  # noqa
    KannaX, filters, Message, get_collection, pool)

kannax = KannaX()  # kannax is the client name
