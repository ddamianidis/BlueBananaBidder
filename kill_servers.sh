#!/bin/bash
bbidder_server_id=$(ps aux | grep bbidder_server | grep -v grep)
if [[ -n $bbidder_server_id ]]; then
    killall -9 bbidder_server
fi

bbidder_paserver_id=$(ps aux | grep bbidder_paserver | grep -v grep)
if [[ -n $bbidder_paserver_id ]]; then
    killall -9 bbidder_paserver
fi
