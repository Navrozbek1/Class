""" Dataclass bo‘yicha 10 ta masala """

from dataclasses import dataclass

from telebot.formatting import hide_link


# 1-masala: Talaba ma’lumoti

# @dataclass
# class Talaba:
#     ism: str
#     yosh: int
#     kurs: int
#
# x = Talaba('Ali', 19, 2)
# print(x)

# 2-masala: Kitob ma’lumoti

# @dataclass
# class Kitob:
#     nomi: str
#     muallifi: str
#     saxifa_soni: int
#
# x = Kitob('Bek', 'bek', 56)
# print(x)

# 3-masala: Telefon ma’lumoti

# @dataclass
# class Telefon:
#     brand: str
#     model: str
#     narx: float
#
# x = Telefon('Honor', 'Honor x9c', 4_000_000)
# print(x)

# 4-masala: Avtomobil

# @dataclass
# class Avtomobil:
#     marka: str
#     rang: str
#     yil: int
#
# print(Avtomobil('bilman', 'oq', 5))

# 5-masala: Shahar

# @dataclass
# class Shahar:
#     nomi: str
#     davlat: str
#     aholi: int
#
# print(Shahar('toshkent', 'Ozbekiston', 43347))

# 6-masala: Kompyuter

# @dataclass
# class Kompyuter:
#     protsessor: str
#     ram: str
#     xotira: int
#
# print(Kompyuter('bilmadim', 'bilmadim', 64))

# 7-masala: Film

# @dataclass
# class Film:
#     nomi: str
#     janr: str
#     yil: int
#
# print(Film('bilmadim', 'bilmadim', 3))

# 8-masala: Bank hisob raqami

# @dataclass
# class Hisob:
#     ism: str
#     hisob_raqam: int
#     balans: int
#
# print(Hisob('bek', 860000000, 2373472))

# 9-masala: O‘qituvchi

# @dataclass
# class Oqituvchi:
#     ism: str
#     fan: str
#     y_t: int
#
# print(Oqituvchi('bek', 'math', 5))

# 10-masala: Mahsulot

# @dataclass
# class Mahsulot:
#     nomi: str
#     narx: int
#     miqdo: int
#
# print(Mahsulot('olma', 500, 5))
