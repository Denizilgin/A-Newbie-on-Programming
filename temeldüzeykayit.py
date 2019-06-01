# ÖDEV #
yesil = "\033[92m"
kalin = "\033[1m"
kirmizi = "\033[91m"
altcizgi = "\033[4m"
normal = "\033[0m"
turkuaz ="\033[96m"
print(kirmizi+"*"*32)
print(kirmizi+"*"*5+yesil+kalin+"X Sitesine Hoşgeldiniz"+kirmizi+"*"*5)
print(kirmizi+"*"*32)
yas = int(input(altcizgi+"Lütfen yaşınızı giriniz."))
if (yas < 15):
 print(normal+"Bu siteyi kullanabilmek için 15 yaşından büyük olmalısın" , (15-yas) , "yıl sonra tekrar gel")
elif (yas >= 15):
      nick = input(turkuaz+"Lütfen kendinize bir kullanıcı adı belirleyin.")
      sifre = input(turkuaz+"Kendinize bir şifre belirleyin.")
      giris = int(input("Hesabınız oluşturuldu. Giriş yapmak için 1'e tıklayın"))
      if giris == 1:
          nickgiris = input("Kullanıcı adınız")
          if nickgiris != nick:
              print(kirmizi+"Kullanıcı adınız hatalı")
          elif nickgiris == nick:
              sifregiris = input("Şifrenizi girin.")
              if sifre != sifregiris:
                  print(kirmizi+"Şifre hatalı.")
              elif sifregiris == sifre:
                  print(yesil+"Başarıyla giriş yaptınız! Hoşgeldiniz.")
