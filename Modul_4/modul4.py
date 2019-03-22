class Mhs (object):
    def __init__ (self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.KotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        a = self.nama + ', NIM ' + str(self.NIM)\
            + '. Tinggal di '+ self.kotatinggal\
            + '. Uang saku Rp '+ str(self.uangsaku)\
            +' tiap bulannya.'
        return a

    def ambilnama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambiluangsaku(self):
        return self.uangsaku

c0 = Mhs ('Ika', 10, 'sukoharjo' ,240000)
c1 = Mhs('Budi', 51, 'sragen', 230000)
c2 = Mhs('Ahmad', 2, 'surakarta',250000)
c3 = Mhs('Chandra', 18, 'surakarta',245000)
c4 = Mhs('eka', 4, 'boyolali',240000)
c5 = Mhs('fandi', 31, 'sragen',240000)
c6 = Mhs('deni', 13, 'klaten',245000)
c7 = Mhs('galuh', 5, 'wonogiri',245000)
c8 = Mhs('janto', 23, 'klaten',245000)
c9 = Mhs('hasan', 64, 'karanganyar',270000)
c10 = Mhs('khalid', 29, 'purwokerto',265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

#No.1 Fungsi Pencarian 
def Cari (Target):
    x =[]
    for i in Daftar:
        if i.KotaTinggal == Target:
            hasil = Daftar.index(i)
            x.append(hasil)
    return x

# no. 2 fungsi menemukan uangSaku terkecil 
def uangsakuTerkecil(Daftar):
    n = len(Daftar)
    terkecil = Daftar[0]
    for i in range (1,n):
        if Daftar[i].uangsaku < terkecil.uangsaku:
            terkecil = Daftar [i]

    return terkecil.uangsaku
#No.3 fungsu menemukan uangsaku terkecil menempilkan object mahasiswa
def uangSakuTerkecil(Daftar):
    n = len(Daftar)
    terkecil = Daftar[0]
    for i in range (1,n):
        if Daftar[i].uangsaku < terkecil.uangsaku:
            terkecil = Daftar [i]

    return terkecil.nama

#No.4fungsi mengebalikan semua objek  yang uang sakunya kurang dari 250000.
def Kurang (Daftar):
    mhs = []
    for b in Daftar:
        if b.uangsaku < 250000:
            mhs.append(b.nama)
    return mhs

#No.5 Mencari suatu item di sebuah liked List
class node :
    def __init__(self,data):
        self.data = data
        self.next = None

    def addnext (self,nextnode):
        self.next = nextnode

    def caridata(self,Target):
        x = self
        if x.data == Target:
            return True
        while x.next != None:
            if x.data == Target:
                return True
                break
            x = x.next
        return False

#No.6 Binary Search mengembalikan index lokasi elemen yang ditemukan
def binse (kumpulan, Target):
    low =0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (high + low) // 2
        if kumpulan [mid] == Target:
            return kumpulan.index(Target)
        elif Target < kumpulan [mid]:
            high = mid - 1
        else :
            low = mid + 1
    return False

#No.7 Binary Search mengembalikan semua index lokasi elemen yang ditemukan
def bins(kumpulan, Target):
    indexList = []
    kumpulan = sorted(kumpulan)
    print " Data Diurutkan :" , kumpulan
    low = 0
    high = len (kumpulan) -1
    while low <= high :
        mid = (high + low) //2
        if kumpulan[mid] == Target:
            index = kumpulan.index (kumpulan[mid])
            indexList.append(index)
            i = 1
            while i < len(kumpulan):
                try:
                    if kumpulan[mid+i] == Target :
                        indexList.append(index+i)
                except IndexError:
                    pass
                i += 1

            return indexList
        elif Target < kumpulan [mid]:
            high = mid - 1
        else :
            low = mid + 1
    return False


#No.8
import random
def tebakAngka(maks):
    num = []
    for a in range (maks):
        num.append (a)
    Angka = random.sample (num,1)
    Angka = Angka[0]
    tebakan = 7 if maks <= 100 else 10
    while tebakan != 0:
        print ("Kesempatan Anda %d Kali" %(tebakan))
        tebak = input ("Masukan tebakannya :")
        if tebak == 0:
            return
        elif tebak == Angka :
            print ("Yaa. Anda sangat benar, Angkanya: %d" % (Angka))
            return True
        else:
            if tebak < Angka :
                print(" Terlalu kecil. Mari Coba Lagi")
            else :
                print ("Terlalu besar. Mari coba lagi")
            tebakan -= 1
    print ("Yahh, Kesempatan anda Sudah habis. Angkanya: %d" %(angka))
                    
        
    
