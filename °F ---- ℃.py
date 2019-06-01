import time

print("-" * 30)
print("1 -Fahrenheit to celsius")
print("2 - Celsius to fahrenheit")
print("-" * 30)

seç = int(input("1/2"))
derece = int(input("derece giriniz"))
if seç == 1:
    print("°F'den ℃'ye çeviriliyor.")
    derece = (derece-32)/1.8
    print("Hesaplanıyor.")
    time.sleep(1)
    print("Hesaplanıyor..")
    time.sleep(1)
    print("Hesaplanıyor...")
    print("Dönüşüm tamamlandı." , derece , "℃")
elif seç == 2:
    print("℃'den °F'ye çeviriliyor.")
    derece = derece * 1.8 + 32
    print("Hesaplanıyor.")
    time.sleep(1)
    print("Hesaplanıyor..")
    time.sleep(1)
    print("Hesaplanıyor...")
    print("Dönüşüm tamamlandı." , derece , "°F")