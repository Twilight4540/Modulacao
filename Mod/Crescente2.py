#Declarar
N1: float = 0.0
N2: float = 0.0
N3: float = 0.0
N4: float = 0.0
#Inicio
def crescente2():
    global N1, N2, N3, N4
    N1 = float(input('Digite o 1° número: '))
    N2 = float(input('Digite o 2° número: '))
    N3 = float(input('Digite o 3° número: '))
    if N1 > N2 or N2 > N3:
        print('Os 3 primeiros números não estão em ordem crescente. Tente novamente.')
    else:
        N4 = float(input('Digite o 4° número: '))
        if N4 < N1:
            print('A ordem crescente é: ', N4, N1, N2, N3)
        else:
            if N4 < N2:
                print('A ordem crescente é: ', N1, N4, N2, N3)
            else:
                if N4 < N3:
                    print('A ordem crescente é: ', N1, N2, N4, N3)
                else:
                    print('A ordem crescente é: ', N1, N2, N3, N4)

def main():
    crescente2()

if __name__ == '__main__':
    main()
