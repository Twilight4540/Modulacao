#Declaração
VF: float = 0.0
#Inicio
def investimento(VF):
    V: float = 0.0
    tipo: str = ''
    tipo = input('Digite 1 para Poupança ou 2 para Renda Fixa: ')
    V = float(input('Digite o valor do investimento: '))
    if tipo == '1':
        VF = V * 1.03
        print('O valor do investimento em Poupança é: ', VF)
    elif tipo == '2':
        VF = V * 1.05
        print('O valor do investimento em Renda Fixa é: ', VF)
    else:
        print('Opção inválida') 

def main():
    investimento(VF)

if __name__ == '__main__':
    main()