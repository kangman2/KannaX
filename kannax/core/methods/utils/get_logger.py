# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

__all__ = ['GetLogger']

import inspect

from kannax import logging

_LOG = logging.getLogger(__name__)
_LOG_STR = "<<<!  #####  %s  #####  !>>>"


class GetLogger:  # pylint: disable=missing-class-docstring
    @staticmethod
    def getLogger(name: str = '') -> logging.Logger:  # pylint: disable=invalid-name
        """ This returns new logger object """
        if not name:
            name = inspect.currentframe().f_back.f_globals['__name__']
        _LOG.debug(_LOG_STR, f"Creating Logger => {name}")
        return logging.getLogger(name)
