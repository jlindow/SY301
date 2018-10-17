#!/bin/bash

for i in {0..1000000..500000}
  do
    OUTPUT=`/usr/bin/time -f %U ./cArray $i 2>&1`
    #OUTPUT=`/usr/bin/time -f %U ./cArray5 $i 2>&1`
    #OUTPUT=`/usr/bin/time -f %U ./cList $i 2>&1`
    #OUTPUT=`/usr/bin/time -f %U python3 pyList.py $i 2>&1`
    echo "$i, $OUTPUT"
 done
