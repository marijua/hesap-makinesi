sayi1 = input("Birinci Sayı : ")
sayi2 = input("İkinci Sayı : ")

print("""
Hesap Makinesi İşte Ne bekliyorsun

[1]Toplama
[2]Çıkarma
[3]Çarpma
[4]Bölme
[5]Üslerini Alma
	""")

x = input("Seçiniz : ")

sayi1 = float(sayi1)
sayi2 = float(sayi2)

if x == "1":
	print("İşleminin Sonucu : ",sayi1+sayi2)
if x == "2":
	print("İşleminin Sonucu : ",sayi1-sayi2)
if x == "3":
	print("İşleminin Sonucu : ",sayi1*sayi2)
if x == "5":
    print("İşleminin Sonucu : ",sayi1**sayi2)
else:
	print("İşleminin Sonucu : ",sayi1/sayi2)

print("Amatörce Birşey İşte Cart Curt")