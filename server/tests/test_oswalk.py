
import os

i = 0
for root, dirs, name in os.walk('bootstrap-3.3.4'):
    print i
    print root,dirs,name
    i += 1

