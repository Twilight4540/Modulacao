#Declarar
N1: float = 0.0
N2: float = 0.0

def real():
    global N1, N2
    N1 = float(input('Digite o 1° número: '))
    N2 = float(input('Digite o 2° número: '))

def main():
    real()
    if N1 > N2:
        print('O maior número é: ', N1)
    else:
        print('O maior número é: ', N2)

if __name__ == '__main__':
    main()