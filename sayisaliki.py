import random

sayiListem = list(range(1,50))

for i in range(1,5):
    print(i,".Sayı Grubu")
    j = 0 
    t = list()
    while j <= 5:
        sayiSec = random.choice(sayiListem)
        t.append(sayiSec)
        sayiListem.remove(sayiSec)
        j = j + 1
        t.sort()
    print(t)