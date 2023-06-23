# import sys

# card_number = int(sys.argv[1])
# color_number = int(sys.argv[2])

card_number = 2
color_number = 2

colors = ['50,205,50', '48, 122, 219', '255,69,0', '231, 250, 254', '254, 231, 250']

f = open('images/single_image_creation.tex', 'w')
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





