import time

#Bubble sort
def bubbleSort(vector):
    start=time.time()
    lungime = len(vector)
    # Cel putin pe codul meu, daca n (sau lungimea vectorului) este mai mare de 10^5
    # dureaza extrem de mult timp sortarea
    if lungime>=10**5:
        return print("Bubble sort: sortarea va dura prea mult timp")

    # Parcurgem vectorul;
    for i in range(lungime):
        inversiune = False
        # Cat timp "bula" nu este sortata, aceasta este parcursa si sortata
        for j in range(0, lungime - i - 1):
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                inversiune = True # "bula" nu este sortata deci functia continua

        if inversiune == False: # Nu mai exista inversiuni, deci lista a fost sortata si se poate iesi din functie
            break

    stop=time.time()
    print("Bubble sort: ", stop-start, "secunde")

#===========================================================================

#Counting Sort
def countingSort(vector):
    start = time.time()
    size = len(vector)
    nmax=max(vector)
    if nmax >= size:
        return print("Counting sort: nu merge daca nmax>n") #in codul meu daca nmax>n atunci primesc eroare de index
                                                            # out of range

    output = [0] * size

    # Initializam array ul de frecventa
    fr = [0] * (nmax+1)

    # Parcurgem vectorul si actualizam frecventa in fr pentru fiecare element din vector
    for i in range(0, nmax):
        fr[vector[i]] += 1

    # Pentru ca algoritmul sa fie stabil vom aduna suma frecventei din stanga la elementul actual. Astfel numerele din
    # vectorul initial vor fi sortate in ordinea in care au fost create
    for i in range(1, 10):
        fr[i] += fr[i - 1]

    # Cautam pozitia fiecarui element din vectorul initial in vectorul de frecventa
    # si le plasam in vectorul de output
    i = size - 1
    while i >= 0:
        output[fr[vector[i]] - 1] = vector[i]
        fr[vector[i]] -= 1
        i -= 1

    # Copiem numerele sortate din output in vectorul initial
    for i in range(0, size):
        vector[i] = output[i]

    stop = time.time()
    print("Counting sort: ", stop - start, "secunde")

#============================================================================

#Quick sort cu pivotul la final (am incercat cu median of 3 dar primeam niste rezultate ciudate
                                 # si nu am avut timp sa mai schimb)

def segmentare(vector, low, high):
    i = (low - 1)  # indexul elementului mai mic
    pivot = vector[high]  # pivotul, care va fi ultimul element din segment

    for j in range(low, high):

        # Daca elemementul curent este mai mic sau egal decat pivotul
        if vector[j] <= pivot:
            # incrementam indexul elemtului mai mic
            i = i + 1
            vector[i], vector[j] = vector[j], vector[i]

    vector[i + 1], vector[high] = vector[high], vector[i + 1]
    return (i + 1)




#Functia principala in care este implementat quicksort ul

def quickSortAlg(vector, low, high):

    if len(vector) == 1:
        return vector
    if low < high:
        pi = segmentare(vector, low, high)


        quickSortAlg(vector, low, pi - 1)
        quickSortAlg(vector, pi + 1, high)

#Fiindca quickSortAlg este recursiva am mai facut o functie care va calcula timpul de sortare al acesteia

def quickSortRez(vector, low, high):
    start=time.time()
    quickSortAlg(vector, low, high)
    stop=time.time()
    print("Quick sort: ", stop - start, "secunde")

#======================================================================================================================

def mergeSortAlg(vector):
    if len(vector) > 1:

        # Cautam jumatatea vectorului
        mid = len(vector) // 2

        # Impartim vectorul initial in doua jumatati L si R
        L = vector[:mid]
        R = vector[mid:]

        # Sortam recursiv cele doua jumatati
        mergeSortAlg(L)
        mergeSortAlg(R)

        i = j = k = 0

        # Copiem numerele inapoi in vectorul initial
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                vector[k] = L[i]
                i += 1
            else:
                vector[k] = R[j]
                j += 1
            k += 1

        #Verificam daca au mai ramas elemente in L sau R
        while i < len(L):
            vector[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            vector[k] = R[j]
            j += 1
            k += 1

#La fel ca la Quick sort am definit o functie pentru a calcula timpul

def mergeSortRez(vector):
    start=time.time()
    mergeSortAlg(vector)
    stop=time.time()
    print("Merge sort: ", stop - start, "secunde")

#Sortarea nativa din Python

def nativeSort(vector):
    start=time.time()
    vector=sorted(vector)
    stop = time.time()
    print("Sortare nativa: ", stop - start, "secunde")

#Radix sort ul nu am reusit sa l implemetez. Am inteles in mare cum functioneaza dar am avut probleme la implementare