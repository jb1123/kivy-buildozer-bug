#!/bin/sh
# A simple build script using p4 directly

opt=$HOME/opt

ANDROIDSDK="/home/jb/opt/android-sdk-linux"
ANDROIDNDK="/home/jb/opt/android-ndk-r13"
ANDROIDAPI="19"  # Minimum API version your application require
ANDROIDNDKVER="r13"  # Version of the NDK you installed

export ANDROIDSDK="$ANDROIDSDK"
export ANDROIDNDK="$ANDROIDNDK"
export ANDROIDAPI="19"  # Minimum API version your application require
export ANDROIDNDKVER="r13"  # Version of the NDK you installed


cmd="p4a apk --private nmeter --package=eu.ijbd.nmeter --name \"Nmeter\" --version 0.1  --requirements=kivy,hostpython2 --bootstrap=sdl2"

echo $cmd

eval $cmd

