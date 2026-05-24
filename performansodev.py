# 9un cevabı
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
secilen_ay = input("Hangi ayın mevsimini merak ediyorsun? ").capitalize() 
# kelimenin ilk harfini büyük yaz yoksa sanırım hata veriyor yani örnek:
# "Temmuz" , "temmuz" değil.

kis = ["Aralık", "Ocak", "Şubat"]
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
    print("Hatalı giriş")

# 29un cevabı
fiyatlar = []
eski_fiyat = float(input("Ürünün fiyatını gir: "))
fiyatlar.append(eski_fiyat)

zam_orani = 0.20
zamli_fiyat = fiyatlar[0] * 1.20
fiyatlar.append(zamli_fiyat)

print("Eski Fiyat:", fiyatlar[0])
print("Yeni Zamlı Fiyat:", fiyatlar[1])

# 49un cevabı
kelime = input("Hecelecek kelimeyi yaz: ")
cikti = "-".join(kelime)
print("Sonuç:", cikti)

# 69un cevabı
sayilar = [10, 10, 5]
toplam = 0
while len(sayilar) > 0:
    toplam += sayilar.pop()
print("Liste boşaldı, toplam:", toplam)

# 89un cevabı
import time
baslangic = int(input("Kaçtan geriye sayılsın? "))
for s in range(baslangic, 0, -1):
    print(s)
    time.sleep(0.5)
print("Bitti")




# bu gün...benim doğum günüm. 24 mayıs🧡2011
