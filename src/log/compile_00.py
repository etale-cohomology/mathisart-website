#!/usr/bin/env py
"""
To run, try:
  py compile.py

---------------------------------------------------------------------------------------------------
Ths is an optional helper script that compiles everything! =)

---------------------------------------------------------------------------------------------------
# Dependencies

- bs4:  pip install bs4
- lxml: pip install lxml
"""

# -------------------------------------------------------------------------------------------------
import subprocess

cmd0 = 'rm ../*.html'
cmd1 = 'py grid2html.py'
cmd2 = 'py miatex2html.py *.md'
CMDS = [cmd0, cmd1, cmd2]

for cmd in CMDS:
  subprocess.run(cmd, shell=True)
