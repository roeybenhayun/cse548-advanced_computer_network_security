#!/bin/sh


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

# esier way to chamge the ip is to use the python interface


py h1.setIP("192.168.2.10")
py h2.setIP("192.168.2.20")
py h3.setIP("192.168.2.30")
py h4.setIP("192.168.2.40")



