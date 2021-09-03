#!/usr/bin/env bash

ck=$(cat '/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor')

choice=$(printf "Performance\nPowersave\nCancel" | dmenu -i -p $ck )

if [ $choice = "Cancel" ]
then
    exit
elif [ $choice = "Performance" ]
then
    alacritty -e bash -c 'sudo cpupower frequency-set -g performance'
    notify-send 'CPU governor changed to Performance'
    exit
elif [ $choice = "Powersave" ]
then
    alacritty -e bash -c 'sudo cpupower frequency-set -g powersave'
    notify-send 'CPU governor changed to Powersave'
    exit
fi