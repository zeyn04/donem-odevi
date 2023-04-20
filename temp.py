anahtar = 1

while anahtar == 1:
    print("Uygulamamıza Hoşgeldiniz\n")
    print("1-GİRİŞ YAP\n2-ÜYE OL\n3-ŞİFREMİ UNUTTUM\n4-ÇIKIŞ YAP\n")
    kontrol = input("Yapmak istediğiniz işlemin numarasını girin : ")
    
    if kontrol == "4":
        print("çıkılıyor...")
        anahtar = 0
         
    elif kontrol == "1":
        input("kullanıcı adınızı giriniz\n")
        parola=input("Şifrenizi giriniz.\n")
        toplam_uzunluk = len(parola)
        if toplam_uzunluk > 10:
          print("parolanızı yanlış girdiniz")
        
    elif kontrol == "2":
        input("adınızı giriniz\n")
        input("doğum tarihinizi giriniz\n")
        input("e-postanızı giriniz\n")
        input("kullanıcı adınızı giriniz\n")
        parola=input("Şifrenizi giriniz.\n")
        toplam_uzunluk = len(parola)
        if toplam_uzunluk > 10:
          print("parolanızı 10 karakterden az olmalıdır")
        else:
          break
    elif kontrol == "3":
        input("e-posta adresinizi giriniz\n")
        input("e-posta adresinize yeni şifreniz yollanmıştır\n")
        print("dilerseniz giriş yapıp şifrenizi değiştirebilirsiniz\n") 
        break
    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:")
        




