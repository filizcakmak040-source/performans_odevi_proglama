# proglama performans odevi
# 9un cevabi
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
# ilk harfi büyük gir yoksa hata veriyor yani örnek temmuz değil Temmuz yazman gerek.

secilen_ay = input("Hangi ayın mevsimini merak ediyon? ")

indis = aylar.index(secilen_ay)

kis = aylar[0:2]
ilkbahar = aylar[2:5]
yaz = aylar[5:8]
sonbahar = aylar[8:11]

if secilen_ay in kis:
    print("Mevsim: Kış")
elif secilen_ay in ilkbahar:
    print("Mevsim: İlkbahar")
elif secilen_ay in yaz:
    print("Mevsim: Yaz")
elif secilen_ay in sonbahar:
    print("Mevsim: Sonbahar")
else:
    print("Hatalı giriş!")




# 29un cevabi
fiyatlar = []
eski_fiyat = float(input("Ürünün fiyatını giriniz:"))
fiyatlar.append(eski_fiyat)

zam_orani = 0.20
zamli_fiyat = fiyatlar[0] + (fiyatlar[0] * zam_orani)

fiyatlar.append(zamli_fiyat)

print("Eski Fiyat:", fiyatlar[0])
print("Yeni Zamlı Fiyat:", fiyatlar[1])



# 49un cevabi
kelime = input("Hecelecek kelime: ")
harf_listesi = list(kelime)

for i in range(1, len(harf_listesi), 1):
    harf_listesi.insert(i, "-")

cikti = "".join(harf_listesi)
print("Sonuç:", cikti)



# 69un cevabi
sayilar = [10, 10, 5]
toplam = 0

while len(sayilar) > 0:
    son_eleman = sayilar.pop()
    toplam = toplam + son_eleman

print("Liste boşaldı, toplam da şu çıktı:", toplam)



# 89un cevabi
import time

baslangic = int(input("Kaçtan geriye? "))
liste = []


for x in range(1, baslangic + 1):
    liste.append(x)

liste.reverse()

for s in liste:
    print(s)
    time.sleep(0.5)
print("Bitti!")
