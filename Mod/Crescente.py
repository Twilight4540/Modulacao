#Declaração
N1: int = 0
N2: int = 0

def crescente():
    global N1, N2
    N1 = int(input('Digite o 1° número: '))
    N2 = int(input('Digite o 2° número: '))
    if N1 == N2:
        print('Os números são iguais')
    else:
        if N1 > N2:
            print('Os número em ordem crescente são: ', N2, 'e', N1)
        else:
            print('Os número em ordem crescente são: ', N1, 'e', N2)

def main():
    crescente()

if __name__ == '__main__':
    main()