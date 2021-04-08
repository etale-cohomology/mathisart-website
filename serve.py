#!/usr/bin/env py
"""
To serve the app locally, run one of the following:
  python3.6 serve.py
  python3 serve.py
  python serve.py
  ./serve.py
  export FLASK_APP=serve.py && flask run

---------------------------------------------------------------------------------------------------
This Python script is used to run a local HTTP server, for local development.

If you add new pages (in the file `cells.grid`), then you must manually add them manually to this file,
to the `PAGE_PATHS` variable!
"""
import mathisart as m

# -----------------------------------------------------------------------------------------------------------------------------#
PAGE_PATHS = []
for path in m.dirlist():
  if not path.endswith('.html') or path=='index.html':  continue;
  PAGE_PATHS.append(path[:-5])

# -----------------------------------------------------------------------------------------------------------------------------#
from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='')

FUNCTION_TEMPLATE = '''
@app.route('/{name}')
def {name}():
  return app.send_static_file('{name}.html')
'''

def page_add(function_content):
  exect(function_content)

# -----------------------------------------------------------------------------------------------------------------------------#
@app.route('/')
def index():
  return app.send_static_file('index.html')

for page_name in PAGE_PATHS:
  exec(FUNCTION_TEMPLATE.format(name=page_name))

# -----------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
  app.run()
