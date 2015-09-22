#!/bin/bash
# Copyright (C) 2015 Raiz Kane <raiz@airmail.cc>
# you are free to use, modify, distribute
# this software under the terms of the
# GNU General Public License v3, see
# https://www.gnu.org/licenses/gpl-3.0.txt
# for more details.

read -p "Seed: " PASSVAR
echo $PASSVAR > /tmp/pwd
clear
pwgen -cnyH /tmp/pwd
echo $RANDOM | sha512sum | base64 > /tmp/pwd
rm /tmp/pwd
