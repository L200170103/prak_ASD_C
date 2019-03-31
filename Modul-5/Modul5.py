#nomer1
class Mhs (object):
    def __init__ (self,nim):
        
        self.nim = nim
        
    def __str__(self):
        a = 'nim :' + str(self.nim)
        return a
    def getnim (self):
        return self.nim

          

c0 = Mhs ( 10)
c1 = Mhs( 51)
c2 = Mhs( 2)
c3 = Mhs( 18)
c4 = Mhs(4)
c6 = Mhs(13)
c7 = Mhs( 5)
c8 = Mhs(23)
c9 = Mhs( 64)
c10 = Mhs( 29)

Daftar = [c0,c1,c2,c3,c4,c6,c7,c8,c9,c10]

def swap (A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim :
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)


insertionSort(Daftar)
cetakDaftar(Daftar)

#nomor 2
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]  :
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai

A = [1, 2, 3, 5, 6, 7, 11, 16, 17, 21, 23, 29, 31]
B =  [ 8,9, 4, 10, 12,  13, 15, 21, 25,  30, 31, 14]
C = []

C.extend(A)
C.extend(B)
insertionSort (C)

print (' Nilai C :', C)

#nomor 3
from time import time as detak
from random import shuffle as kocok

def swap (A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil (A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range (dariSini+1, sampaiSini):
        if A[i] < A [posisiYangTerkecil]:
            posisiYangTerkecil = i
            return posisiYangTerkecil
def bubbleSort(A):
    n = len (A)
    for i in range (n-1):
        for j in range (n-i-1):
            if A[j] > A [j+1]:
                swap(A,j,j+1)

def selectionSort (A):
    n = len(A)
    for i in range (n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A,i, indexKecil
                 )
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]  :
            A[pos] = A[pos -1]
            pos -= 1
            A[pos] = nilai
            
k = range (1,6001)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak() ; bubbleSort(u_bub) ; ak = detak(); print "Bubble : %g detik" %(ak-aw)
aw = detak() ; selectionSort(u_sel) ; ak = detak(); print "Selection : %g detik" %(ak-aw)
aw = detak() ; insertionSort(u_ins) ; ak = detak(); print "insertion : %g detik" %(ak-aw)

            




        
