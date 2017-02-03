#!/usr/bin/env bash

for i in {1..50}
do
    echo w `shuf -i 0-100 -n 20` >> ./data/20/uf20-0$i.cnf
done
