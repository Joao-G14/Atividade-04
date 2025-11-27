n = int(input())

if n < 1:
    print(1)

    exit()


if n >= 13:
    print("Erro")
    exit()

resultado = 1
i = n

while True:
    resultado *= i
    i -= 1
    
    if i == 0:
        break

print(resultado)
