class Tecnico:
    def __init__(self,nome):
        self.nome = nome

    def realizar_manutencao(self,equipamento):
        print(f"O técnico {self.nome} está realizando manutenção no equipamento {equipamento.nome}")

class Equipamento:
    def __init__(self,nome):
        self.nome = nome
    
    def manutencao(self,tecnico):
        print(f"O equipamento {self.nome} está com o tecnico {tecnico.nome}")

tecnico1 = Tecnico("Lucas")
tecnico2= Tecnico("Maria")

equipamento1 = Equipamento("MacBook Air")
equipamento2 = Equipamento("Projetor Samsung")

tecnico1.realizar_manutencao(equipamento1)
tecnico2.realizar_manutencao(equipamento2)

equipamento1.manutencao(tecnico1)

print(tecnico1.nome)
print(tecnico2.nome)