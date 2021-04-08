#!/usr/bin/env python3.6
import mathisart as m
import sys

# ----------------------------------------------------------------
SVG_APP    = 'rsvg'
PNG_HEIGHT = 512
PNG_WIDTH  = 512

# ----------------------------------------------------------------
def fail_no_file():
  m.print('FAIL  Must provide an SVG file as first argument')
  exit()

def fail_no_svg():
  m.print('FAIL  The first argument must be a file ending in \'.svg\'')
  exit()

if(len(sys.argv) < 2):  fail_no_file()
svg = sys.argv[1]
if(not svg.endswith('.svg')):  fail_no_svg()

# ----------------------------------------------------------------
png = f'{svg[:-4]}.png'
print(f'Converting `{svg}` to `{png}`')

# ----------------------------------------------------------------
cmd = f'{SVG_APP} -h {PNG_WIDTH} -w {PNG_HEIGHT} {svg} {png}'
print(f'RUN  {cmd}')

with m.timeit():
  m.shell_run(cmd)

# rsvg -h 256 -w 256 icon_algebra.svg icon_algebra.png && fehf icon_algebra.png
