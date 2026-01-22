""" Algoritmik masalalar """


"""Task 1: Talabalar Ro’yxati"""


# class Talaba:
#     def __init__(self, nomi, yosh, kurs):
#         self.nomi = nomi
#         self.yosh = yosh
#         self.kurs = kurs
#
# ali = Talaba("Ali", "20", "1")
# bek = Talaba("Bek", "20", "2")
# otash = Talaba("Otash", "20", "3")
# bexruz = Talaba("Bexruz", "20", "4")
# oygul = Talaba("Oygul", "20", "5")
#
# print("=== TALABALAR RO'YXATI ===")
# print(f"{ali.nomi} - {ali.yosh} yosh, {ali.kurs}-kurs.")
# print(f"{bek.nomi} - {bek.yosh} yosh, {bek.kurs}-kurs.")
# print(f"{otash.nomi} - {otash.yosh} yosh, {otash.kurs}-kurs.")
# print(f"{bexruz.nomi} - {bexruz.yosh} yosh, {bexruz.kurs}-kurs.")
# print(f"{oygul.nomi} - {oygul.yosh} yosh, {oygul.kurs}-kurs.")


"""Task 2: Kitoblar Kutubxonasi"""


# class Kitob:
#     def __init__(self, nomi, muallifi, narxi):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narxi = narxi
#
# pd = Kitob("Python dasturlash", "Python", "50000") # pd = 'Python dasturlash'
# a = Kitob("Algoritmlar", "Odam", "75000") # a = 'Algoritmlar'
# ms = Kitob("Ma'lumotlar strukturalari", "Katta odam", "50000") # ms = 'Ma'lumotlar strukturalari'
# wd = Kitob("Web dasturlash", "Hasan", "80000") # wd = "Web dasturlash"
# m = Kitob("Ma'shuniyat", "Hech kim", "45000") # m = 'Hasan'
#
# print("=== KITOBLAR RO'YXATI ===\n")
# print(f"{pd.nomi} - {pd.narxi} so'm")
# print(f"{a.nomi} - {a.narxi} so'm")
# print(f"{ms.nomi} - {ms.narxi} so'm")
# print(f"{wd.nomi} - {wd.narxi} so'm")
# print(f"{m.nomi} - {m.narxi} so'm\n")
#
# for x in [pd, a, ms, wd]:
#     eng_katta = 0
#     if int(x.narxi) > eng_katta:
#         eng_katta = x.narxi
#
# print("=== ENG QIMMAT KITOB ===\n")
# print(f"Kitob nomi: {x.nomi}")
# print(f"Kitob narxi: {x.muallifi}")
# print(f"Kitob narxi: {x.narxi}")


"""Task 3: Telefonlar Ro’yxati"""


# class Telefon:
#     def __init__(self, mobile, rangi, xotrasi):
#         self.mobile = mobile
#         self.xotrasi = xotrasi
#         self.rangi = rangi
#
#
# iphone = Telefon("IPhone", "Qora", "128")
# samsunge = Telefon("Samsung S23", "Oq", "256")
# xiaomi = Telefon("Xiaomi 13", "Ko'k", "128")
# huawi = Telefon("Xiaomi 13", "Kumush", "512")
# oneplus = Telefon("OnePlus 11", "Yashil", "256")
#
# print("=== TELEFONLAR RO'YXATI ===")
# print(f"{iphone.mobile} ({iphone.rangi}):  {iphone.xotrasi} GB")
# print(f"{samsunge.mobile} ({samsunge.rangi}):  {samsunge.xotrasi} GB")
# print(f"{xiaomi.mobile} ({xiaomi.rangi}):  {xiaomi.xotrasi} GB")
# print(f"{huawi.mobile} ({huawi.rangi}):  {huawi.xotrasi} GB")
# print(f"{oneplus.mobile} ({oneplus.rangi}):  {oneplus.xotrasi} GB\n")
#
# eng_katta = 0
# for x in [iphone, samsunge, xiaomi, huawi, oneplus]:
#     if x != 0:
#         eng_katta += int(x.xotrasi)
# print(f"Jami xotira: {eng_katta} GB")


"""Task 4: Mevalar Do’koni"""


# class Meva:
#     def __init__(self, nomi, vazni, narxi):
#         self.nomi = nomi
#         self.vazni = vazni
#         self.narxi = narxi
#
# olma = Meva("Olma", "1", "15000")
# banan = Meva("Banan", "1.5", "20000")
# uzum = Meva("Uzum", "0.5", "12000")
# anor = Meva("Anor", "2", "30000")
# nok = Meva("Nok", "1", "10000")
#
# print("=== MEVALAR RO'YXATI ===")
# print(f"{olma.nomi} - {olma.vazni} kg, {olma.narxi} so'm ")
# print(f"{banan.nomi} - {banan.vazni} kg, {banan.narxi} so'm ")
# print(f"{uzum.nomi} - {uzum.vazni} kg, {uzum.narxi} so'm ")
# print(f"{anor.nomi} - {anor.vazni} kg, {anor.narxi} so'm ")
# print(f"{nok.nomi} - {nok.vazni} kg, {nok.narxi} so'm \n")
#
# kichik = 0
# for x in [olma, banan, uzum, anor, nok]:
#     if int(x.narxi) > int(kichik):
#         kichik = x.narxi
#
# print("=== ENG ARZON MEVA ===")
# print(
#     f"Meva nomi: {x.nomi}\n"
#     f"Vazni: {x.vazni}\n"
#     f"Narxi: {x.narxi}"
# )


"""Task 5: Sportchilar Ro’yxati"""

# class Sportchi:
#     def __init__(self, ismi, yoshi, soprt_turi):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.soprt_turi = soprt_turi
#
# ali = Sportchi("Ali", "25", "Futbol")
# vali = Sportchi("Vali", "22", "Basketbol")
# hasan = Sportchi("Hasan", "28", "Tennis")
# husan = Sportchi("Husan", "20", "Suzish")
# olim = Sportchi("Olim", "24", "Voleybol")
#
# print(f"{ali.ismi} - {ali.yoshi} yosh, {ali.soprt_turi}")
# print(f"{vali.ismi} - {vali.yoshi} yosh, {vali.soprt_turi}")
# print(f"{hasan.ismi} - {hasan.yoshi} yosh, {hasan.soprt_turi}")
# print(f"{husan.ismi} - {husan.yoshi} yosh, {husan.soprt_turi}")
# print(f"{olim.ismi} - {olim.yoshi} yosh, {olim.soprt_turi}\n")
#
# eng_yosh = ali
#
# for x in [ali, vali, hasan, husan, olim]:
#     if int(x.yoshi) < int(eng_yosh.yoshi):
#         eng_yosh = x
#
# print("=== ENG YOSH SPORTCHI ===")
# print(f"Ismi: {eng_yosh.ismi}\nYoshi: {eng_yosh.yoshi}\nSport turi: {eng_yosh.soprt_turi}")


"""Task 6: Xodimlar Ro'yxati"""


# class Xodim:
#     def __init__(self, ismi, lavozimi, maoshi):
#         self.ismi = ismi
#         self.lavozimi = lavozimi
#         self.maoshi = maoshi
#
# ali = Xodim("Ali", "Dasturchi", "5000000")
# vali = Xodim("Vali", "Dizayner", "4000000")
# hasan = Xodim("Hasan", "Menejer", "7000000")
# husan = Xodim("Husan", "Tester", "3500000")
# olim = Xodim("Olim", "DevOps", "6000000")
#
# print("=== XODIMLAR RO'YXATI ===")
# print(f"{ali.ismi} - {ali.lavozimi}, {ali.maoshi}")
# print(f"{vali.ismi} - {vali.lavozimi}, {vali.maoshi}")
# print(f"{hasan.ismi} - {hasan.lavozimi}, {hasan.maoshi}")
# print(f"{husan.ismi} - {husan.lavozimi}, {husan.maoshi}")
# print(f"{olim.ismi} - {olim.lavozimi}, {olim.maoshi}\n")
#
# print("=== ENG KATTA MAOSHLI XODIM ===")
#
# eng_katta = ali
#
# for x in [ali, vali, hasan, husan, olim]:
#     if int(x.maoshi) > int(eng_katta.maoshi):
#         eng_katta = x
# print(f"Ismi: {eng_katta.ismi}\nLavozimi: {eng_katta.lavozimi}\nMaoshi: {eng_katta.maoshi} so'm")

"""Task 7: Avtomobillar Saloni"""

# class Avtomobil:
#     def __init__(self, modeli, rangi, yili):
#         self.modeli = modeli
#         self.rangi = rangi
#         self.yili = yili

# chevrolet = Avtomobil("Chevrolet Malibu", "Oq", 2020)
# toyota = Avtomobil("Toyota Camry", "Qora", 2022)
# hyundai = Avtomobil("Hyundai Sonata", "Kumush", 2019)
# kia = Avtomobil("Kia K5", "Ko'k", 2023)
# bmw = Avtomobil("BMW X5", "Qizil", 2021)

# print("=== AVTOMOBILLAR RO'YXATI ===")
# for auto in [chevrolet, toyota, hyundai, kia, bmw]:
#     print(f"{auto.modeli} ({auto.rangi}) - {auto.yili}")

# eng_yangi = chevrolet
# for auto in [chevrolet, toyota, hyundai, kia, bmw]:
#     if auto.yili > eng_yangi.yili:
#         eng_yangi = auto

# print("\n=== ENG YANGI AVTOMOBIL ===")
# print(f"Modeli: {eng_yangi.modeli}")
# print(f"Rangi: {eng_yangi.rangi}")
# print(f"Yili: {eng_yangi.yili}")


"""Task 8: Mahsulotlar Ombori"""  

# class Mahsulot:
#     def __init__(self, nomi, miqdori, narxi):
#         self.nomi = nomi
#         self.miqdori = miqdori
#         self.narxi = narxi

# kompyuter = Mahsulot("Kompyuter", 10, 8000000)
# monitor = Mahsulot("Monitor", 15, 2000000)
# klaviatura = Mahsulot("Klaviatura", 20, 200000)
# sichqoncha = Mahsulot("Sichqoncha", 25, 100000)
# printer = Mahsulot("Printer", 5, 3000000)

# print("=== MAHSULOTLAR OMBORI ===")
# print(f"{kompyuter.nomi}: {kompyuter.miqdori} dona x {kompyuter.narxi} = {kompyuter.miqdori * kompyuter.narxi} so'm")
# print(f"{monitor.nomi}: {monitor.miqdori} dona x {monitor.narxi} = {monitor.miqdori * monitor.narxi} so'm")
# print(f"{klaviatura.nomi}: {klaviatura.miqdori} dona x {klaviatura.narxi} = {klaviatura.miqdori * klaviatura.narxi} so'm")
# print(f"{sichqoncha.nomi}: {sichqoncha.miqdori} dona x {sichqoncha.narxi} = {sichqoncha.miqdori * sichqoncha.narxi} so'm")
# print(f"{printer.nomi}: {printer.miqdori} dona x {printer.narxi} = {printer.miqdori * printer.narxi} so'm\n")

# umumiy_qiymat = 0
# for i in [kompyuter, monitor, klaviatura, sichqoncha, printer]:
#     umumiy_qiymat += i.miqdori * i.narxi
# print(f"UMUMIY QIYMAT: {umumiy_qiymat} so'm")


"""Task 9: O'quvchilar Bahosi"""

# class Oquvchi:
#     def __init__(self, ismi, sinfi, ortacha_baho):
#         self.ismi = ismi
#         self.sinfi = sinfi
#         self.ortacha_baho = ortacha_baho

# ali = Oquvchi("Ali", "9-sinf", 4.5)
# vali = Oquvchi("Vali", "10-sinf", 4.8)
# hasan = Oquvchi("Hasan", "9-sinf", 3.9)
# husan = Oquvchi("Husan", "11-sinf", 4.2)
# olim = Oquvchi("Olim", "10-sinf", 5.0)  

# print("=== O'QUVCHILAR RO'YXATI ===")
# for oquvchi in [ali, vali, hasan, husan, olim]:
#     print(f"{oquvchi.ismi} - {oquvchi.sinfi}, O'rtacha baho: {oquvchi.ortacha_baho}")

# eng_alochi = ali
# for oquvchi in [ali, vali, hasan, husan, olim]:
#     if oquvchi.ortacha_baho > eng_alochi.ortacha_baho:
#         eng_alochi = oquvchi

# print("\n=== ENG A'LOCHI O'QUVCHI ===")
# print(f"Ismi: {eng_alochi.ismi}")
# print(f"Sinfi: {eng_alochi.sinfi}")
# print(f"O'rtacha bahosi: {eng_alochi.ortacha_baho}")

"""Task 10: Uylar Agentligi"""

# class Uy:
#     def __init__(self, manzili, x_soni, narxi):
#         self.manzili = manzili
#         self.x_soni = x_soni
#         self.narxi = narxi

# uy1 = Uy("Chilonzor", 2, 80000)
# uy2 = Uy("Yunusobod", 3, 120000)
# uy3 = Uy("Sergeli", 1, 45000)
# uy4 = Uy("Mirzo Ulug'bek", 4, 180000)
# uy5 = Uy("Yakkasaroy", 3, 150000)

# print("=== UYLAR RO'YXATI ===")
# for uy in [uy1, uy2, uy3, uy4, uy5]:
#     print(f"{uy.manzili}, {uy.x_soni} xonali - {uy.narxi}$")

# eng_kop_xonali = uy1
# for uy in [uy1, uy2, uy3, uy4, uy5]:
#     if uy.x_soni > eng_kop_xonali.x_soni:
#         eng_kop_xonali = uy
# print("\n=== ENG KO'P XONALI UY ===")
# print(f"Manzili: {eng_kop_xonali.manzili}\nXonalar soni: {eng_kop_xonali.x_soni}\nNarxi: {eng_kop_xonali.narxi}$")