def faktorPrima(x) :
    a = []
    b = []
    hasil = 0
    bil = x
    prima =True
    for i in range(2,x):
        prima = True
        for u in range(2, i) :
            if i % u == 0 :
               prima = False
        if prima :
            a.append(i)
    idx = 0
    while bil > 1 :      
        try:
            if (bil%a[idx]) == 0 : 
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])
            else :
                idx = idx + 1
        except IndexError :
            break
    print (b)
