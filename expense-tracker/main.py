gelirler = []
giderler = []

while True:
    print("\n=== GELİR - GİDER HESAPLAYICI ===")
    print("1 - Gelir Ekle")
    print("2 - Gider Ekle")
    print("3 - Durumu Göster")
    print("4 - Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        gelir = float(input("Gelir miktarını girin: "))
        gelirler.append(gelir)
        print("Gelir eklendi.")

    elif secim == "2":
        gider = float(input("Gider miktarını girin: "))
        giderler.append(gider)
        print("Gider eklendi.")

    elif secim == "3":
        toplam_gelir = sum(gelirler)
        toplam_gider = sum(giderler)
        kalan = toplam_gelir - toplam_gider

        print("\n----- Mali Durum -----")
        print("Toplam Gelir:", toplam_gelir, "TL")
        print("Toplam Gider:", toplam_gider, "TL")
        print("Kalan Para:", kalan, "TL")

    elif secim == "4":
        print("Program kapatıldı.")

