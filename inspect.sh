#!/bin/sh

set -ex

lscpu
free -h
cat /proc/meminfo
top -b -n 1
