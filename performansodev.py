# 9un cevabı
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
secilen_ay = input("Hangi ayın mevsimini merak ediyon? ").capitalize() # Küçük girse de düzeltir

# Mevsimleri doğru aralıklarla tanımlayalım
kis = ["Aralık", "Ocak", "Şubat"]
ilkbahar = aylar[2:5] # Mart, Nisan, Mayıs
yaz = aylar[5:8]      # Haziran, Temmuz, Ağustos
sonbahar = aylar[8:11] # Eylül, Ekim, Kasım

if secilen_ay in kis:
    print("Mevsim: Kış")
elif secilen_ay in ilkbahar:
    print("Mevsim: İlkbahar")
elif secilen_ay in yaz:
    print("Mevsim: Yaz")
elif secilen_ay in sonbahar:
    print("Mevsim: Sonbahar")
else:
    print("Hatalı giriş yaptın kanka!")

# 29un cevabı
fiyatlar = []
eski_fiyat = float(input("Ürünün fiyatını gir: "))
fiyatlar.append(eski_fiyat)

zam_orani = 0.20
zamli_fiyat = fiyatlar[0] * 1.20 # %20 zam eklenmiş hali
fiyatlar.append(zamli_fiyat)

print("Eski Fiyat:", fiyatlar[0])
print("Yeni Zamlı Fiyat:", fiyatlar[1])

# 49un cevabı
kelime = input("Hecelecek kelimeyi yaz: ")
cikti = "-".join(kelime) # En garantisi ve kısa yolu budur
print("Sonuç:", cikti)

# 69un cevabı
sayilar = [10, 10, 5]
toplam = 0
while len(sayilar) > 0:
    toplam += sayilar.pop()
print("Liste boşaldı, toplam:", toplam)

# 89un cevabı
import time
baslangic = int(input("Kaçtan geriye sayalım? "))
for s in range(baslangic, 0, -1): # Listeye gerek kalmadan direkt geri sayar
    print(s)
    time.sleep(0.5)
print("Bitti!")
