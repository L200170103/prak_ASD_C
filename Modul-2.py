#################################NO.1##################################
class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
        
#################################NO.1A#################################
    def apakahTerkandung(self, kata):
        self.kata = kata
        if self.kata in self.teks:
            return True
        else:
            return False
        
#################################NO.1B#################################
    def hitungKonsonan(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() not in vowel :
                jml+=1
        return jml
    
#################################NO.1C#################################
    def hitungVokal(self):
        k = self.teks
        vowel = " AIUEOaiueo"	
        jml = 0	
        for a in k:
            if a.lower() in vowel :
                jml+=1
        return jml
    
#############################Kode Eksekusi#############################
## p9 = Pesan('Indonesia adalah negeri yang indah')
## p9.apakahTerkandung('ege')
## p9.apakahTerkandung('eka')
## p10 = Pesan('Surakarta')
## p10.hitungKonsonan()
## p10.hitungVokal()

#################################NO.2##################################
class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulannya."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
        
#################################NO.2A#################################
    def ambilKotaTinggal(self):
        print (self.kotaTinggal)
        
#################################NO.2B#################################
    def perbaruiKotaTinggal(self, baru):
        self.kotaTinggal = baru
        
#################################NO.2C#################################
    def tambahUangSaku(self, uang):
        self.uangsaku = self.uangsaku + uang
        
#################################NO.3##################################
##a = input("Masukkan Nama Anda : ")
##b = input("Masukkan NIM Anda : ")
##c = input("Masukkan Kota Tinggal Anda : ")
##d = input("Masukkan Uang Saku Anda : ")
    

#############################Kode Eksekusi#############################
## m1 = Mahasiswa(a,b,c,d)
## m1.ambilNama()
## m1.ambilNIM()
## m1.ambilKotaTinggal()
## m1.ambilUangSaku()
        
#################################NO.4##################################
    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)

#################################NO.5##################################
    def hapusKuliah(self, item):
        self.listKuliah.remove(item)

#################################NO.6##################################
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,nama,no_induk,kelas,alamat):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.no = no_induk
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"No Induk : "+str(self.no)+'\n'+"Tinggal di : "+self.alamat+'\n'+"Kelas : "+str(self.kelas)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)

#################################NO.7##################################
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('Python is cool.')

##Dari class Manusia:
##    1. nama
##    2. keadaan
##    3. ucapkanSalam
##    4. makan
##    5. olahraga
##    6. mengalikanDenganDua
##
##Dari class Mahasiswa:
##    1. NIM
##    2. kotaTinggal
##    3. uangsaku
##    4. ambilNama
##    5. ambilNIM
##    6. ambilUangSaku
##    7. makan
##    8. ambilKotaTinggal
##    9. perbaruiKotaTinggal
##    10. tambahUangSaku
##    11. listKuliah
##    12. ambilKuliah
##    13. hapusKuliah
##
##Dari class MhsTIF:
##    1. katakanpy
    
#############################Kode Eksekusi#############################     
m9 = Mahasiswa("Ati","L200170103","Palembang",54000)
s1 = SiswaSMA("Ati",17001,54,"Palembang")

## m9.ambilKotaTinggal()
## m9.perbaruiKotaTinggal('Solo')
## m9.ambilKotaTinggal()
## m9.ambilUangSaku()
## m9.tambahUangSaku(45000)
## m9.ambilUangSaku()





    
