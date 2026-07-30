print("=== HESAP MAKİNESİ ===")

ilk_sayi = int(input("İlk sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")
ikinci_sayi = int(input("İkinci sayıyı girin: "))

if islem == "+":
    print("Sonuç:", ilk_sayi + ikinci_sayi)

elif islem == "-":
    print("Sonuç:", ilk_sayi - ikinci_sayi)

elif islem == "*":
    print("Sonuç:", ilk_sayi * ikinci_sayi)

elif islem == "/":
    if ikinci_sayi != 0:
        print("Sonuç:", ilk_sayi / ikinci_sayi)
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")

else:
    print("Hatalı işlem seçtiniz.")
