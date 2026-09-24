#Declaração
N1: int = 0
N2: int = 0
#Inicio
def inteiros3():
    global N1, N2
    N1 = int(input('Digite o 1° número: '))
    N2 = int(input('Digite o 2° número: '))
    if N1 == N2:
        print('Os números são iguais')
    else:
        if N1 > N2:
            if N1 == int(N1/N2)*N2:
                print('O número', N1, 'é múltiplo de ', N2)
            else:
                print('O número', N1, 'não é múltiplo de ', N2)
        else:
            if N2 == int(N2/N1)*N1:
                print('O número', N2, 'é múltiplo de ', N1)
            else:
                print('O número', N2, 'não é múltiplo de ', N1)

def main():
    inteiros3()

if __name__ == '__main__':
    main()