#!/bin/bash

for file in ./rawData/*.xlsx;
  do
    python3 tcr.py "$file";

  done
