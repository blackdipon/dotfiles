#!/usr/bin/env bash

#if [[ $chosen = "Logout" ]]; then
#	jwm -exit
#elif [[ $chosen = "Shutdown" ]]; then
#	systemctl poweroff
#elif [[ $chosen = "Reboot" ]]; then
#	systemctl reboot
#elif [[ $chosen = "Suspend" ]]; then
#	systemctl suspend
#elif [[ $chosen = "Hibernate" ]]; then
#	systemctl hibernate
#elif [[ $chosen = "Hybrid-sleep" ]]; then
#	systemctl hibernate
#elif [[ $chosen = "Suspend-then-hibernate" ]]; then
#	systemctl suspend-then-hibernate
#fi

conf()
{
    c=$(printf "Yes\nNo" | dmenu -p "Are you Sure?")
    if [ $c = "No" ]
    then
        exit
    else
        continue
    fi
}

choice=$(printf "Shutdown\nReboot\nSleep\nCancel" | dmenu -i -p "Menu")

if [ $choice = "Cancel" ]
then
    exit
elif [ $choice = "Shutdown" ]
then
    conf
    systemctl poweroff -i
elif [ $choice = "Reboot" ]
then
    conf
    systemctl reboot -i
elif [ $choice = "Sleep" ]
then
    conf
    systemctl hybrid-sleep -i
fi