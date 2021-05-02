import glob
import json
import calendar
from string import Template


substituteData = {
  'body': 'testbody'
}

with open('README.md.tpl', 'r') as f:
  src = Template(f.read())
  result = src.substitute(substituteData)
  with open('README.md', 'w') as readme:
    readme.write(result)
