#Declaração
N: int = 0
#Inicio
def inteiro():
    global N
    N = int(input('Digite o 1° número: '))
    if N / 2 == int(N/2) and N / 3 == int(N/3):
        print('O número é divisível por 2 e 3')
    else:
        print('O número não é divisível por 2 e 3')

def main():
    inteiro()

if __name__ == '__main__':
    main()

#Fim
    