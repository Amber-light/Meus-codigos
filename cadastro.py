alunos = []

for i in range(3):
    print(f"\n--- Cadastro do aluno {i + 1} ---")

    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3=float(input("Nota 3:"))
    email=input("Email:")
    matricula=input("Matricula:")

    media = (nota1 + nota2+nota3) / 2

    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao,
        "email":email,
        "matricula":matricula
    }

    alunos.append(aluno)


print("\n" + "=" * 70)
print(f"{'NOME':<25} {'EMAIL':<25} {'MATRICULA':<25} {'NOTA 1':<10} {'NOTA 2':<10} {'NOTA 3':<10} {'MÉDIA':<10} {'SITUAÇÃO':<15}")
print("=" * 70)

for aluno in alunos:
    print(
        f"{aluno['nome']:<25} "
        f"{aluno['email']:<25}"
        f"{aluno['matricula']:<25}"
        f"{aluno['nota1']:<10.1f} "
        f"{aluno['nota2']:<10.1f} "
        f"{aluno['nota3']:<10.1f}"
        f"{aluno['media']:<10.1f} "
        f"{aluno['situacao']:<15}"
    )

print("=" * 70)


aprovados = 0
reprovados = 0

for aluno in alunos:
    if aluno["situacao"] == "Aprovado":
        aprovados += 1
    else:
        reprovados += 1

print(f"\nTotal de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")