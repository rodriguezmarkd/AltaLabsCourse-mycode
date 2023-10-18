#!/usr/bin/env python3

import yaml
import subprocess

def populate_dict():
    topology = {}
    with open('network_topology.yml', 'r') as reader:
        topology = yaml.load(reader, Loader=yaml.FullLoader)
    return topology
    

def build_network(topology):
    print("Creating namespaces...")
    for routers in topology['routers']:
        #print(type(routers))
        print(f"Creating {routers['name']} namespace...")
        subprocess.call(['sudo','ip','netns','add',routers['name']])
    for hosts in topology['hosts']:
        print(f"Creating {hosts['name']} namespace...")
        subprocess.call(['sudo','ip','netns','add',hosts['name']])
    for bridges in topology['subnets']:
        if bridges['bridge'] == True:
            print(f"Creating {bridges['name']}bridge namespace...")
            subprocess.call(['sudo','ip','link','add','name',bridges['name'] + 'bridge','type','bridge'])
            print(f"Setting {bridges['name']}bridge to an up state...")
            subprocess.call(['sudo','ip','link','set','dev',bridges['name'] + 'bridge','up'])
    
def main():
    network_topology = populate_dict()
    build_network(network_topology)
    #print(network_topology)
    print("Showing Created Namespaces...")
    subprocess.call(['sudo','ip','netns'])
    print("Showing up bridges")
    subprocess.call(['sudo','brctl','show'])
if __name__ == '__main__':
    main()

