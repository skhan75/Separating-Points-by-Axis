#!/bin/bash
FILES=input/*.txt
counter=0
 
for f in $FILES
do
	python Separating.py -f $f -n $counter
	let counter=counter+1 
done