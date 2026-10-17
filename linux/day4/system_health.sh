#!/bin/bash

STATUS=0
LOGFILE="$HOME/sre-training/linux/app.log"

echo "=================================="
echo "       SYSTEM HEALTH REPORT"
echo "=================================="

echo "Hostname: $(hostname)"
echo "Current user: $(whoami)"
echo "Uptime: $(uptime -p)"

DISK_USAGE=$(df -P / | awk 'NR==2 {gsub(/%/, "", $5); print $5}')
MEMORY_AVAILABLE=$(free -h | awk '/^Mem:/ {print $NF}')

echo "Root disk usage: $DISK_USAGE%"
echo "Memory available: $MEMORY_AVAILABLE"

if [ "$DISK_USAGE" -ge 80 ]; then
    echo "Disk status: WARNING"
    STATUS=1
else
    echo "Disk status: HEALTHY"
fi

if [ -f "$LOGFILE" ]; then
    ERRORS=$(grep -c "ERROR" "$LOGFILE")

    if [ "$ERRORS" -gt 0 ]; then
        echo "Application status: UNHEALTHY"
        echo "Errors found: $ERRORS"
        STATUS=1
    else
        echo "Application status: HEALTHY"
    fi
else
    echo "Application status: LOG FILE NOT FOUND"
    STATUS=1
fi

echo "----------------------------------"

if [ "$STATUS" -eq 0 ]; then
    echo "OVERALL STATUS: HEALTHY"
else
    echo "OVERALL STATUS: UNHEALTHY"
fi

echo "=================================="
exit "$STATUS"
