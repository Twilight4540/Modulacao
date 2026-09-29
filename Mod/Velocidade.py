def velocidade(NV, EC, T):
    VM: float = 0.0
    D: int = 0
    D = NV * EC
    D = D / 1000
    T = T / 60
    VM = D / T
    return VM
    

def main():
    numvol: int = 0
    ex: int = 0
    t: int = 0
    numvol = int(input('Digite o número de voltas: '))
    ex = int(input('Digite a extenção do circuito em metros: '))
    t = int(input('Digite o tempo gasto em minutos: '))
    if numvol <= 0 or ex <= 0 or t <= 0:
        print('Erro! Valores inválidos!')
    else:
        valor_vel = velocidade(numvol, ex, t)
        print('A velocidade média do carro é de: ', valor_vel , 'Km/h')

if __name__ == '__main__':
    main()