def investimento(V, tipo):
    VF: float = 0.0
    if tipo == '1':
        VF = V * 1.03
        print('O valor do investimento em Poupança é: ', VF)
    elif tipo == '2':
        VF = V * 1.05
        print('O valor do investimento em Renda Fixa é: ', VF)
    else:
        print('Opção inválida') 

def main():
    vi: float = 0.0
    tipinv: str = ''
    valinv: str = ''
    tipinv = input('Digite 1 para Poupança ou 2 para Renda Fixa: ')
    vi = float(input('Digite o valor do investimento: '))
    valinv = investimento(vi, tipinv)

if __name__ == '__main__':
    main()