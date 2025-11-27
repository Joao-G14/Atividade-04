N = int(input())

fat = 1
contador = N

while contador > 1:
    fat *= contador
    contador -= 1

print(fat)
