#Declararação de variáveis
N1: float = 0.0
N2: float = 0.0
N3: float = 0.0
N4: float = 0.0
NF: float = 0.0
#Inicio
def notas():
    global N1, N2, N3, N4, NF
    N1 = float(input('Digite a primeira nota: '))
    N2 = float(input('Digite a segunda nota: '))
    N3 = float(input('Digite a terceira nota: '))
    N4 = float(input('Digite a quarta nota: '))
    NF = (N1 + N2 + N3 + N4)/4
    if NF >= 6.0:
        print('Aprovado com nota: ', NF)
    else:
        if NF >= 3.0:
            print('EXAME')
        else:
            print('Retido com nota: ', NF)
def main():
    notas()

if __name__ == '__main__':
    main()