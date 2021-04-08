#!/usr/bin/env py
"""
To run, try:
  py grid2html.py

---------------------------------------------------------------------------------------------------
# Grid grammar definition

  link := ^\\link .*\n
  image := ^\\link .*\n
  title := ^\\title .*\n
  text := ^\\text .*\n

---------------------------------------------------------------------------------------------------
A parsing expression grammar (PEG) is a formal grammar: it describes a formal language in terms of *rules for recognizing strings in the language*.
Introduced by Bryan Ford (2004). Closely related to the family of top-down parsing languages introduced in the early 1970s.
Syntactically, PEGs also look similar to CFGs, but they have a different interpretation:
the choice operator selects the first match in PEG, while it is ambiguous in CFG.
This is closer to how string recognition tends to be done in practice, e.g. by a recursive descent parser.
PEGs are well-suited to parsing computer languages (and artificial human languages such as Lojban),
but not natural languages where the performance of PEG algorithms is comparable to general CFG algorithms such as the Earley algorithm.
"""

# -------------------------------------------------------------------------------------------------
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import mathisart as m
import re

# -------------------------------------------------------------------------------------------------
GRID_FILENAME         = 'cells.grid'
HTML_PREFIX_FILENAME  = 'index_prefix.html'
HTML_POSTFIX_FILENAME = 'index_postfix.html'
HTML_OUT_FILENAME     = 'index.html'

# -------------------------------------------------------------------------------------------------
# Grid grammar implementation!
RE_GRID_LINK     = re.compile(r'\\link (.*)')
RE_GRID_IMAGE    = re.compile(r'\\image (.*)')
RE_GRID_TITLE    = re.compile(r'\\title (.*)')
RE_GRID_TEXT     = re.compile(r'\\text (.*)')
RE_GRID_COMMENTS = re.compile(r'[\n]?/\*.*?\*/[\n]?', re.MULTILINE|re.DOTALL)

# -------------------------------------------------------------------------------------------------
TEMPLATE_HTML = r'''
          <div class='mdl-cell mdl-cell--3-col mdl-cell--4-col-phone mdl-cell--4-col-tablet cell_outer'>
            <a href='{link}'>
              <div class='cell_mid'>
                <img src='{image}' class='cell_img'/>
                <div class='cell_inner'>
                  <div class='cell_title'>{title}</div>
                  <div class='cell_text'>{text}</div>
                </div>
              </div>
            </a>
          </div>'''

# -------------------------------------------------------------------------------------------------
m.sep()
HTML_PREFIX  = m.file_read(HTML_PREFIX_FILENAME)
HTML_POSTFIX = m.file_read(HTML_POSTFIX_FILENAME)
grid_data    = m.file_read(GRID_FILENAME)
grid_data    = re.sub(RE_GRID_COMMENTS, r'', grid_data)  # Remove Grid comments!

links        = re.findall(RE_GRID_LINK,  grid_data)
images       = re.findall(RE_GRID_IMAGE, grid_data)
titles       = re.findall(RE_GRID_TITLE, grid_data)
texts        = re.findall(RE_GRID_TEXT,  grid_data)

# <1ms
cells_html_list = []
for link, image, title, text in zip(links, images, titles, texts):
  cell_html = TEMPLATE_HTML.format(link=link, image=image, title=title, text=text)
  print('  ' + title)
  cells_html_list.append(cell_html)

cells_html = ''.join(cells_html_list)

# -------------------------------------------------------------------------------------------------
html_hack = "          <div class='mdl-cell mdl-cell--4-col mdl-cell--6-col-tablet cell_outer cell_white'></div>"
html_grid = '{0}\n\n{1}\n{1}\n'.format(cells_html, html_hack)
html_full = HTML_PREFIX + html_grid + HTML_POSTFIX

# <1ms
m.file_write(HTML_OUT_FILENAME, html_full, path=os.pardir)
