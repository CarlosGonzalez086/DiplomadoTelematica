#
# read binary file (dictionary)
# and print it
#

import pickle
from this import d

with open('dict.bin','rb') as fh:
    d=pickle.load(fh)

print(type(d))
print(d)
print('done..')
