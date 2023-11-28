#!/bin/bash

for i in {0..7}; do
    for j in {0..7}; do
        chain=$((2**i))
        unroll=$((2**j))

        echo $chain $unroll
        python3 skeleton_ind_loop.py $chain $unroll
    done
done

for i in {0..5}; do
    unroll=$((2**i))

    echo $unroll
    python3 skeleton_red_loop.py $unroll
done
