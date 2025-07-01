import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' CONTROLE DE ESTOQUE '.center(40, '-'))

    nome = str(input('Nome: ')).strip().title()
    cat = str(input('Categoria: ')).strip().title()

    try:
        qtd = int(input('Quantidade atual: '))
    except ValueError:
        continue

    if not nome or not cat:
        continue

    break

if 'Alimentos' in cat:
    if qtd < 50:
        print(f'Solicitar {nome} à equipe de compras'
              f'\nTemos apenas {qtd} em estitoque')

if 'Bebidas' in cat:
    if qtd < 75:
        print(f'Solicitar {nome} à equipe de compras'
              f'\nTemos apenas {qtd} em estitoque')

if 'Limpeza' in cat:
    if qtd < 30:
        print(f'Solicitar {nome} à equipe de compras'
              f'\nTemos apenas {qtd} em estitoque')
