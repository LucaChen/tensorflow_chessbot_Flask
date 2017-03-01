import os
from os import path
filename = 'index.html'
if os.path.exists(filename):
  os.remove(filename)
