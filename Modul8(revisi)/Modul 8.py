#nomor 1
class stack ():
    def __init__ (self):
        self.list = []
    def empty (self):
        return len(self.list) == 0
    def __len__ (self):
        return len(self.list)
    def push(self, data):
        self.list.append(data)
    def pop(self):
        assert not self.empty(), 'No file'
        return self.list.pop()

def cetak_hexa(angka):
    x = stack()

    if angka == 0:
        x.push(0)
    while angka != 0:
        sisa = angka % 16
        angka = angka//16
        x.push(sisa)
    hexa = [0,1,2,3,4,5,6,7,8,9,       'A','B', 'C', 'D', 'E', 'F']
    hasil = ''
    for i in range (len(x)):
        hasil += str(hexa[x.pop()])
    return hasil
print("-------------------------------------------------------------------------------")
#nomor 2

class stack ():
    def __init__ (self): #membuat stack kosong 
        self.item = []
    def empty (self): #mengembalikan nilai bolean yang menunjukan apakah  stack itu kosong
        return len(self) == 0
    def __len__ (self):#mengembalikan banyaknya item di stack
        return len(self.item)
    def peek(self):# mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang  paling atas
        assert not self.empty()
        return self.item[-1] 
    def pop(self):#mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stact, menambah item ke puncak stack
        self.item.append(data)
b = stack()
b.push(3)
b.push(9)
b.push(5)
b.push(1)

print (b.pop())
print (b.pop())
print (b.pop())
print("----------------------------------------------------------------------------")
class stack ():
    def __init__ (self): #membuat stack kosong 
        self.item = []
    def empty (self): #mengembalikan nilai bolean yang menunjukan apakah  stack itu kosong
        return len(self) == 0
    def __len__ (self):#mengembalikan banyaknya item di stack
        return len(self.item)
    def peek(self):# mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang  paling atas
        assert not self.empty()
        return self.item[-1] 
    def pop(self):#mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stact, menambah item ke puncak stack
        self.item.append(data)

#3

nilai = stack()
for i in range (16):
    if i % 3 == 0 :
        nilai.push(i)
st = ''
for i in range(len(nilai)):
    st = st + " " +str(nilai.pop())
    print (st)


