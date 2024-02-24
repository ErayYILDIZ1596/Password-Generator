import random
sifre = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
kucukharfler = "abcdefghijklmnopqrstuvwxyz" #Not used
buyukharfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Not used
sayilar = "1234567890" #Not used
simgeler = "+-/*!&$#?=@" #Not used
uzunluk = int(input("Şifreniz ne kadar uzun olsun?:"))

sonuc = ""
for i in range(uzunluk):
    sonuc += random.choice(sifre)
print("Şifreniz:", sonuc)
