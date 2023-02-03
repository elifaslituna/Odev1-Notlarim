import random

randomsayi = random.randint(1,10)
cansayisi = int(input("Can sayınız: "))
y = 0
can = cansayisi
canin = cansayisi

while can != 0 :

    y = y + 1
    x = int(input("Bir sayı giriniz: "))

    if x != randomsayi:
        can = can - 1

        if can == 0:
            print("Canınız bitti" + " " f"Doğru sayı : {randomsayi} ")
            break

    if x > randomsayi:
        print("Kalan can sayısı: " + str(can))
        print("Aşağı ininiz") 
                
    elif x < randomsayi:
        print("Kalan can sayısı: " + str(can))
        print("Yukarı çıkınız")
        
    else:
        skor = (100/cansayisi)*(canin-y+1)
        print(f"Tebrikler puanınız: {skor}")
        break