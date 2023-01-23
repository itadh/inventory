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
file = 'netdevices.list'
csv_file = 'netdevices.csv'
json_file = 'netdevices.json'
hosts = inv.read_data(csv_file, list())

# main
while True:
    print('-' * 60)
    print('')
    print('   [q] quit: ')
    print('   [l] Auflisten aller Hosts: ')
    print('   [e] Dateneingabe: ')
    print('   [b] Datensatz bearbeiten: ')
    print('   [d] Daten löschen: ')
    print('   [r] Daten einlesen: ')
    print('   [a] eingelese Daten anhängen: ')
    print('   [i] JSON Import: ')
    print('   [x] JSON Export: ')
    print('   [s] speichern in Datei: ')
    print('')
    print('-' * 60)
    action = input('Was wollen Sie machen: ')

    os.system('clear')
    if action == 'q':
        break
    elif action == 'e':
        hosts = inv.gather_data(hosts)
    elif action == 's':
        inv.save_to_file_as_csv(csv_file, hosts)
    elif action == 'b':
        inv.edit_data(hosts)
    elif action == 'd':
        inv.remove_data(hosts)
    elif action == 'r':
        # liest Datei ein und ueberschreibt hosts
        hosts = inv.read_data(csv_file, hosts)
    elif action == 'a':
        # liest Datei ein und haengt die Daten an hosts an
        hosts = inv.read_data(csv_file, hosts, True)
    elif action == 'i':
        # importiert JSON aus Dateiliest Datei ein und haengt die Daten an hosts an
        hosts = inv.import_json(json_file, hosts, True)
    elif action == 'I':
        # importiert JSON aus Datei ein und ueberschreibt hosts
        hosts = inv.import_json(json_file, hosts)
    elif action == 'x':
        # exportiert JSON in Datei
        inv.export_json(json_file, hosts)
    elif action == 'l':
        inv.list_hosts(hosts)

os.system('clear')
exit(0)
