nomes = []
notas = []

while True:
    nome = input("Nome do aluno (ou 'FIM' para encerrar): ").strip()

    if nome.upper() == "FIM":
        break

    if nome == "":
        print("Nome não pode ser vazio. Tente novamente.")
        continue

    # validar nota
    while True:
        try:
            nota = float(input(f"Nota de {nome}: "))
            if 0 <= nota <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except:
            print("Digite um valor numérico válido.")

    nomes.append(nome)
    notas.append(nota)


# --- Relatório final ---
if len(notas) == 0:
    print("\nNenhum aluno foi registrado.")
else:
    total = len(notas)
    media_geral = sum(notas) / total

    maior_nota = max(notas)
    menor_nota = min(notas)

    aluno_maior = nomes[notas.index(maior_nota)]
    aluno_menor = nomes[notas.index(menor_nota)]

    acima_da_media = sum(1 for n in notas if n > media_geral)

    print("\n=== Relatório Final ===")
    print(f"Total de alunos: {total}")
    print(f"Média geral: {media_geral:.3f}")
    print(f"Maior nota: {aluno_maior} -> {maior_nota}")
    print(f"Menor nota: {aluno_menor} -> {menor_nota}")
    print(f"Alunos acima da média: {acima_da_media}")
