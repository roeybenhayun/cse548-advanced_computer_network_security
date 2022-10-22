#!/bin/sh


IPTABLES="/sbin/iptables"

$IPTABLES -P INPUT DROP
$IPTABLES -P OUTPUT DROP
$IPTABLES -P FORWARD DROP

echo "Whitelist iptables complete"
