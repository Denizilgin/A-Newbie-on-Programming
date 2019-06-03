turkuaz = "\033[96m"
sari = "\033[93m"
kirmizi = "\033[91m"
boy = int(input(turkuaz+"Lütfen boyunuzu araya nokta koymayarak giriniz."))
kilo = int(input("Şimdide kilonuzu giriniz."))
boykare = boy/100
boykare = boykare*boykare
print(sari+"Vücut kitle indeksiniz"+kirmizi,(kilo/boykare))
if (kilo/boykare<18.5):
    print("Vücut kitle indeksine göre"+sari+" zayıfsın")
elif(kilo/boykare<25):
    print("Vücut kitle indeksine göre" + sari + " idealsin")
elif(kilo/boykare<30):
    print("Vücut kitle indeksine göre" + sari + " kilolusun")
else:
    print("Vücut kitle indeksine göre" + sari + " obezsin")


