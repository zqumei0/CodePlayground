#!/bin/bash
if [ -z $1 ]; then
  echo "No number of exercises to generate provided."
  echo "Usage: $0 (number of arguments)"
  exit 1
fi

for ((i=1;i<=$1;i++)); do
  touch ./exercise_$i.go
done