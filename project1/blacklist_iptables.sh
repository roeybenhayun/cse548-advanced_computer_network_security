#!/bin/sh


IPTABLES="/sbin/iptables"

$IPTABLES -P INPUT ACCEPT
$IPTABLES -P OUTPUT ACCEPT
$IPTABLES -P FORWARD ACCEPT

echo "Whitelist iptables complete"
