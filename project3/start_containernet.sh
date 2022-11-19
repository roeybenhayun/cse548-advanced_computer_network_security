#!/bin/sh

TOPO_TYPE=single
HOSTS=4

mn --topo=$TOPO_TYPE,$HOSTS --controller=remote,port=6655 --switch=ovsk --mac
