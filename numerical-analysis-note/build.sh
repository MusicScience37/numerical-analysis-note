#!/bin/bash

cd $(dirname $0)

tectonic --keep-intermediates --keep-logs main.tex
upmendex -s jpbase -o main.ind main.idx
tectonic --keep-intermediates --keep-logs main.tex
