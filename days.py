yas = int(input("Yaşınızı daxil edin: "))

# Hesablamalar (təxmini olaraq 1 il = 365 gün götürülür)
gun = yas * 365
saat = gun * 24
deqiqe = saat * 60

print(f"Təxminən {gun} gün, {saat} saat və {deqiqe} dəqiqə yaşamısınız.")