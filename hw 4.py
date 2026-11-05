class Prystriy:

    def __init__(self, name):
        self.name = name

    def uvimknuty(self):
        print(f"Пристрій '{self.name}' увімкнено.")

    def vymknuty(self):
        print(f"Пристрій '{self.name}' вимкнено.")

class Smartphone(Prystriy):

    def __init__(self, name, model):
        Prystriy.__init__(self, name)
        self.model = model

    def uvimknuty(self):
        Prystriy.uvimknuty(self)
        print(f"Завантаження операційної системи смартфона {self.model}...")

phone = Smartphone("Телефон", "iPhone 17")
phone.uvimknuty()
phone.vymknuty()