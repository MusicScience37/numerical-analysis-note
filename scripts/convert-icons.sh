#!/bin/bash -e

cd $(dirname $0)/../icon-logo

convert icon512.png -background none -resize 192x192 -quality 90 icon192.png
convert icon512.png -define icon:auto-resize=192,64,48,32,16 icon.ico
identify icon.ico
