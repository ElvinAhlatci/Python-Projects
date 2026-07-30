gorevler = []

while True:
    print("1- Görev Ekle")
    print("2- Görevleri Göster")
    print("3- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        gorev = input("Görev: ")
        gorevler.append(gorev)

    elif secim == "2":
        for gorev in gorevler:
            print(gorev)

    elif secim == "3":
        break

    else:
        print("Hatalı seçim!")
