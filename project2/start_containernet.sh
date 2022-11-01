#!/bin/sh

TOPO_TYPE=single
HOSTS=4

mn --topo=$TOPO_TYPE,$HOSTS --controller=remote,port=6655 --switch=ovsk --mac


# https://www.oreilly.com/library/view/software-defined-networking-with/9781783984282/1bf99372-3ace-48d9-b57c-cb581c518ddb.xhtml

# Reassigen IP address to the virtual hosts
# One way to do that 

# h1 ip addr del 10.0.0.1/8 dev h1-eth0
# h1 ip addr add 192.168.2.10/24 dev h1-eth0

# h2 ip addr del 10.0.0.2/8 dev h2-eth0
# h2 ip addr add 192.168.2.20/24 dev h2-eth0

# h3 ip addr del 10.0.0.3/8 dev h3-eth0
# h3 ip addr add 192.168.2.30/24 dev h3-eth0


# h4 ip addr del 10.0.0.4/8 dev h4-eth0
# h4 ip addr add 192.168.2.40/24 dev h4-eth0



