#!/bin/bash
#
# Copyright (C) 2020 by fnixdev@Github, < https://github.com/fnixdev >.
#
# Este arquivo é parte de < https://github.com/fnixdev/KannaX > project,
# e é lançado sob o "GNU v3.0 License Agreement".
# Por Favor leia < https://github.com/fnixdev/KannaX/blob/master/LICENSE >
#
# Todos os direitos reservados.

. init/logbot/core/utils.sh

api.getUpdates() {
    local params=($*)
    _getResponse $FUNCNAME ${params[*]}
}

api.sendMessage() {
    local params=(
        chat_id=$1
        text=$(urlEncode "$2")
        parse_mode=HTML
    )
    test -n $3 && params+=(reply_to_message_id=$3)
    log "$2"
    _getResponse $FUNCNAME ${params[*]}
}

api.editMessageText() {
    local params=(
        chat_id=$1
        message_id=$2
        text=$(urlEncode "$3")
        parse_mode=HTML
    )
    log "$3"
    _getResponse $FUNCNAME ${params[*]}
}

api.deleteMessage() {
    local params=(
        chat_id=$1
        message_id=$2
    )
    unset _allMessages[$3]
    _getResponse $FUNCNAME ${params[*]}
}
