#
# 2do
#
import pickle


t=12,True,3.1,'aCat'

with open('tuple.bin','wb') as fh:
        pickle.dump(t,fh)

print('done...')