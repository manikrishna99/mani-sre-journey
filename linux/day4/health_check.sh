#!/bin/bash

LOGFILE="$1"

if [ ! -f "$LOGFILE" ]; then
   echo "ERROR : Log doesnot found : $LOGFILE"
   exit 1
fi

TOTAL=$( wc -l < "$LOGFILE")
ERRORS=$( grep "ERROR" "$LOGFILE" | wc -l)

echo "Total log entries : $TOTAL"
echo "Total errors : $ERRORS"

if [ "$ERRORS" -gt 0 ]; then
  echo "Application status : UNHEALTHY"
  exit 1
else
   echo "Application status : HEALTHY"
  exit 0
fi
