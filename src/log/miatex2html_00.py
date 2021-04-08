#!/usr/bin/env py
"""
To run, try:
  py miatex2html.py *.md

---------------------------------------------------------------------------------------------------
# Data flow

1. markdown --> tex: groups00.md -> temp.tex
2. tex --> mathjax/html: eg. temp.tex -> temp.html (using pandoc!)
3. markdown --> html: temp.html -> temp.html (using the custom regex found in this file!)

---------------------------------------------------------------------------------------------------
# mathIsART-Markdown language

- Italics must be preceded by a whitespace or a linefeed, and NOT the beginning of a file!
"""
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import mathisart as m
import re
import subprocess
import bs4  # pip36 install bs4 && pip36 install lxml

# -------------------------------------------------------------------------------------------------
FILENAME_TEMP_MD   = 'temp.md'
FILENAME_TEMP_TEX  = 'temp.tex'
FILENAME_TEMP_HTML = 'temp.html'


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
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

# Shell commands for pandoc!
# COMMAND0 = 'pandoc {} -o {}'.format(FILENAME_TEMP_MD, FILENAME_TEMP_TEX)
COMMAND1 = 'pandoc {} --mathjax -o {}'.format(FILENAME_TEMP_TEX, FILENAME_TEMP_HTML)  # --mathjax --mathml --katex

# Stuff!
m.sep()
HTML_PREFIX  = m.file_read('article_prefix.html')
HTML_POSTFIX = m.file_read('article_postfix.html')


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
for cli_argument in sys.argv[1:]:
  m.sep()
  FILENAME_IN = cli_argument if cli_argument.endswith('.md') else '{}.md'.format(cli_argument)  # Accept only `.md` files!
  FILENAME_OUT = cli_argument[0:-3] if cli_argument.endswith('.md') else cli_argument
  FILENAME_OUT += '.html'

  # -------------------------------------------------------------------------------------------------
  """
  `.groups()` only returns explicitly-captured groups in your regex (denoted by round brackets `(` round brackets ) in your regex)
  `.group(0)` returns the entire substring matched by your regex regardless of whether your expression has any capture groups.
  The first explicit capture in your regex is indicated by group(1) instead.
  """
  data_md = m.file_read(FILENAME_IN)  # <1ms

  # Doing these replacements takes 1ms
  title_page    = re.search(RE_MIA_TITLE_PAGE, data_md).group(1)
  title_article = re.search(RE_MIA_TITLE_ARTICLE, data_md).group(1)

  category0 = re.search(RE_MIA_CATEGORY0, data_md)  # Find category
  category1 = re.search(RE_MIA_CATEGORY1, data_md)  # Find category
  category2 = re.search(RE_MIA_CATEGORY2, data_md)  # Find category
  category3 = re.search(RE_MIA_CATEGORY3, data_md)  # Find category
  category0 = category0.group(1) if category0 is not None else ''
  category1 = category1.group(1) if category1 is not None else ''
  category2 = category2.group(1) if category2 is not None else ''
  category3 = category3.group(1) if category3 is not None else ''

  print('  {:14} : {}'.format('title_page', title_page))
  print('  {:14} : {}'.format('title_article', title_article))
  print('  {:14} : {}'.format('category0', category0))
  print('  {:14} : {}'.format('category1', category1))
  print('  {:14} : {}'.format('category2', category2))
  print('  {:14} : {}'.format('category3', category3))

  # -------------------------------------------------------------------------------------------------
  # Parse mathIsART-Markdown!

  # Doing these naive replacements takes 1ms!
  SEP = '---------------------------------------------------------------------------------------------------\n'
  data_md = data_md.replace(SEP,              r'')

  data_md = data_md.replace(r'\qed',          '$\\tab$ $\\square$')
  data_md = data_md.replace(' \\lf\n',        ' \\\\\n')  # Replace mathIsART-Markdown newlines with TeX newlines!
  data_md = data_md.replace(r'\example ',     r'$\tab$ *Example*. ')
  data_md = data_md.replace(r'\proof ',       r'$\tab$ *Proof*. ')
  data_md = data_md.replace(r'\remark ',      r'$\tab$ *-Remark*. ')

  data_md = data_md.replace(r'\theorem ',     r'$\tab$ **Theorem**. ')
  data_md = data_md.replace(r'\definition ',  r'$\tab$ **Definition**. ')
  data_md = data_md.replace(r'\proposition',  r'$\tab$ **Proposition**. ')
  data_md = data_md.replace(r'\lemma',        r'$\tab$ **Lemma**. ')

  data_md = data_md.replace(r'\defined ',     r'\hskip8pt := \hskip8pt ')
  data_md = data_md.replace(r'\equals ',      r'\hskip8pt = \hskip8pt ')
  data_md = data_md.replace(r'\pipe ',        r'\hskip6pt | \hskip6pt ')

  data_md = data_md.replace(r'\Po',           r'{ \mathcal P }')
  data_md = data_md.replace(r'\subset',       r'\subseteq')
  data_md = data_md.replace(r'\propersubset', r'\subset')
  data_md = data_md.replace(r'\compose',      r'\circ')

  # Handle miaTeX command for theorems!
  TEMPLATE_THEOREM = r'$\tab$ **Theorem {content}**. '
  for theorem in re.findall(r'\\theorem\{.*\}', data_md):
    content = re.search(r'\{.*\}', theorem).group()
    content = content.replace('{', '').replace('}', '')  # print(theorem, TEMPLATE_THEOREM.format(content=content))
    data_md = data_md.replace(theorem, TEMPLATE_THEOREM.format(content=content))

  # -------------------------------------------------------------------------------------------------
  # Parse (standard) Markdown! VERY HARD!! 3ms!

  # Sanitize URLs for TeX!
  for hyperlink in re.findall(RE_MD_HYPERLINKS, data_md):
    hyperlink_old = '[{}][{}]'.format(*hyperlink)
    hyperlink_new = hyperlink_old.replace('%', '\\%')
    data_md = data_md.replace(hyperlink_old, hyperlink_new)
    # print(hyperlink_new)  # print(hyperlink)  # print('  {:32} : {}'.format(*hyperlink))

  data_md = re.sub(RE_MD_BOLD,       r'{\\bf \1}', data_md)  # Parse Markdown bold!
  data_md = re.sub(RE_MD_ITALIC0,    r' {\\it \1}', data_md)  # Parse Markdown italic, 1st pass!
  data_md = re.sub(RE_MD_ITALIC1,    r'\n{\\it \1}', data_md)  # Parse Markdown italic, 2nd pass!
  data_md = re.sub(RE_MD_COMMENTS,   r'', data_md)  # Parse Markdown comments!
  data_md = re.sub(RE_MD_HYPERLINKS, r'\\href{\2}{\1}', data_md)  # Parse Markdown hyperlinks!

  m.file_write(FILENAME_TEMP_TEX, data_md)

  # -------------------------------------------------------------------------------------------------
  # import mistletoe
  # from mistletoe.latex_renderer import LaTeXRenderer
  # data_latex = mistletoe.markdown(data_md, LaTeXRenderer)  # 100ms
  # m.print(data_latex)
  # m.file_write(FILENAME_TEMP_TEX, data_latex)

  # import mistune
  # mistune_markdown = mistune.Markdown()
  # data_lala = mistune_markdown(data_md)  # 20ms!
  # m.file_write(FILENAME_TEMP_TEX, data_lala)

  # print('RUN  {}'.format(COMMAND0))
  # m.shell_run(COMMAND0)  # 130ms, markdown --> tex

  print('RUN  {}'.format(COMMAND1))
  subprocess.run(COMMAND1, shell=True)  # 80ms, tex --> mathjax/html

  # -------------------------------------------------------------------------------------------------
  # Assemble HTML for article!
  html_data    = m.file_read(FILENAME_TEMP_HTML)
  sep          = '<!-- ---------------------------------------------------------------------- -->\n'
  prefix       = "<div id='article_text' class='mdl-color-text--grey-700 mdl-card__supporting-text'>"
  postfix      = "</div>"
  html_article = '{sep}{}\n\n{}\n{}\n{sep}'.format(prefix, html_data, postfix, sep=sep)
  # m.print(html_article)

  # -------------------------------------------------------------------------------------------------
  # <1ms
  html_full = '{prefix}\n\n{article}\n\n{postfix}'.format(prefix=HTML_PREFIX, article=html_article, postfix=HTML_POSTFIX)

  # 70ms
  soup = bs4.BeautifulSoup(html_full, 'lxml')  # lxml is the fastest BS4 parser, I think!
  soup.find('title').string += title_page
  soup.find(id='title_article').string = title_article
  soup.find(id='category0').string = category0
  soup.find(id='category1').string = category1
  soup.find(id='category2').string = '/ ' + category2 if category2 else category2
  soup.find(id='category3').string = '/ ' + category3 if category3 else category3
  html_full = str(soup)

  # <1ms
  m.file_write(FILENAME_OUT, html_full, path=os.pardir)
