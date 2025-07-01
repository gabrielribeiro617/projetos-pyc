'''
print('Alo mundo')

num = int(input('\nDigite um número: '))
print(f'O número informado foi {num}')

num1 = int(input('\nDigite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print(f'A soma de {num1} + {num2} = {soma}\n')

notas = []
for i in range(4):
    notas.append(float(input(f'{i + 1}ª nota: ')))
media = sum(notas) / len(notas)
print(f'Média: {media:.2f}')

m = float(input('Comprimento em metros: '))
cm = m * 100
print(f'{m:.2f}m = {cm}cm')

largura = float(input('Largura da sala: '))
comprimento = float(input('Comprimento da sala: '))
area = largura * comprimento
print(f'Área: {area}m²')

ganho_hora = float(input('Ganho por hora: R$'))
h_trab = int(input('Horas trabalhadas no mês: '))
tot_sal = ganho_hora * h_trab
print(f'Total do salário: R${tot_sal}')

gf = int(input('Temperatura em ºF: '))
gc = int(5 / 9 * (gf - 32))
print(f'Temperatura em Celsius: º{gc}')

gc = int(input('Temperatura em ºC: '))
gf = int(9 / 5 * gc + 32)
print(f'Temperatura em Fahrenheit: º{gf}')

h = float(input('Altura em metros: '))
p = 72.7 * h - 58
print(f'O seu peso ideal é {p:.2f}Kg')

h = float(input('Altura em metros: '))
sexo = str(input('Sexo [M/F]: '))
if 'M' in sexo:
    p = 72.7 * h - 58
    print(f'O seu peso ideal é {p:.2f}Kg')
else:
    p = 62.1 * h - 44.7
    print(f'O seu peso ideal é {p:.2f}Kg')

ganho_hora = float(input('Ganho por hora: R$'))
h_trab = int(input('Horas trabalhadas no mês: '))
sal_bruto = ganho_hora * h_trab
desc_ir = sal_bruto * 0.11
desc_inss = sal_bruto * 0.08
desc_sind = sal_bruto * 0.05
descontos = desc_ir + desc_inss + desc_sind
sal_liq = sal_bruto - descontos
print(f'Salário bruto: R${sal_bruto:.2f}')
print(f'Desconto do IR: R${desc_ir:.2f}')
print(f'Desconto do INSS: R${desc_inss:.2f}')
print(f'Desconto do sindicato: R${desc_sind:.2f}')
print(f'Salário líquido: R${sal_liq:.2f}')

import math
m2 = float(input('Área a ser pintada: '))
tinta = math.ceil(m2 / 18)
tot_preco = tinta * 80
print(f'Precisa de {tinta} lata(s) de tinta')
print(f'Custará: R${tot_preco:.2f}')
'''
mb = float(input('Tamanho do arquivo (MB): '))
vel = float(input('Velocidade da conexão (Mbps): '))
megabits = mb / 8
tempo_min = (megabits / vel) * 60
print(f'O tempo de download é de {tempo_min} minutos')