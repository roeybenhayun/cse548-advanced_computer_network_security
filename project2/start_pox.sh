#!/bin/sh


# create two POX controllers
/home/ubuntu/pox/pox.py --verbose openflow.of_01 --port=6655 pox.forwarding.l2_learning pox.forwarding.L3Firewall --l2config="l2firewall.config" --l3config="l3firewall.config"

