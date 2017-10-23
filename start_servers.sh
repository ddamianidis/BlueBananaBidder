#!/bin/bash
bbidder_server_line=$(ps aux | grep bbidder_server | grep -v grep)
echo $bbidder_server_line
if [[ -z $bbidder_server_line ]]; then
    bbidder_server &
fi

bbidder_paserver_line=$(ps aux | grep bbidder_paserver | grep -v grep)
if [[ -z $bbidder_paserver_line ]]; then
    bbidder_paserver --limit=2 &
fi