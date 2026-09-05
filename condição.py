horas=int(input("Quantas horas utilizadas?:"))
defeito=input("Equipamento possui defeito:").lower()

if defeito=="sim":
    print("manutenção urgente")
elif defeito=="não" and horas>=500:
    print("preventiva")
else:
    print("Tudo certo")    