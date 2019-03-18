def apakahKabisat(t):
    b = int(t)
    if(t % 4) == 0:
        if(t % 100) == 0:
            if(t % 400) == 0:
                print("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")
    
