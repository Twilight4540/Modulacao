def fatorial(n):
    c: int = 1
    r: int = 1
    i: int = 1
    while c <= n:
        r = c * r
        c = c + 1
    return r

def divisao(pri, seg):
    return pri / seg

def main():
    N: int = 0
    fat: int = 0
    i: int = 1
    div: int = 0
    som: int = 1
    N = int(input('Digite o número: '))

    while i <= N:
        fat = fatorial(i)
        div = divisao(1, fat)
        i += 1
        som = som + div
    
    print('A soma desse número é igual a:', som)

if __name__ == '__main__':
    main()