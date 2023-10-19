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

    
    subprocess.call(['sudo','sysctl','net.bridge.bridge-nf-call-iptables=0'])
    subprocess.call(['echo','\'net.ipv4.ip_forward','=','1\n','net.ipv6.conf.default.forwarding','=','1\n','net.ipv6.conf.all.forwarding','=','1\'','|','sudo','tee','/etc/sysctl.d/10-ip-forwarding.conf'])

    for routers in topology['routers']:
        print(f"Creating {routers['name']} namespace...")
        subprocess.call(['sudo','ip','netns','add',routers['name']])
        if routers['ds_bridge'] != None:
            #print(routers['ds_bridge'])
            subprocess.call(['sudo','ip','link','add',routers['name'] + '2' + routers['ds_bridge'],'type','veth','peer','name',routers['ds_bridge'] + '2' + routers['name']])
            subprocess.call(['sudo','ip','link','set',routers['name'] + '2' + routers['ds_bridge'],'netns',routers['name']])
            subprocess.call(['sudo','ip','link','set','dev',routers['ds_bridge'] + '2' + routers['name'],'master',routers['ds_bridge']])
            subprocess.call(['sudo','ip','link','set','dev',routers['ds_bridge'] + '2' + routers['name'],'up'])
            print(f"Connecting {routers['name']} to core...")
            subprocess.call(['sudo','ip','link','add','core' + '2' + routers['name'],'type','veth','peer','name',routers['name'] + '2' + 'core'])
            subprocess.call(['sudo','ip','link','set','core' + '2' + routers['name'],'netns','core'])
            subprocess.call(['sudo','ip','link','set',routers['name'] + '2' + 'core','netns',routers['name']])

        subprocess.call(['sudo','ip','netns','exec',routers['name'],'sysctl','-p','/etc/sysctl.d/10-ip-forwarding.conf'])        
        #for hosts in topology['hosts']:

    for hosts in topology['hosts']:
        print(f"Creating {hosts['name']} namespace...")
        ltr = str(hosts['name'][1])
        subprocess.call(['sudo','ip','netns','add',hosts['name']])
        subprocess.call(['sudo','ip','link','add',hosts['name'] + '2' + hosts['bridge'],'type','veth','peer','name',hosts['bridge'] + '2' + hosts['name']])
        subprocess.call(['sudo','ip','link','set',hosts['name'] + '2' + hosts['bridge'],'netns', hosts['name']])
        subprocess.call(['sudo','ip','link','set','dev',hosts['bridge'] + '2' + hosts['name'],'master', hosts['bridge']])
        subprocess.call(['sudo','ip','link','set','dev',hosts['bridge'] + '2' + hosts['name'],'up'])

        #print(f'Configuring {hosts['name']} with an IP of {hosts['ip']}')
        #subprocess.call('sudo','ip','netns','exec',hosts['name'],'ip','addr','add',hosts['ip'] + '/24','dev',''

    print(f"Connecting core to NAT...")
    subprocess.call(['sudo','ip','link','add','core2nat','type','veth','peer','name','nat2core'])
    subprocess.call(['sudo','ip','link','set','core2nat','netns','core'])

    subprocess.call(['sudo','sysctl','net.bridge.bridge-nf-call-iptables=0'])
    subprocess.call(['echo','\'net.ipv4.ip_forward','=','1\n','net.ipv6.conf.default.forwarding','=','1\n','net.ipv6.conf.all.forwarding','=','1\'','|','sudo','tee','/etc/sysctl.d/10-ip-forwarding.conf'])

def main():
    network_topology = populate_dict()

    build_network(network_topology)

    print("Showing Created Namespaces...")
    subprocess.call(['sudo','ip','netns'])

    print("Showing up bridges")
    subprocess.call(['sudo','brctl','show'])

if __name__ == '__main__':
    main()

