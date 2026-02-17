class Salomlashish:
    def __init__(self, ism, fam): # Konustruktr
        self.__ism = ism
        self.__fam = fam

    def get_ism(self): # Maxsus Metod, Bu yashrin xususiyatlarni olish uchun ishlatiladi !
        return self.__ism

    def get_fam(self): # Maxsus Metod, Bu yashrin xususiyatlarni olish uchun ishlatiladi !
        return self.__fam

    def salom(self):
        print(f"Asalomu alaykim hurmatli {self.ism} {self.fam} jamoga hush kelibsiz !")

s1 = Salomlashish("Ali", "Valiyev")
s2 = Salomlashish("Bek", "Husanov")
s3 = Salomlashish("Shox", "Boburov")

print(s1.get_ism())
print(s1.get_fam())
