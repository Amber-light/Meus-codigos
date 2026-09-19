class Manutencao:
    def __init__(self,descricao,responsavel,custos,status):
        self.descricao=descricao
        self.responsavel=responsavel
        self.custos=custos
        self.status=status

    @property
    def custos(self):
        return self.__custos

    @custos.setter
    def custos(self,novos_custos):
        if novos_custos<0:
            raise ValueError("Os custos tem que ser maior que 0")

        self.__custos=novos_custos
        print("Custos cadastrados/alterados com sucesso!")

        @property
        def descricao(self):
            return self.__descricao
    
        @descricao.setter
        def descricao(self,nova_descricao):
            if not nova_descricao:
                raise ValueError("Descrição não pode ser vazia")
            self.__descricao=nova_descricao

        @custos.setter
        def custos(self,novos_custos):
            if novos_custos<0:
                raise ValueError("Os custos tem que ser maior que 0")

            self.__custos=novos_custos
            print("Custos cadastrados/alterados com sucesso!")
    

    def exibir_informação(self):
        print ("Descrição",self.descricao)
        print ("Responsável",self.responsavel)
        print ("Custos",self.custos)

try:
    produto=Manutencao("Mouse", "João", 50, "Ativa")
    produto.exibir_informação()
except ValueError as erro:
    print("Erro",erro)

try:
    produto.custos=-500
    produto.exibir_informação()
except ValueError as erro:
    print("Erro",erro)

print("\nTestando com valor válido")
try:
    produto.custos=100
    produto.descricao="----"
    produto.exibir_informação()
except ValueError as erro:
    print("Erro:",erro)
        