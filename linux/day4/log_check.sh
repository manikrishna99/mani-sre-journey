#!/bin/bash

LOGFILE="$1"

if [ ! -f "$LOGFILE" ]; then
   echo "ERROR: Log file not found: $LOGFILE"
   exit 1
fi

echo "Checking application logs..."
Total=$(wc -l < ~/sre-training/linux/app.log)
ERRORS=$(grep "ERROR" ~/sre-training/linux/app.log | wc -l)
Non=$(grep -v "ERROR" ~/sre-training/linux/app.log | wc -l)
echo "Total log entries : $Total"
echo "Total errors : $ERRORS"
echo "Non-error entries : $Non"

if [ "$ERRORS" -gt 0 ]; then
   echo "WARNING: Application has errors!"
   exit 1
else
   echo "Application is healthy!"
   exit 0
fi
