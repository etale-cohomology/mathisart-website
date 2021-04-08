#!/usr/bin/env py
'''
To run, try:
  py miatex2html.py *.md

--------------------------------------------------------------------------------------------------------------------------------
# flow

1. markdown --> tex:          eg. groups00.md -> tmp.tex
2. tex      --> mathjax/html: eg. tmp.tex     -> tmp.html (using pandoc!)
3. markdown --> html:         eg. tmp.html    -> tmp.html (using the custom regex found in this file!)

--------------------------------------------------------------------------------------------------------------------------------
# mathIsART-Markdown language

- Italics must be preceded by a whitespace or a linefeed, and NOT the beginning of a file!
'''
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import mathisart as m
import re
import subprocess
import bs4  # pip36 install bs4 && pip36 install lxml

# -----------------------------------------------------------------------------------------------------------------------------#
FILENAME_TEMP_MD   = 'tmp00.md'
FILENAME_TEMP_TEX  = 'tmp00.tex'
FILENAME_TEMP_HTML = 'tmp00.html'


# -----------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------#
# Regex for Markdown!
regex_name    = '[^]]*'  # Anything that isn't a closing square bracket
regex_url     = '[^]]*'  # Anything that isn't a closing square bracket
regex_markup  = '\[({0})]\[\s*({1})\s*\]'.format(regex_name, regex_url)

RE_MD_COMMENTS   = re.compile(r'[\n]?<\!--.*?-->[\n]?', re.MULTILINE | re.DOTALL)
RE_MD_BOLD       = re.compile(r'\*\*([^\*]*)\*\*')
RE_MD_ITALIC0    = re.compile(r' \*([^*]*)\*')
RE_MD_ITALIC1    = re.compile(r'^\*([^*]*)\*', re.MULTILINE)
RE_MD_HYPERLINKS = re.compile(regex_markup)

# Regex for mathIsART-Markdown!
RE_MIA_TITLE_PAGE    = re.compile(r'\\title_page (.*)')
RE_MIA_TITLE_ARTICLE = re.compile(r'\\title_article (.*)')
RE_MIA_CATEGORY0     = re.compile(r'\\category0 (.*)')  # We use round brackets `()` to speficy a regex **group**
RE_MIA_CATEGORY1     = re.compile(r'\\category1 (.*)')  # We use round brackets `()` to speficy a regex **group**
RE_MIA_CATEGORY2     = re.compile(r'\\category2 (.*)')  # We use round brackets `()` to speficy a regex **group**
RE_MIA_CATEGORY3     = re.compile(r'\\category3 (.*)')  # We use round brackets `()` to speficy a regex **group**
RE_IMG_URL           = re.compile(r'\\img_url (.*)')  # We use round brackets `()` to speficy a regex **group**

# Stuff!
m.sep()
HTML_PREFIX  = m.file_read('article_prefix.html')
HTML_POSTFIX = m.file_read('article_postfix.html')


# -----------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------#
# `.groups()` only returns explicitly-captured groups in your regex (denoted by round brackets `(` round brackets ) in your regex)
# `.group(0)` returns the entire substring matched by your regex regardless of whether your expression has any capture groups.
# The first explicit capture in your regex is indicated by group(1) instead.
def parse_header(md_in):  # parse the header in the `.md` file (which is a comment block with certain directives/commands!)
  data = m.file_read(md_in)  # <1ms

  # Doing these replacements takes 1ms
  title_page    = re.search(RE_MIA_TITLE_PAGE,    data).group(1)  # Mandatory
  title_article = re.search(RE_MIA_TITLE_ARTICLE, data).group(1)  # Mandatory
  category0     = re.search(RE_MIA_CATEGORY0,     data)           # Optional
  category1     = re.search(RE_MIA_CATEGORY1,     data)           # Optional
  category2     = re.search(RE_MIA_CATEGORY2,     data)           # Optional
  category3     = re.search(RE_MIA_CATEGORY2,     data)           # Optional
  img_url       = re.search(RE_IMG_URL,           data)           # Optional
  category0     = category0.group(1) if category0 is not None else ''
  category1     = category1.group(1) if category1 is not None else ''
  category2     = category2.group(1) if category2 is not None else ''
  category3     = category3.group(1) if category3 is not None else ''
  img_url       = img_url.group(1)   if img_url   is not None else 'img/mathisart_big.png'

  print('  {:14} : {}'.format('title_page',    title_page))
  print('  {:14} : {}'.format('title_article', title_article))
  print('  {:14} : {}'.format('category0',     category0))
  print('  {:14} : {}'.format('category1',     category1))
  print('  {:14} : {}'.format('category2',     category2))
  print('  {:14} : {}'.format('category3',     category3))
  print('  {:14} : {}'.format('img_url',     img_url))
  return [title_page, title_article, category0,category1,category2,category3, img_url]

# -----------------------------------------------------------------------------------------------------------------------------#
def compile__miamd(argin, argout, arg):
  file_data = m.file_read(argin[0])  # <1ms

  SEP = '---------------------------------------------------------------------------------------------------\n'  # Doing these naive replacements takes 1ms!
  file_data = file_data.replace(SEP,              r'')

  file_data = file_data.replace(r'\qed',          '$\\tab$ $\\square$')
  file_data = file_data.replace(' \\lf\n',        ' \\\\\n')  # Replace mathIsART-Markdown newlines with TeX newlines!
  file_data = file_data.replace(r'\example ',     r'$\tab$ *Example*. ')
  file_data = file_data.replace(r'\proof ',       r'$\tab$ *Proof*. ')
  file_data = file_data.replace(r'\remark ',      r'$\tab$ *-Remark*. ')

  file_data = file_data.replace(r'\theorem ',     r'$\tab$ **Theorem**. ')
  file_data = file_data.replace(r'\definition ',  r'$\tab$ **Definition**. ')
  file_data = file_data.replace(r'\proposition',  r'$\tab$ **Proposition**. ')
  file_data = file_data.replace(r'\lemma',        r'$\tab$ **Lemma**. ')

  file_data = file_data.replace(r'\defined ',     r'\hskip8pt := \hskip8pt ')
  file_data = file_data.replace(r'\equals ',      r'\hskip8pt = \hskip8pt ')
  file_data = file_data.replace(r'\pipe ',        r'\hskip6pt | \hskip6pt ')

  file_data = file_data.replace(r'\Po',           r'{ \mathcal P }')
  file_data = file_data.replace(r'\subset',       r'\subseteq')
  file_data = file_data.replace(r'\propersubset', r'\subset')
  file_data = file_data.replace(r'\compose',      r'\circ')

  TEMPLATE_THEOREM = r'$\tab$ **Theorem {content}**. '  # Handle miaTeX command for theorems!
  for theorem in re.findall(r'\\theorem\{.*\}', file_data):
    content   = re.search(r'\{.*\}', theorem).group()
    content   = content.replace('{', '').replace('}', '')  # print(theorem, TEMPLATE_THEOREM.format(content=content))
    file_data = file_data.replace(theorem, TEMPLATE_THEOREM.format(content=content))

  # 1) parse (standard) Markdown! VERY HARD!! 3ms!
  for hyperlink in re.findall(RE_MD_HYPERLINKS, file_data):  # Sanitize URLs for TeX!
    hyperlink_old = '[{}][{}]'.format(*hyperlink)
    hyperlink_new = hyperlink_old.replace('%', '\\%')
    file_data     = file_data.replace(hyperlink_old, hyperlink_new)  # print(hyperlink_new)  # print(hyperlink)  # print('  {:32} : {}'.format(*hyperlink))

  file_data = re.sub(RE_MD_BOLD,       r'{\\bf \1}',      file_data)  # Parse Markdown bold!
  file_data = re.sub(RE_MD_ITALIC0,    r' {\\it \1}',     file_data)  # Parse Markdown italic, 1st pass!
  file_data = re.sub(RE_MD_ITALIC1,    r'\n{\\it \1}',    file_data)  # Parse Markdown italic, 2nd pass!
  file_data = re.sub(RE_MD_COMMENTS,   r'',               file_data)  # Parse Markdown comments!
  file_data = re.sub(RE_MD_HYPERLINKS, r'\\href{\2}{\1}', file_data)  # Parse Markdown hyperlinks!

  m.file_write(argout[0], file_data)

# -----------------------------------------------------------------------------------------------------------------------------#
def compile__pandoc(argin, argout, arg):
  pandon_cmd = 'pandoc  {} {} -o {}'.format(argin[0], arg[0], argout[0])  # --mathjax --mathml --katex
  print('\x1b[33mRUN  \x1b[31m{}\x1b[0m'.format(pandon_cmd))
  subprocess.run(pandon_cmd, shell=True)  # 80ms, tex --> mathjax/html

# -----------------------------------------------------------------------------------------------------------------------------#
def compile__html(argin, argout, arg):
  arg0 = arg[0] if len(arg)>0 else ''
  arg1 = arg[1] if len(arg)>1 else ''

  header        = parse_header(argin[0])
  title_page    = header[0]
  title_article = header[1]
  category0     = header[2]
  category1     = header[3]
  category2     = header[4]
  category3     = header[5]
  img_url       = header[6]

  html_data    = m.file_read(argin[1])
  html_data    = re.sub('(<!--.*?-->)', '', html_data, flags=re.DOTALL)  # Remove HTML comments!
  sep          = '<!-- ---------------------------------------------------------------------- -->\n'
  html_article = '{sep}{}\n\n{}\n{}\n{sep}'.format(arg0, html_data, arg1, sep=sep)
  html_full    = '{prefix}\n\n{article}\n\n{postfix}'.format(prefix=HTML_PREFIX, article=html_article, postfix=HTML_POSTFIX)  # <1ms

  # 70ms
  soup = bs4.BeautifulSoup(html_full, 'lxml')  # lxml is the fastest BS4 parser, I think!
  soup.find('title').string                            += title_page
  soup.find(id='title_article').string                  = title_article
  soup.find(id='category0').string                      = category0
  soup.find(id='category1').string                      = category1
  soup.find(id='category2').string                      = '/ ' + category2 if category2 else category2
  soup.find(id='category3').string                      = '/ ' + category3 if category3 else category3
  soup.find(attrs={'class':'mdl-card__media'})['style'] = f"background:url('{img_url}') no-repeat center;"
  html_full = str(soup)

  m.file_write(argout[0], html_full, path=os.pardir)  # <1ms


# -----------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------#
def compile_html(html_in, html_out):
  html_out = html_out[5:] if html_out[:5]=='html_' else html_out

  html__in  = [html_in, html_in]
  html__out = [html_out]
  html__arg = ["  <div id='article_text' class='mdl-color-text--grey-700 mdl-card__supporting-text'>", "  </div>"]
  compile__html(html__in, html__out, html__arg)

# -----------------------------------------------------------------------------------------------------------------------------#
def compile_tex(md_in, md_out):
  miamd_in  = [md_in]
  miamd_out = ['tmp.tex']
  miamd_arg = []

  pandoc_in  = [miamd_out[0]]
  pandoc_out = ['tmp.html']
  pandoc_arg = ['--mathjax']

  html_in  = [md_in, pandoc_out[0]]
  html_out = [md_out]
  html_arg = [m.file_read('mathjax.html') + "  <div id='article_text' class='mdl-color-text--grey-700 mdl-card__supporting-text'>", "  </div>"]

  compile__miamd(miamd_in, miamd_out, miamd_arg)
  compile__pandoc(pandoc_in, pandoc_out, pandoc_arg)
  compile__html(html_in, html_out, html_arg)


# -----------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------------------#
for arg in sys.argv[1:]:
  m.sep()
  path_in   = arg
  path_out  = f'{os.path.splitext(arg)[0]}.html'

  if   path_in[:3]                 =='vid':   compile_html(path_in,path_out)
  elif os.path.splitext(path_in)[1]=='.html': compile_html(path_in,path_out)
  else:                                       compile_tex(path_in,path_out)
  # else:                      print("\x1b[91mFAIL  \x1b[33mcan't recognize file prefix... skipping!\x1b[0m")
