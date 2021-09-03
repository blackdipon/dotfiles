#!/usr/bin/env bash

# Ondemand services start and stop script

serv=$(printf "libvert\nCancel" | dmenu -i -p "Menu")

opt=$(printf "Start\nStop\nRestart" | dmenu -i -p "Menu")

if [ $serv = "Cancel" ]
then
    exit
elif [ $serv = "libvert" ]
then
    if [ $opt = "Start" ]
    then
        systemctl start libvirtd.service
    elif [ $opt = "Restart" ]
    then
        systemctl restart libvirtd.service
    elif [ $opt = "Stop" ]
    then
        systemctl stop libvirtd.service
    fi
fi
