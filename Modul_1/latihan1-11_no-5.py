from math import sqrt as sq
def apakahPrima(x):
    x = int(x)
    assert x >= 0
    primaKecil = [2,3,5,7,11]
    bukanPriKecil = [0,1,4,6,8,9,10]
    if x in primaKecil:
        return True
    elif x in bukanPriKecil:
        return False
    else:
        hasil=[]
        for i in range(2,int(sq(x))+1):
            if i in primaKecil:
                hasil.append(True)
                print (True)
            elif i in bukanPriKecil:
                hasil.append(False)
                print (False)
        #return hasil

apakahPrima(25)
