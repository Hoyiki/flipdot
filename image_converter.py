#python -f xxx.png

#this script converts any image to black & white with size 28*28, but this is for references only. Better to edit the outcome in PhotoShop.
#python2

from __future__ import print_function
from PIL import Image, ImageDraw
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--file',
    action="store", dest="image_loc", default="")
options, args = parser.parse_args()

im = Image.open(options.image_loc).convert('1')
im.thumbnail((28,28))
im.show()
