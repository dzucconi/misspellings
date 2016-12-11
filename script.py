import sys
import random
from PIL import Image

BLOCKLEN = int(sys.argv[2])

img = Image.open('./source/' + sys.argv[1])
width, height = img.size

xblock = width / BLOCKLEN
yblock = height / BLOCKLEN
blockmap = [(xb * BLOCKLEN, yb * BLOCKLEN, (xb+1) * BLOCKLEN, (yb+1) * BLOCKLEN)
  for xb in xrange(xblock) for yb in xrange(yblock)]

shuffle = list(blockmap)
shuffle.reverse()

result = Image.new(img.mode, (width, height))
for box, sbox in zip(blockmap, shuffle):
  c = img.crop(sbox)
  result.paste(c, box)

result.save('./processed/' + sys.argv[1])
