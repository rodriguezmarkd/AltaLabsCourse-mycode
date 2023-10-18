#!/usr/bin/env python3

import yaml
import subprocess

def populate_dict():
    topology = {}
    with open('network_topology.yml', 'r') as reader:
        topology = yaml.load(reader, Loader=yaml.FullLoader)
    return topology
    

def build_network(topology):
    for key, value in topology['routers'].items():
        print(key, value)
        print(key)
        i = 0
        if key == 'routers':
            subprocess.call(['sudo','ip','netns','add',topology['routers'][i]['name']])
            i = i + 1
    print(topology.keys())
    print(topology['routers'][0]['name'])
    print(topology['routers'][1]['name'])
    print(topology['routers'][2]['name'])
def main():
    network_topology = populate_dict()
    build_network(network_topology)
    #print(network_topology)

if __name__ == '__main__':
    main()

