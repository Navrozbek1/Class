# Bu class - Class bu shablon, arxitektor chizgan chizma deb tushunish mumkin !
class Car:
    def __init__(self, model, rang, narx): # Bu Canustructor motodi !
        # model, rang, narx - Bular Attribut
        self.model = model
        self.rang = rang
        self.narx = narx

    def malumot(self): # Bu malumot metodi - Metod bu class ichida yoziladi!
        return f"Model: {self.model}, Rang: {self.rang} rangli, Narxi: {self.narx} so'm!"

# Object yaratish
# Object — klass asosida yaratilgan aniq nusxasi!

car = Car('Legenda 😂', 'Oq', 'Fit filiyon $') # Bu Object deyiladi !

