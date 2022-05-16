#
# 2do
#
import pickle

d={'one':'aaa aaa', 'two':'bbb bbb', 'three':'ccc ccc'}

with open('dict.bin','wb') as fh:
    pickle.dump(d,fh)
print('done...')

