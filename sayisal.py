import random

sayiListesi = list(range(1, 50))                   


for i in range(1, 7):                               
    print(i, ".Sayı grubu")
    j = 0                                           
    t = list()
    while j <= 3:
        sayiSec = random.choice(sayiListesi)
        t.append(sayiSec) 
        sayiListesi.remove(sayiSec)
        j = j + 1
        t.sort()           
        
    print(t)

    