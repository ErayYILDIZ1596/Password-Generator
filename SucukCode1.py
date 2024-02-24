import random
sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
kucukharfler = "abcdefghijklmnopqrstuvwxyz"
buyukharfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "1234567890"
simgeler = "+-/*!&$#?=@"
uzunluk = int(input("Şifreniz ne kadar uzun olsun?:"))

sonuc = ""
for i in range(uzunluk):
    sonuc += random.choice(sifre)
print("Şifreniz:", sonuc)