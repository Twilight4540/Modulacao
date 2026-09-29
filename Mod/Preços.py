def preço(PA, VM):
    if VM < 500 and PA < 30:
        PN = PA * 1.10
        return print('O valor do produto após o reajuste é: ', PN)
    elif (VM >= 500 and VM < 1000) and (PA >= 30 and PA < 80):
        PN = PA * 1.15
        return print('O valor do produto após o reajuste é: ', PN)
    elif VM >= 1000 and PA >= 80:
        PN = PA * 0.95
        return print('O valor do produto após o reajuste é: ', PN)
    else:
        PN = PA
        return print('O valor do produto não sofreu alteração')

def main():
    prat: float = 0.0
    venmen: float = 0.0
    PF: str = ''
    prat = float(input('Digite o valor do preço atual: '))
    venmen = float(input('Digite o valor da venda mensal: '))
    PF = preço(prat, venmen)

if __name__ == '__main__':
    main()