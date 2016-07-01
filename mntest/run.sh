#!/bin/bash

dir=$(pwd)

for i in $(seq 1 9)
do
	mkdir $dir/results/000$i
done
for i in $(seq 10 99)
do
	mkdir $dir/results/00$i
done
for i in $(seq 100 999)
do
	mkdir $dir/results/0$i
done
for i in $(seq 1000 1005)
do
	mkdir $dir/results/$i
done
