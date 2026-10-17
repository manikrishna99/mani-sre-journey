#!/bin/bash

USAGE=$(df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}')

echo "Root disk usage: $USAGE%"

if [ "$USAGE" -ge 80 ]; then
   echo " WARNING : Disk usage is high"
   exit 1
else
   echo "Disk status: HEALTHY"
  exit 0
fi
