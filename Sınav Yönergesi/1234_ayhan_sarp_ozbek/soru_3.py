# Kullanıcıdan bir tam sayı girişi alınıyor.
girilen_sayi = int(input("Bir sayı giriniz: "))

# Girilen sayının kaç basamaklı olduğunu hesaplamak için sayaç başlatılıyor.
basamak_sayisi = 0

# Girilen sayı sıfır ise, doğrudan basamak sayısı 1 olarak belirlenir çünkü '0' bir basamaklıdır.
# Bu kısım eklenmezse kullanıcının '0' girmesi durumunda sonucu '0' olarak verir.
if girilen_sayi == 0:
    basamak_sayisi = 1
else:
    # Girilen sayı sıfır değilse, sayı sıfır olana kadar 10'a bölünerek basamakları sayılır.
    while girilen_sayi != 0:
        girilen_sayi //= 10  # Sayıyı 10'a bölerek bir basamak azaltıyoruz.
        basamak_sayisi += 1  # Her bölme işlemi bir basamak azalttığı için sayaç artırılır.

# Sonuç olarak hesaplanan basamak sayısını ekrana yazdırıyoruz.
print(basamak_sayisi)
