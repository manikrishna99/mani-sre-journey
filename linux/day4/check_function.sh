#!/bin/bash

check_log() {

LOGFILE="$1"

ERRORS=$( grep "ERROR" "$LOGFILE" |wc -l)

echo "checking : $LOGFILE"
echo "Errors : $ERRORS"

if [ "$ERRORS" -gt 0 ]; then
  echo " Status: UNHEALTHY"
else
  echo " Status: HEALTHY"
fi


echo "_______________________"
}

check_log "../app.log"
check_log "../test.log"
