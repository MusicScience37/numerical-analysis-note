#!/usr/bin/env perl

@default_files = ('main.tex');

$pdf_mode = 4;

$lualatex = 'lualatex -synctex=1 -halt-on-error -file-line-error %O %S';
$pdflualatex = $lualatex;
$max_repeat = 10;

$bibtex = 'bibtex %O %B';

$makeindex = 'mendex %O -s jpbase -o %D %S';
