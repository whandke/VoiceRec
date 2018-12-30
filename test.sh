#!/bin/bash
#!/usr/bin/env python
OK=0
ALL=0

for file in $( ls voice/*_[MK].wav)
do 
    let ALL=$ALL+1
    sex=${file: -5}
    sex=${sex:0:1}
    res=$(/usr/bin/python $PWD/voicerec.py $file)
    if [ $res = $sex ]; then
        echo "${file: -9} OK"
        let OK=$OK+1
    else
        echo "${file: -9} WRONG"
    fi
done
echo "Success rate: $OK/$ALL"