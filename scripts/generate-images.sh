#!/bin/bash

set -e

cd $(dirname $0)

poetry run python -m num_anal_plots.make_pdf_plot
