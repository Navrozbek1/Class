""" Hayotiy algoritmik masalalar """

""" 1-Masala: Transport vositalari iyerarxiyasi """

# Transport - bu asosiy (ota) klass bo'lib, barcha transport turlari uchun umumiy xususiyatlarni saqlaydi
# class Transport:
#     # __init__ metodi obyekt yaratilganda ishga tushadi va boshlang'ich qiymatlarni o'rnatadi
#     def __init__(self, model: str, yil: int) -> None:
#         self.model = model  # Transport modeli
#         self.yil = yil      # Ishlab chiqarilgan yili
        
#     # Transport haqida malumot qaytaruvchi metod
#     def malumot(self) -> str:
#         return f"Model: {self.model}, Yil: {self.yil}"

# # Avtomobil klassi Transport klassidan meros oladi (Transport xususiyatlariga ega bo'ladi)
# class Avtomobil(Transport):
#     def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
#         # super().__init__ yordamida ota klass (Transport) ning __init__ metodi chaqiriladi
#         super().__init__(model, yil)
#         self.yonilgi_turi = yonilgi_turi  # Avtomobilga xos qo'shimcha xususiyat
    
#     # Ota klassdagi malumot metodini o'zgartiramiz (override)
#     def malumot(self) -> str:
#         baza = super().malumot()  # Ota klassdagi malumotni olamiz
#         return f"{baza}, Yonilg'i: {self.yonilgi_turi}"  # Unga yangi malumot qo'shamiz

# # Avtobus klassi ham Transport klassidan meros oladi
# class Avtobus(Transport):
#     def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
#         super().__init__(model, yil)
#         self.orinlar_soni = orinlar_soni  # Avtobusga xos xususiyat
    
#     def malumot(self) -> str:
#         baza = super().malumot()
#         return f"{baza}, O'rinlar: {self.orinlar_soni}"


# # Obyektlarni yaratish va tekshirish
# a = Avtomobil("Cobalt", 2022, "benzin")
# print(a.malumot())  # Avtomobil ma'lumotlarini ekranga chiqarish

# b = Avtobus("Isuzu", 2018, 40)
# print(b.malumot())  # Avtobus ma'lumotlarini ekranga chiqarish

"""2-Masala: Kutubxona tizimi – kitob turlari"""

# class Kitob:
#     def __init__(self, nom: str, muallif: str, yil: int) -> None:
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
    
#     def taqdimot(self) -> str:
#         return f"'{self.nom}' - {self.muallif} ({self.yil})"

# class ElektronKitob(Kitob):
#     def __init__(self, nom: str, muallif: str, yil: int, fayl_hajmi_mb: int) -> None:
#         super().__init__(nom, muallif, yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
    
#     def taqdimot(self) -> str:
#         baza = super().taqdimot()
#         return f"{baza} [Elektron, {self.fayl_hajmi_mb}MB]"

# class AudioKitob(Kitob):
#     def __init__(self, nom: str, muallif: str, yil: int, davomiylik_soat: int) -> None:
#         super().__init__(nom, muallif, yil)
#         self.davomiylik_soat = davomiylik_soat
    
#     def taqdimot(self) -> str:
#         baza = super().taqdimot()
#         return f"{baza} [Audio, {self.davomiylik_soat} soat]"

# # Obyektlarni yaratish va tekshirish
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)

# print(e.taqdimot())
# print(a.taqdimot())

"""3-Masala: Xodimlar va maosh tizimi"""

# # Xodim klassi - bu ota klass
# class Xodim:
#     def __init__(self, ism: str, asosiy_maosh: int):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh

#     def oylik(self):
#         # Oddiy xodim uchun oylik shunchaki asosiy maoshning o'zi
#         return self.asosiy_maosh
    
#     def malumot(self):
#         # self.oylik() metodini chaqiramiz, shunda har bir klassning o'z oylik hisoblash usuli ishlaydi
#         return f"Ism: {self.ism}, Oylik: {self.oylik()}"

# # Oqsoch klassi - bonus oladigan xodim
# class Oqsoch(Xodim):
#     def __init__(self, ism: str, asosiy_maosh: int, bonus_foiz: int):
#         super().__init__(ism, asosiy_maosh)
#         self.bonus_foiz = bonus_foiz
    
#     def oylik(self):
#         # Asosiy maoshga bonus qo'shamiz
#         # Masalan: 20% bonus bo'lsa: maosh + (maosh * 0.20)
#         bonus = self.asosiy_maosh * (self.bonus_foiz / 100)
#         return self.asosiy_maosh + bonus

# # SoatbayXodim klassi - soatiga qarab ishlaydigan xodim
# class SoatbayXodim(Xodim):
#     def __init__(self, ism: str, soat: int, soatlik_stavka: int):
#         # Bu yerda asosiy maosh soat * stavka bo'ladi
#         hisoblangan_maosh = soat * soatlik_stavka
#         # Ota klassga hisoblangan maoshni beramiz
#         super().__init__(ism, hisoblangan_maosh)
#         self.soat = soat
#         self.soatlik_stavka = soatlik_stavka
 

# # Obyektlarni yaratish va tekshirish
# o = Oqsoch("Dilshod", 5_000_000, 20)
# s = SoatbayXodim("Aziza", soat=160, soatlik_stavka=50_000)

# print(o.malumot())
# print(s.malumot())

""" 4-Masala: Onlayn do’kon – Mahsulot turlari"""



# class Mahsulot:
#     def __init__(self, nom: str, narx: int) -> None:
#         self.nom = nom
#         self.narx = narx
    
#     def chegirmali_narx(self, foiz: int) -> int:
#         return self.narx - (self.narx * foiz / 100)

# class Elektronika(Mahsulot):
#     def __init__(self, nom: str, narx: int, kafolat_oy: int) -> None:
#         super().__init__(nom, narx)
#         self.kafolat_oy = kafolat_oy

#     def malumot(self) -> str:
#         return f"Nom: {self.nom}, Narx: {self.narx}, Kafolat: {self.kafolat_oy} oy"

# class OziqOvqat(Mahsulot):
#     def __init__(self, nom: str, narx: int, yaroqlilik_kuni: str) -> None:
#         super().__init__(nom, narx)
#         self.yaroqlilik_kuni = yaroqlilik_kuni

#     def malumot(self) -> str:
#         # Xato: O'zgaruvchilar oldiga self qo'yilmagan edi
#         return f"Nom: {self.nom}, Narx: {self.narx}, Yaroqlilik: {self.yaroqlilik_kuni}"   

# a = Elektronika("Randa", 18000, 24)
# # Xato: Yaroqlilik kuni string bo'lishi kerak edi, son emas
# b = OziqOvqat("Olma", 5000, "2024-12-31")

# # Xato: Metodlarni chaqirishda () qavslar qolib ketgan
# print(a.malumot())
# print(b.malumot())


