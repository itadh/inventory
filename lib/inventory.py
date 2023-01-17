#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Get all data from user input

    @param:     host (list)         networkdevices
    @return     (list)              list of all networkdevices
"""
def gather_data(hosts):
    hostname = input('Rechnername: ')
    mac = input('MAC Adresse: ')
    ipv4 = input('IPv4 Adresse: ')
    hosts.append({'hostname': hostname, 'mac': mac, 'ipv4': ipv4})
    return hosts


"""
    Export python to csv and save to file

    @param:     file (str)          file to save data in
    @param:     host (list)         networkdevices
    @return     void (bool)
"""
def save_to_file_as_csv(file, hosts):
    lines = list()
    for item in hosts:
        lines.append(f'{item["hostname"]},{item["mac"]},{item["ipv4"]}\n')
    with open(file, 'a') as fh:
        for line in lines:
            fh.write(line)
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
    List all hosts

    @param:     host (list)         list of all networkdevices
    @return     void (bool)
"""
def list_hosts(hosts):
    counter = 0
    for item in hosts:
        counter += 1
        print(f" [{counter}] -- {item['hostname']}")
