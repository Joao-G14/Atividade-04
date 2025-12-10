dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

lojas = int(input("Quantas lojas deseja analisar? "))

lista_lodas_vendas = []   # Lista externa com listas internas das vendas

# --- Entrada das vendas ---
for i in range(lojas):
    print(f"\n--- Loja {i+1} ---")
    vendas_semana = []

    for d in range(7):
        valor = float(input(f"Vendas de {dias[d]}: "))
        vendas_semana.append(valor)

    lista_lodas_vendas.append(vendas_semana)


# --- Processamento ---
maior_total = -9999999
menor_total =  9999999
loja_maior = 0
loja_menor = 0

for i in range(lojas):
    vendas = lista_lodas_vendas[i]

    total = sum(vendas)
    media = total / 7

    maior = max(vendas)
    menor = min(vendas)

    dia_maior = dias[vendas.index(maior)]
    dia_menor = dias[vendas.index(menor)]

    print(f"\n=== Resultados da Loja {i+1} ===")
    print(f"Total semanal: {total}")
    print(f"Média diária: {media:.2f}")
    print(f"Dia de maior venda: {dia_maior} → {maior}")
    print(f"Dia de menor venda: {dia_menor} → {menor}")

    if total > maior_total:
        maior_total = total
        loja_maior = i + 1

    if total < menor_total:
        menor_total = total
        loja_menor = i + 1


# --- Resultado final ---
print("\n=== Comparação entre lojas ===")
print(f"Loja com MAIOR total semanal: Loja {loja_maior} → {maior_total}")
print(f"Loja com MENOR total semanal: Loja {loja_menor} → {menor_total}")
