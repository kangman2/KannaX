# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

__all__ = ['Utils']

from .get_logger import GetLogger
from .get_channel_logger import GetCLogger
from .restart import Restart
from .terminate import Terminate


class Utils(GetLogger, GetCLogger, Restart, Terminate):
    """ methods.utils """
