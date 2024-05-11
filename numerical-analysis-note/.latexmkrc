#!/usr/bin/env perl

@default_files = ('main.tex');

$pdf_mode = 4;

$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$pdflualatex = $lualatex;
$max_repeat = 10;

$bibtex = 'upbibtex %O %B';

$makeindex = 'upmendex %O -s jpbase -o %D %S';
