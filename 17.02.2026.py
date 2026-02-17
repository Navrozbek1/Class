class Salomlashish:
    def __init__(self, ism, fam):
        self.ism = ism
        self.fam = fam

    def salom(self):
        print(f"Asalomu alaykim hurmatli {self.ism} {self.fam} jamoga hush kelibsiz !")

s1 = Salomlashish("Ali", "Valiyev")
s2 = Salomlashish("Bek", "Husanov")
s3 = Salomlashish("Shox", "Boburov")

s1.salom()
s2.salom()
s3.salom()