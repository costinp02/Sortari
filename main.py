import random
import time
import copy

from sortari import bubbleSort,quickSortRez, countingSort,mergeSortRez,nativeSort


f=open("date.in","r")
nr_teste=f.readline()
print("Numar de teste:",nr_teste)

for linie in f.readlines():
    n,nmax = linie.split()
    vector=[random.randrange(0,int(nmax)) for i in range(int(n))]
    print("\nn=",n,"\nnmax=",nmax)
    start = time.time()
    bubbleSort(copy.deepcopy(vector))
    countingSort(copy.deepcopy(vector))
    quickSortRez(copy.deepcopy(vector),0,int(n)-1)
    mergeSortRez(copy.deepcopy(vector))
    nativeSort(copy.deepcopy(vector))
    stop = time.time()
    t = stop - start

f.close()