#!/usr/bin/env python3

import yaml
import subprocess

def populate_dict():
    topology = {}
    with open('network_topology.yml', 'r') as reader:
        topology = yaml.load(reader, Loader=yaml.FullLoader)
    return topology
    

def build_network(topology):
    bridges = []
    print("Creating namespaces...")




    for bridges in topology['subnets']:
        if bridges['bridge'] == True:
            print(f"Creating {bridges['bridge_name']} namespace...")
            subprocess.call(['sudo','ip','link','add','name',bridges['bridge_name'],'type','bridge'])
            print(f"Setting {bridges['name']}bridge to an up state...")
            subprocess.call(['sudo','ip','link','set','dev',bridges['bridge_name'],'up'])

    for hosts in topology['hosts']:
        print(f"Creating {hosts['name']} namespace...")
        ltr = str(hosts['name'][1])
        subprocess.call(['sudo','ip','netns','add',hosts['name']])
        subprocess.call(['sudo','ip','link','add',hosts['name'] + '2' + hosts['bridge'],'type','veth','peer','name',hosts['bridge'] + '2' + hosts['name']])
        subprocess.call(['sudo','ip','link','set',hosts['name'] + '2' + hosts['bridge'],'netns', hosts['name']])
        subprocess.call(['sudo','ip','link','set','dev',hosts['bridge'] + '2' + hosts['name'],'master', hosts['bridge']])
        subprocess.call(['sudo','ip','link','set','dev',hosts['bridge'] + '2' + hosts['name'],'up'])
    
    for routers in topology['routers']:
        print(f"Creating {routers['name']} namespace...")
        subprocess.call(['sudo','ip','netns','add',routers['name']])
        if routers['ds_bridge'] != None:
            print(routers['ds_bridge'])
        #for hosts in topology['hosts']:

def main():
    network_topology = populate_dict()

    build_network(network_topology)

    print("Showing Created Namespaces...")
    subprocess.call(['sudo','ip','netns'])

    print("Showing up bridges")
    subprocess.call(['sudo','brctl','show'])

if __name__ == '__main__':
    main()

