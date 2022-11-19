#!/bin/sh


# create a  controllers
# The L3Firewall will invoke l2firewall.config and l3firewall.config to add blocking rules
# at layer 2 and layer 3 respectivaly
/home/ubuntu/pox/pox.py --verbose openflow.of_01 --port=6655 pox.forwarding.l3_learning pox.forwarding.L3Firewall log.level -DEBUG

