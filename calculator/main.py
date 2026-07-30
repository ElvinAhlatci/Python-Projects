print("=== HESAP MAKİNESİ ===")

ilk_sayi = int(input("İlk sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")
ikinci_sayi = int(input("İkinci sayıyı girin: "))

if islem == "+":
    print("\nSonuç:", ilk_sayi + ikinci_sayi)

elif islem == "-":
    print("\nSonuç:", ilk_sayi - ikinci_sayi)

elif islem == "*":
    print("\nSonuç:", ilk_sayi * ikinci_sayi)

elif islem == "/":
    if ikinci_sayi == 0:
        print("\nHata: Bir sayı sıfıra bölünemez.")
    else:
        print("\nSonuç:", ilk_sayi / ikinci_sayi)

else:
    print("\nHatalı işlem seçtiniz.")
