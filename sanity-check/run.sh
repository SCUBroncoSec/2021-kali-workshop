#!/bin/sh
while (true); do
    cat flag.txt | nc -l 1337
done