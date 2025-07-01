'''
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
mai = num1
if num2 > mai:
    mai = num2
print(f'Maior número: {mai}')
'''
'''
val = float(input('Digite um valor: '))
if val >= 0:
    print(f'{val} é um valor positivo')
else:
    print(f'{val} é um valor negativo')
'''
'''
estado = str(input('Estado Civil: ')).strip().upper()
match estado:
    case 'C':
        print(f'{estado} - Casado')
    case 'S':
        print(f'{estado} - Solteiro')
    case 'D':
        print(f'{estado} - Divorciado')
    case 'V':
        print(f'{estado} - Viúvo')
    case 'O':
        print(f'{estado} - Outros')
'''
'''
emails_spam = ('fulano@gmail.com','beltrano@gmail.com', 'ciclano@gmail.com')
email = str(input('E-mail: '))
if email in emails_spam:
    print('E-mail de Spam')
'''
'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
'''
'''
emp1 = float(input('Orçamento empresa 1: R$'))
emp2 = float(input('Orçamento empresa 2: R$'))
emp3 = float(input('Orçamento empresa 3: R$'))
mai = emp1
if emp2 > mai:
    mai = emp2
if emp3 > mai:
    mai = emp3
print(f'Maior orçamento: R${mai:.2f}')
'''
'''
emp1 = float(input('Orçamento empresa 1: R$'))
emp2 = float(input('Orçamento empresa 2: R$'))
emp3 = float(input('Orçamento empresa 3: R$'))
mai = emp1
men = emp1
if emp2 > mai:
    mai = emp2
elif emp2 < men:
    men = emp2
if emp3 > mai:
    mai = emp3
elif emp3 < men:
    men = emp3
print(f'Maior orçamento: R${mai:.2f}')
print(f'Menor orçamento: R${men:.2f}')
'''
'''
prec1 = float(input('Preço 1: R$'))
prec2 = float(input('Preço 2: R$'))
prec3 = float(input('Preço 3: R$'))
men = prec1
if prec2 < men:
    men = prec2
if prec3 < men:
    men = prec3
print(f'Compre o de R${men:.2f}')
'''
'''
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))
mai = n1
men = n1
if n2 > mai:
    mai = n2
elif n2 < men:
    men = n2
if n3 > mai:
    mai = n3
elif n3 < men:
    men = n3
aux = (n1 + n2 + n3) - mai - men
print(f'{mai} {aux} {men}')
'''
'''
tur = str(input('Em que turno você estuda? ')).strip().upper()
match tur:
    case 'M':
        print('Bom dia!')
    case 'V':
        print('Boa tarde!')
    case 'N':
        print('Boa noite!')
'''
'''
sal = float(input('Salario: R$'))
if sal <= 280:
    porc = 20
elif sal < 700:
    porc = 15
elif sal < 1500:
    porc = 10
else:
    porc = 5
aum = sal * (porc/100)
n_sal = sal + aum
print(f'Antes do reajuste: R${sal:.2f}')
print(f'Percentual de aumento: {porc}%')
print(f'Valor do aumento: R${aum:.2f}')
print(f'Novo salário: R${n_sal:.2f}')
'''
'''
val_h = float(input('Valor da hora: R$'))
qtd_h = int(input('Quantidade de horas: '))
sal_brut = val_h * qtd_h
if sal_brut <= 900:
    porc = 0
elif sal_brut <= 1500:
    porc = 5
elif sal_brut <= 2500:
    porc = 10
else:
    porc = 20
ir = sal_brut * (porc/100)
inss = sal_brut * (10/100)
fgts = sal_brut * (11/100)
tot_desc = ir + inss
sal_liq = sal_brut - tot_desc
print(f'\nSalário Bruto: ({val_h:.2f} * {qtd_h}): R$ {sal_brut:.2f}')
print(f'(-) IR ({porc}%): R$ {ir:.2f}')
print(f'(-) INSS (10%): R$ {inss:.2f}')
print(f'FGTS (11%): R$ {fgts:.2f}')
print(f'Total de descontos: R$ {tot_desc:.2f}')
print(f'Salário Líquido: R$ {sal_liq:.2f}')
'''
'''
num = int(input('Digite um número de 1 a 7: '))
if 7 >= num >= 1:
    match num:
        case 1:
            print('Domingo')
        case 2:
            print('Segunda-feira')
        case 3:
            print('Terça-feira')
        case 4:
            print('Quarta-feira')
        case 5:
            print('Quinta-feira')
        case 6:
            print('Sexta-feira')
        case 7:
            print('Sábado')
else:
    print('Valor inválido!')
'''
'''
n1 = float(input('1º Nota: '))
n2 = float(input('2º Nota: '))
media = (n1 + n2) / 2
if media < 4:
    conc = 'E'
elif media < 6:
    conc = 'D'
elif media < 7.5:
    conc = 'C'
elif media < 9:
    conc = 'B'
else:
    conc = 'A'
print(f'Conceito: {conc}')
'''
'''
ano = int(input('Ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
'''
'''
n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
media = (n1 + n2) / 2
if media >= 10:
    passou = 'Aprovado com Distinção'
elif media >= 7:
    passou = 'Aprovado'
else:
    passou = 'Reprovado'
print(f'{passou}  {media:.2f}')
'''
'''
exc = 0
peso = float(input('Peso de peixes: '))
if peso > 50:
    exc = peso - 50
multa = exc * 4
print(f'Excesso: {exc} Kg')
print(f'Multa: R$ {multa:.2f}')
'''
'''
notas = [100, 50, 10, 5, 1]
saq = float(input('Valor do saque: R$ '))
if 600 >= saq >= 10:
    for nota in notas:
        qtd = int(saq // nota)
        if qtd > 0:
            print(f'{qtd} nota(s) de R$ {nota:.2f}')
        saq %= nota
else:
    print('Valor inválido')
'''
'''
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
             "Devia para a vítima?", "Já trabalhou com a vítima?" ]
cont = 0
for pergunta in perguntas:
    print(pergunta)
    resp = str(input()).upper()
    if 'S' in resp:
        cont += 1
if cont == 5:
    print('Assassino')
elif cont == 3 or cont == 4:
    print('Cúmplice')
elif cont == 2:
    print('Suspeita')
else:
    print('Inocente ')
'''
'''
num_l = float(input('Litros vendidos: '))
tip_com = str(input('Tipo de combustível [A/G]: ')).upper()
if 'A' in tip_com:
    preco_l = 1.90
    if num_l <= 20:
        desc = 3
    else:
        desc = 5
elif 'G' in tip_com:
    preco_l = 2.50
    if num_l <= 20:
        desc = 4
    else:
        desc = 6
else:
    print('Opção inválida')
    exit()
preco_bruto = num_l * preco_l
val_desc = preco_bruto * (desc / 100)
val_final = preco_bruto - val_desc
print(f'Valor a ser pago: R$ {val_final:.2f}')
'''
'''
kg_mor = int(input('Quantidade (em Kg) de morangos: '))
kg_mac = int(input('Quantidade (em Kg) de maçãs: '))
if kg_mor <= 5:
    preco_kg_mor = 2.50
else:
    preco_kg_mor = 2.20
if kg_mac <= 5:
    preco_kg_mac = 1.80
else:
    preco_kg_mac = 1.50
preco_mor = kg_mor * preco_kg_mor
preco_mac = kg_mac * preco_kg_mac
tot_preco = preco_mor + preco_mac
tot_kg = kg_mor + kg_mac
if tot_kg > 8 or tot_preco > 25:
    desc = 10
val_desc = tot_preco * (desc / 100)
val_pagar = tot_preco - val_desc
print(f'Pagar: R$ {val_pagar:.2f}')
'''
'''
tip = str(input('Qual carne [F/A/P]? ')).upper()
kg = int(input('Quantidade (em Kg): '))
pag = str(input('Forma de pagamento [CT/D]: ')).upper()
if 'F' in tip:
    if kg <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
elif 'A' in tip:
    if kg <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
elif 'P' in tip:
    if kg <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80
else:
    print('Opção inválida')
    exit()
if 'CT' in pag:
    desc = 5
elif 'D' in pag:
    desc = 0
else:
    print('Opção inválida')
    exit()
tot_preco = kg * preco_kg
val_desc = tot_preco * (desc / 100)
val_pag = tot_preco - val_desc
print(f'\nTipo: {tip}')
print(f'Quantidade: {kg} Kg')
print(f'Preço total: R$ {tot_preco:.2f}')
print(f'Tipo de pagamento: {pag}')
print(f'Valor do desconto: R$ {val_desc:.2f}')
print(f'Valor a pagar: R$ {val_pag:.2f}')
'''
area = float(input("Informe o tamanho da área a ser pintada em m²: "))

litros_tinta = area / 6
litros_folga = litros_tinta * 1.1
galoes = 0
latas = litros_folga // 18
tinta_faltante = litros_folga - 18 * latas

if tinta_faltante > 0:
    if tinta_faltante % 3.6 > 0:
        faltante_galoes = tinta_faltante // 3.6 + 1
    else:
        faltante_galoes = tinta_faltante // 3.6
    if faltante_galoes <= 3:
        galoes = faltante_galoes
    else:
        galoes = 0
        latas = latas + 1

preco = latas * 80 + galoes * 25

print(f'São necessários {int(latas)} latas e {int(galoes)} galões. '
      f'Custando R$ {preco:.2f} no total')
