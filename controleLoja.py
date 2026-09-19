class Loja:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preço=preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self,novo_preco):
        if novo_preco<0:
            raise ValueError("O preço tem que ser maior que 0")

        self.__preco=novo_preco
        print("Preço cadastrado/alterado com sucesso!")

    def exibir_informação(self):
        print ("Nome do Produto",self.nome)
        print ("Preço do Produto",self.preço)

try:
    produto=Loja("Mouse", 50)
    produto.exibir_informação()
except ValueError as erro:
    print("Erro",erro)

try:
    produto.preco=-500
    produto.exibir_informação()
except ValueError as erro:
    print("Erro",erro)

print("\nTestando com valor válido")
try:
    produto.preco=100
    produto.nome="----"
    produto.exibir_informação()
except ValueError as erro:
    print("Erro:",erro)
        