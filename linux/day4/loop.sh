#!/bin/bash

for file in ../*.log
do

  echo "Checking : $file"
  ERRORS=$(grep "ERROR" "$file" | wc -l)

 echo "errors: $ERRORS"

  if [ "$ERRORS" -gt 0 ]; then
    echo "$file -> UNHEALTHY"
  else
    echo "$file -> HEALTHY"
  fi


done
