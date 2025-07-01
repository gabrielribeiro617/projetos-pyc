'''
print('Compara duas strings')
str1 = str(input('String 1: ')).strip()
str2 = str(input('String 2: ')).strip()
print(f'Tamanho de {str1}: {len(str1)} caracteres')
print(f'Tamanho de {str2}: {len(str2)} caracteres')
if len(str1) != len(str2):
    print('As duas strings são de tamanhos diferentes.')
else:
    print('As duas strings são do mesmo tamanho.')
if str2 != str1:
    print('As duas strings possuem conteúdo diferente.')
else:
    print('As duas strings possuem conteúdo igual.')
'''

print('Valida e corrige número de telefone')
tel = str(input('Telefone: ')).strip()
tel_fmt = tel.replace('-', '')
if len(tel_fmt) == 7:
    print(f'Telefone possui {len(tel_fmt)} digitos. Vou acrescentar o digito três na frente.')
    print(f'Telefone corrigido sem formatação: {'3' + tel}')
    print(f'Telefone corrigido com formatação: {'3' + tel_fmt}')
else:
    print('O telefone não tem 7 digitos.')
