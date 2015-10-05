#!/usr/bin/env python

'''
		Copyright (C) 2015 Raiz Kane <raiz@airmail.cc>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Importing necessary libraries/modules

import os
import argparse
import random
import base64

# Functions must be defined here for later execution



# The whole code goes here

parser = argparse.ArgumentParser()
parser.add_argument('seed', help='your seed goes here')
args = parser.parse_args()
os.system("echo " + args.seed + " > /tmp/pwd")
os.system("clear")
os.system("pwgen -cnyH /tmp/pwd")
os.system("echo ahW6eiBaair6AhsaEomi2beeohZae8wiOoga6eeVAeM4theiGee5ahl4UChu6ieG > /tmp/pwd")
os.system("rm /tmp/pwd")
