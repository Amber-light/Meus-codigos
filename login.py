senha_correta ="python123"
tentativas = 0
senha= ""
while senha!=senha_correta and tentativas<3:
    senha=input("Senha:")
    tentativas+= 1
if senha==senha_correta:print("Acesso permitido")
else:print("Acesso bloqueado")    