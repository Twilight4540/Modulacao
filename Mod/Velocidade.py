#Declaração
VM: float = 0.0
#Inicio
def velocidade(VM):
    NV: int = 0
    EC: int = 0
    T: int = 0
    D: float = 0.0
    NV = int(input('Digite o número de voltas: '))
    EC = int(input('Digite a extenção do circuito em metros: '))
    T = int(input('Digite o tempo gasto em minutos: '))
    if NV <= 0 or EC <= 0 or T <= 0 or T > 60:
        print('Erro! Valores inválidos!')
    else:
        D = NV * EC
        D = D / 1000
        T = T / 60
        VM = D / T
        print('A velocidade média do carro é de: ', VM, 'Km/h')

def main():
    velocidade(VM)

if __name__ == '__main__':
    main()