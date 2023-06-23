import sys

card_number = int(sys.argv[1])
color_number = int(sys.argv[2])

# card_number = 4
# color_number = 4

colors = ['255,69,0', '255,140,0', '34,139,34', '100,149,237', '30,144,255', '0,0,128', '138,43,226', '139,0,139',
		  '255,20,147', '210,105,30']

f = open('single_image_creation.tex', 'w')
f.write(chr(92) + 'documentclass[tikz,border=0pt]' + chr(123) + 'standalone}' + '\n')
f.write(chr(92) + 'definecolor' + chr(123) + 'CardColor}' + chr(123) + 'RGB}{' + colors[color_number-1] + '}' + '\n')

f.write(chr(92) + 'newlength{' + chr(92) + 'cardwidth}' + '\n')
f.write(chr(92) + 'newlength{' + chr(92) + 'cardheight}' + '\n')
f.write(chr(92) + 'setlength{' + chr(92) + 'cardwidth}{6mm}' + '\n')
f.write(chr(92) + 'setlength{' + chr(92) + 'cardheight}{10mm}' + '\n')

f.write(chr(92) + 'begin' + chr(123) + 'document}' + '\n')
f.write(chr(92) + 'begin' + chr(123) + 'tikzpicture}' + '\n')


f.write('' + chr(92) + 'path[fill=CardColor] (0mm, 0mm) rectangle (' + chr(92) + 'cardwidth, ' + chr(92) + 'cardheight);' + '\n')
f.write('' + chr(92) + 'draw (.5' + chr(92) + 'cardwidth, .5' + chr(92) + 'cardheight) node [text width=.5' + chr(92) + 'cardwidth, align=center, color = white]{' + chr(92) + 'fontsize{10}{2}' + chr(92) + 'selectfont' + str(card_number) + '};' + '\n')

f.write(chr(92) + 'end' + chr(123) + 'tikzpicture}' + '\n')
f.write(chr(92) + 'end' + chr(123) + 'document}' + '\n')


# pdflatex -no-shell-escape  images/single_image_creation.tex


