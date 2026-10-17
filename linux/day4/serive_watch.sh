#!/bin/bash

count=1

while [ "$count" -le 3 ]
do

  echo "Checking serive ...attempt $count"

  systemctl is-active  --quiet cron

  if [ "$?" -eq 0 ]; then
     echo "Cron service: HEALTHY"
  else
      echo "cron service: UNHEALTHY:

  fi

echo "_____________________"
