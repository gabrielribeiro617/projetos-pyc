'''
import re
quarto = []
qtd_pes = int(input('Quantidade de pessoas: '))
for i in range(qtd_pes):
    print(f'PESSOA {i + 1}')
    nome = str(input('Nome: ')).strip().title()
    cpf = str(input('CPF: '))
    cpf_fmt = re.sub(r'[.\-\s]', '', cpf)
    hospede = [nome, f'cpf:{cpf_fmt}']
    quarto.append(hospede)
print(quarto)
'''
'''
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
for item in vendas:
    if item[1] > meta:
        print(f'{item[0]} -> {item[1]}')
'''
produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
for i, item in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        cres = ((vendas2020[i] / vendas2019[i]) - 1) * 100
        print(f'{item} vendeu R$ {vendas2019[i]}(2019) -> {vendas2020[i]}(2020) com {cres:.2f}%^')
