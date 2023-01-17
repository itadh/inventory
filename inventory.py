#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

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

"""
__VERSION__ = '0.1.0'
__AUTHOR__ = 'J0rg Zimmermann <jz@mgeg.de>'
__COPYRIGHT__ = 'Copyright (C) 2023'

# imports
import os
import lib.inventory as inv
os.system('clear')

# global variables
hosts = list()
file = 'netdevices.list'
csv_file = 'netdevices.csv'

# main
while True:
    print('[q] quit: ')
    print('[l] Auflisten aller Hosts: ')
    print('[i] Dateneingabe: ')
    print('[s] speichern in Datei: ')
    print('[e] export nach CSV: ')

    action = input('Was wollen Sie machen: ')

    if action == 'q':
        exit(0)
    if action == 'i':
        os.system('clear')
        hosts = inv.gather_data(hosts)
    if action == 's':
        hosts = inv.save_to_file(file, hosts)
    if action == 'e':
        hosts = inv.save_to_file_as_csv(csv_file, hosts)
    if action == 'l':
        os.system('clear')
        inv.list_hosts(hosts)
