#!/bin/bash

while inotifywait -e modify titles.txt; do play -n synth 4 pluck G1 2; done
