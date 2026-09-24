#Declaração
HI: int = 0
MI: int = 0
HF: int = 0
MF: int = 0
I: int = 0
F: int = 0
D: int = 0
H: int = 0
M: int = 0

def jogo():
    global HI, MI, HF, MF, I, F, D, H, M
    HI = int(input('Digite a hora inicial: '))
    MI = int(input('Digite o minuto inicial: '))
    HF = int(input('Digite a hora final: '))
    MF = int(input('Digite o minuto final: '))
    if HI >= 24 or HI < 0 or HF >= 24 or HF < 0 or MI >= 60 or MI < 0 or MF >= 60 or MF < 0:
        print('Hora ou minuto inválido')
    else:
        I = (HI * 60) + MI
        F = (HF * 60) + MF
        if F < I:
            F = F + 1440
        D = F - I
        H = int(D / 60)
        M = D - (H * 60)
        print('O jogo durou: ', H,':', M)

def main():
    jogo()

if __name__ == '__main__':
    main()