class Animal:
    def __init__(self, tipo):
        self.tipo = tipo

    def falarIngles(self):
        print(f"{self.tipo}: Hello Man!")

cavalo = Animal("Cavalo")
cavalo.falarIngles()