# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

__all__ = ['Decorators']

from .raw_decorator import RawDecorator  # noqa
from .add_task import AddTask
from .on_cmd import OnCmd
from .on_filters import OnFilters
from .on_left_member import OnLeftMember
from .on_new_member import OnNewMember


class Decorators(AddTask, OnCmd, OnFilters, OnLeftMember, OnNewMember):
    """ methods.decorators """
