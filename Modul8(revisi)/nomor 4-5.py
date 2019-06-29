#1 queue

class Queue(object) :
    
    def __init__(self):
        self.qlist = []
        
    def __len__(self) :
        return len(self.qlist)
    
    def is_Empty(self) :
        return len(self) == 0
    
    def enqueue(self, data) :
        self.qlist.append(data)
        
    def dequeue(self) :
        assert not self.is_Empty()
        return self.qlist.pop(0)
    
    def getFrontMost(self) :
        assert not self.is_Empty()
        return self.qlist[0]
    
    def getRearMost(self) :
        assert not self.is_Empty()
        return self.qlist[-1]

a = Queue ()
a.enqueue(18)
a.enqueue(15)
a.enqueue(25)
a.enqueue(14)

print (a.dequeue())
print (a.dequeue())

print (a.getFrontMost())
print (a.getRearMost())

print ("-------------------------------------------------------------------------------")
        
#5 priority
class PriorityQueue(object) :
    
    def __init__(self):
        self.qlist = []
        
    def __len__(self) :
        return len(self.qlist)
    
    def is_Empty(self) :
        return len(self) == 0
    
    def enqueue(self, data, priority) :
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
        
    def dequeue(self) :
        A = []
        for i in self.qlist:
            A.append(i)
        b = 0
        for i in range(1, len(self.qlist)) :
            if A[i].priority < A[b].priority :
                b = i
        hasil = self.qlist.pop(b)
        return hasil.item
    
class _PriorityQEntry() :
    def __init__ (self, data, priority) :
        self.item = data
        self.priority = priority
    
S = PriorityQueue()
S.enqueue("Santi",2)
S.enqueue("tia",4)
S.enqueue("Ati",0)
S.enqueue("Tio",2)
S.enqueue("hasna",5)

print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())
print (S.dequeue())

