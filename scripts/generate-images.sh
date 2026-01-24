#!/bin/bash

set -e

cd $(dirname $0)/..

poetry run python -m num_anal_plots.make_pdf_plot

wget -O ./numerical-analysis-note/logo/KLogo.pdf https://kicon.musicscience37.com/KLogo-horizontal.pdf
