#!/bin/bash
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT
trap 'echo hi' USR1

initKannaX() {
    printLogo
    assertPrerequisites
    sendMessage "Inicializando KannaX ..."
    assertEnvironment
    editLastMessage "Iniciando KannaX ..."
    printLine
}

startKannaX() {
    startLogBotPolling
    runPythonModule kannax "$@"
}

stopKannaX() {
    sendMessage "Finalizando KannaX ..."
    endLogBotPolling
}

handleSigTerm() {
    log "Saindo com SIGTERM (143) ..."
    stopKannaX
    exit 143
}

handleSigInt() {
    log "Saindo com SIGINT (130) ..."
    stopKannaX
    exit 130
}

runKannaX() {
    initKannaX
    startKannaX "$@"
    local code=$?
    stopKannaX
    return $code
}
