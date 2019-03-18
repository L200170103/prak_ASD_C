class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.checkSizeConsis()
        self.checkTypeConsis()

    def checkSizeConsis(self):
        for allcol in self.matrix:
            if len(allcol) != self.col:
                raise ValueError("Jumlah kolom tidak sama/konsisten")

    def checkTypeConsis(self):
        typedata = type(self.matrix[0][0])
        for x in self.matrix:
            for y in x:
                if type(y) != typedata:
                    raise ValueError("Tipe data di dalam matrix tidak sama/konsisten")

    def getSize(self):
        return (self.row, self.col)

    def transposeX(self):
        m = len(self.matrix)
        n = len(self.matrix[1])
        d = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                d[j][i] = self.matrix[i][j]
        return d

    def addMatrix(self, objMatrix):
        if objMatrix.row != self.row and objMatrix.col != self.col:
            return "Size/ukuran matrix tidak konsisten"
        final = []
        for [x, y] in zip(self.matrix, objMatrix.matrix):
            colTemp = []
            for a, b in zip(x, y):
                colTemp.append(a + b)
                if len(colTemp) == self.col:
                    final.append(colTemp)
                    colTemp = []
        return final

    def multiplyMatrix(self, objMatrix):
        if self.row != objMatrix.col and self.col != objMatrix.row:
            return "Syarat perkalian matrix tidak memenuhi"
        newObjMatrix = objMatrix.transposeX()
        final = []
        for x, y in zip(self.matrix, newObjMatrix):
            colTemp = []
            for a, b in zip(x, y):
                colTemp.append(a * b)
                if len(colTemp) == self.col:
                    final.append(colTemp)
                    colTemp = []
        return final

    def determinan2x2(self):
        if self.row != 2 and self.col != 2:
            return "Hanya matrix 2x2"
        det = (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] * self.matrix[1][0])
        return det


a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8]])
b = Matrix([[11, 12, 13, 14], [15, 16, 17, 18], [5, 6, 7, 8]])
print(a.getSize())
print(a.addMatrix(b))

c = Matrix([[1, 2, 3], [4, 5, 6]])
d = Matrix([[1, 2], [3, 4], [5, 6]])
print(c.multiplyMatrix(d))
c.multiplyMatrix(d)

e = Matrix([[1, 2], [3, 4]])
print(e.determinan2x2())

print("======================================================================================")


def buatNol(m, n="izzy"):
    if n == "izzy":
        n = m
    return [[0 for y in range(n)] for x in range(m)]


def buatIdentitas(i):
    return [[1 if y == x else 0 for y in range(i)] for x in range(i)]


print(buatNol(2))
print(buatIdentitas(4))

print("=======================================================================================")


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def MakeNode(list):
    a = Node(list[0])
    if len(list) > 1:
        b = a
        for i in range(1, len(list)):
            b.next = Node(list[i])
            b = b.next
    return a


def kunjungi(head):
    curNode = head
    while curNode != None:
        print(curNode.data)
        curNode = curNode.next


def cari(head, yang_dicari):
    temp = head
    while temp != None:
        if temp.data == yang_dicari:
            return temp
        temp = temp.next
    return Node(None)


def tambahDepan(head):
    temp = Node("tambah depan", head)
    return temp


def tambahAkhir(head):
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = Node("tambah akhir")
    return head


def tambah(head, posisi):
    """ Menambahkan simpul sebelum posisi """
    temp = head
    while temp != None:
        if temp.next.data == posisi:
            temp_belakang = temp.next
            temp.next = Node("tambah tengah", temp_belakang)
            return head
        temp = temp.next
    return None


def hapus(head, posisi):
    temp = head
    while temp != None:
        if temp.next.data == posisi:
            temp_belakang = temp.next.next
            temp.next = temp_belakang
            return head
        temp = temp.next
    return None


a = MakeNode(["er", "ge", "beh", "GG", "WP"])

print(a.data)
c = cari(a, "beh")
print(c.next.data)

print()
kunjungi(a)

print()
a = tambahDepan(a)
kunjungi(a)

print()
a = tambahAkhir(a)
kunjungi(a)

print()
a = tambah(a, "beh")
kunjungi(a)

print()
a = hapus(a, "beh")
kunjungi(a)

print("==========================================================================================")


class DNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def massDNodeCreator(list):
    a = DNode(list[0])
    p = a
    for i in list[1:]:
        p.next = DNode(i)
        p.next.prev = p
        p = p.next
    return a


def tambahSimpulAwal(head, data):
    data = DNode(data)
    data.next = head
    data.next.prev = data
    return data


def tambahSimpulAkhir(head, data):
    data = DNode(data)
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = data
    return head


list = ["c", "m", "y", "k"]
a = massDNodeCreator(list)
print(a.next.next.next.prev.prev.data)

a = tambahSimpulAwal(a, "awal")
print(a.next.prev.data)

a = tambahSimpulAkhir(a, "akhir")
print(a.next.next.next.next.next.data)