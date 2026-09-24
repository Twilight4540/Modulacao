#Declaração
PN: float = 0.0
#inicio
def preço(PN):
    PA: float = 0.0
    VM: float = 0.0
    PA = float(input('Digite o valor do preço atual: '))
    VM = float(input('Digite o valor da venda mensal: '))
    if VM < 500 and PA < 30:
        PN = PA * 1.10
        print('O valor do produto após o reajuste é: ', PN)
    elif (VM >= 500 and VM < 1000) and (PA >= 30 and PA < 80):
        PN = PA * 1.15
        print('O valor do produto após o reajuste é: ', PN)
    elif VM >= 1000 and PA >= 80:
        PN = PA * 0.95
        print('O valor do produto após o reajuste é: ', PN)
    else:
        PN = PA
        print('O valor do produto não sofreu alteração')

def main():
    preço(PN)

if __name__ == '__main__':
    main()