#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json

"""
    Get all data from user input

    @param:     host (list)         networkdevices
    @return     (list)              list of all networkdevices
"""
def gather_data(hosts):
    print('-' * 60)
    print('')
    hostname = input('Rechnername: ')
    mac = input('MAC Adresse: ')
    ipv4 = input('IPv4 Adresse: ')
    print('')
    print('-' * 60)
    hosts.append({'hostname': hostname, 'mac': mac, 'ipv4': ipv4})
    return hosts


"""
    Export python to csv and save to file

    @param:     file (str)          file to save data in
    @param:     host (list)         networkdevices
    @return     void (bool)
"""
def save_to_file_as_csv(file, hosts):
    with open(file, 'r') as fh:
        first_line = fh.readline()

    lines = list()
    with open(file, 'w') as fh:
        # first line in csv file
        if first_line[:-1] != 'hostname,mac,ip':
            fh.write('hostname,mac,ip\n')
        for item in hosts:
            fh.write(f'{item["hostname"]},{item["mac"]},{item["ipv4"]}\n')
    return True


"""
    Save all netdevices to specific file.

    @param:     file (str)          file to save data in
    @param:     host (list)         networkdevices
    @return     void (bool)
"""
def save_to_file(file, hosts):
    with open(file, 'a') as fh:
        fh.write(str(hosts))
    return True


"""
    Export all netdevices to specific file.

    @param:     file (str)          file to save data in
    @param:     host (list)         networkdevices
    @return     void (bool)
"""
def export_json(file, hosts):
    # convert into JSON
    data = json.dumps(hosts)
    with open(file, 'w') as fh:
        fh.write(data)
    return True


"""
    List all hosts

    @param:     hosts (list)         list of all networkdevices
    @param:     view  (bool)         if true, only show list of hosts
    @return     void  (bool)
"""
def list_hosts(hosts, view=True):
    os.system('clear')
    counter = -1
    print('-' * 60)
    print('')
    for item in hosts:
        counter += 1
        if counter == 0:
            continue
        print(f" [{counter}] -- {item['hostname']}")
    print('')
    print('-' * 60)
    if view is True:
        proceed = input('[Return] für Weiter ')
    return counter - 1


"""
    Edit dataset

    @param:     hosts (list)         list of all networkdevices
    @return     void (bool)
"""
def edit_data(hosts):
    list_hosts(hosts, view=False)
    dataset = input('Welcher Datensatz soll bearbeitet werden: ')
    dataset = int(dataset)
    print(hosts[dataset])
    os.system('clear')
    print('-' * 60)
    print('')
    hostname = input(f'Rechnername: [{hosts[dataset]["hostname"]}]') or hosts[dataset]['hostname']
    mac = input(f'MAC Adresse: [{hosts[dataset]["mac"]}]') or hosts[dataset]['mac']
    ipv4 = input(f'IPv4 Adresse: [{hosts[dataset]["ipv4"]}]') or hosts[dataset]['ipv4']
    print('')
    print('-' * 60)
    hosts[dataset]['hostname'] = hostname
    hosts[dataset]['mac'] = mac
    hosts[dataset]['ipv4'] = ipv4
    return hosts


"""
    Remove dataset

    @param:     hosts (list)         list of all networkdevices
    @return     void (bool)
"""
def remove_data(hosts):
    list_hosts(hosts, view=False)
    dataset = input('Welcher Datensatz soll gelöscht werden: ')
    print(f'entferne Host{hosts[int(dataset)]}')
    del hosts[int(dataset)]


"""
    Read data from csv file

    @param:     file                file ti read
    @param:     hosts (list)        list of all networkdevices
    @return     void (bool)
"""
def read_data(file, hosts, append=False):
    if append is False:
        hosts = list()
    with open(file, 'r') as fh:
        for line in fh.readlines():
            hostname, mac, ipv4 = line.split(',')
            hosts.append({'hostname': hostname, 'mac': mac, 'ipv4': ipv4[:-1]})
    return hosts


"""
    Read data from json file

    @param:     file                file ti read
    @param:     hosts (list)        list of all networkdevices
    @return     void (bool)
"""
def import_json(file, hosts, append=False):
    if append is False:
        hosts = list()
    with open(file, 'r') as fh:
        data = json.load(fh)
    hosts = hosts + data
    return hosts


"""
    Error Test

    @return     void (bool)
"""
def generate_error(message):
    raise Exception(message)
