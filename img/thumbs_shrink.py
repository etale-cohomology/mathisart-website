#!/usr/bin/env python3.6
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import mathisart as m
from PIL import Image  # pip36 install pillow


# ----------------------------------------------------------------------
MIN_WIDTH  = 640
MIN_HEIGHT = 360


# ----------------------------------------------------------------------
files = m.listdir()
# m.print(*files)

thumbnails = []
for filename in files:
  if(filename.endswith('.jpg')):
    if(filename.startswith('thumb')):
      img = Image.open(filename)
      if(all([img.width > MIN_WIDTH, img.height > MIN_HEIGHT])):
        thumbnails.append(img)
        print('ADD   {}'.format(filename))
      else:
        print('SKIP  {}'.format(filename))

print('\nFound {} thumbnails for shrinking!\n'.format(len(thumbnails)))


# ----------------------------------------------------------------------
for img in thumbnails:
  img.aspect = img.width / img.height
  new_width_based_on_height = round(MIN_HEIGHT * img.aspect)
  new_height_based_on_width = round(MIN_WIDTH / img.aspect)
  good_width_flag  = new_width_based_on_height >= MIN_WIDTH
  good_height_flag = new_height_based_on_width >= MIN_HEIGHT
  # print('{}  {:4}  {:4}  {:3}/{}  {:4}/{}  {:1}|{:1}|{:1}'.format(img.filename, img.width, img.height, new_width_based_on_height, MIN_WIDTH, new_height_based_on_width, MIN_HEIGHT, good_width_flag, good_height_flag, good_width_flag or good_height_flag))

  if(good_width_flag):
    new_width = new_width_based_on_height
    new_height = MIN_HEIGHT
  elif(good_height_flag):
    new_width = MIN_WIDTH
    new_height = new_height_based_on_width
  print('{}  ({:4},{:4}) -> ({},{:4})'.format(img.filename, img.width, img.height, new_width, new_height))

  img_small = img.resize((new_width, new_height), Image.ANTIALIAS)
  img_small.save(img.filename)
