funcionario = {}
bonus = 0.0
for i in range(3):
    print(f'FUNCIONÁRIO {i + 1}')
    nome = str(input('Nome: ')).title()
    vendas = float(input('Valor de vendas: R$'))
    if vendas >= 2000:
        bonus = vendas * 0.15
    elif 2000 >= vendas >= 1000:
        bonus = vendas * 0.10
    else:
        bonus = 0.0
    funcionario[nome] = bonus
    print('--' * 20)
for nome, bonus in funcionario.items():
    print(f'O(A) funcionário(a) {nome} ganhou R${bonus:.2f} de bônus')
