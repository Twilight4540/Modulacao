#Declarar
N1: int = 0
N2: int = 0
D: int = 0
#Inicio

def diferença():
    global N1, N2, D
    N1 = int(input('Digite o 1° número: '))
    N2 = int(input('Digite o 2° número: '))
    if N1 > N2:
        D = N1 - N2
    else:
        D = N2 - N1
    print('A diferença entre os dois números do maior para o menor é de: ', D)

def main():
    diferença()

if __name__ == '__main__':
    main()