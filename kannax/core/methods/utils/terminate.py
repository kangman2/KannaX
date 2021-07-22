# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

__all__ = ['Terminate']

import asyncio

from ...ext import RawClient


class Terminate(RawClient):  # pylint: disable=missing-class-docstring
    async def terminate(self) -> None:
        """ terminate kannax """
        if not self.no_updates:
            for _ in range(self.workers):
                self.dispatcher.updates_queue.put_nowait(None)
            for task in self.dispatcher.handler_worker_tasks:
                try:
                    await asyncio.wait_for(task, timeout=0.3)
                except asyncio.TimeoutError:
                    task.cancel()
            self.dispatcher.handler_worker_tasks.clear()
        await super().terminate()
