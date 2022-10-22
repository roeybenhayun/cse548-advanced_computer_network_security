#!/bin/sh


IPTABLES="/sbin/iptables"

$IPTABLES -F 
$IPTABLES -X 
$IPTABLES -F -t nat

echo "Cleaning iptables complete"
