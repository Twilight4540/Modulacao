def fatorial(n):
    c: int = 1
    r: int = 1
    i: int = 1
    while c <= n:
        r = c * r
        c = c + 1
    return r

def main():
    N: int = 0
    fat: int = 0
    N = int(input('Digite o número: '))
    fat = fatorial(N)
    print('O fatorial desse número é igual a:', fat)

if __name__ == '__main__':
    main()