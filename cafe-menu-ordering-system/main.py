print("=== KAFE MENÜ VE SİPARİŞ SİSTEMİ ===")

toplam = 0

while True:
    print("\n------ MENÜ ------")
    print("1 - Kahve (80 TL)")
    print("2 - Çay (30 TL)")
    print("3 - Tost (90 TL)")
    print("4 - Sandviç (120 TL)")
    print("0 - Siparişi Bitir")

    secim = input("Ürün seçin: ")

    if secim == "0":
        break

    adet = int(input("Kaç adet?: "))

    if secim == "1":
        fiyat = 80
        urun = "Kahve"
    elif secim == "2":
        fiyat = 30
        urun = "Çay"
    elif secim == "3":
        fiyat = 90
        urun = "Tost"
    elif secim == "4":
        fiyat = 120
        urun = "Sandviç"
    else:
        print("Geçersiz seçim!")
        continue

    tutar = fiyat * adet
    toplam += tutar

    print(f"{adet} adet {urun} eklendi. Tutar: {tutar} TL")

print("\n========================")
print("Toplam Ödenecek Tutar:", toplam, "TL")
print("Afiyet olsun!")
