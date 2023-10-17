#!/usr/bin/env python3

import yaml
from yaml import load
from yaml import CLoader as Loader

NETWORK_TOPOLOGY_DICT = {}
def main():
    #reader = open('network_topology.yml' ,'r')
    #topology = yaml.load(reader)
    #for key, value in topology.items():
    #    print(key + " : " + str(value))
    with open('network_topology.yml', 'r') as reader:
        NETWORK_TOPOLOGY_DICT = yaml.load(reader, Loader=yaml.FullLoader)

    print(NETWORK_TOPOLOGY_DICT)

if __name__ == '__main__':
    main()

