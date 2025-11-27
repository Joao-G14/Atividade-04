n = int(input())

def primo(x):
    d = 2
    conta_div = 0

    while d * d <= x:
        conta_div += (x % d == 0)
        d += 1

    return {
        True:  f"{x} nao eh primo",
        False: f"{x} eh primo"
    }[conta_div > 0]

i = 0
while i < n:
    x = int(input())
    print(primo(x))
    i += 1
