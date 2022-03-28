@default_files = ('main.tex');

$pdf_mode = 3;

$latex = 'platex -synctex=1 -kanji=utf8 -halt-on-error -file-line-error %O %S';
$max_repeat = 10;

$bibtex = 'pbibtex %O %B';

$dvipdf = 'dvipdfmx %O -f ptex-ipaex.map -o %D %S';

$makeindex = 'mendex %O -s jpbase -o %D %S';
