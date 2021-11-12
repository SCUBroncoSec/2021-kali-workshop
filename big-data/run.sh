#!/bin/sh
while (true); do
    cat flag.txt | nc -l 7331
done