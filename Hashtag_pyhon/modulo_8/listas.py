# Exercício 1
# Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve:
# - Pegar o usuário qual produto vai ser cadastrado por meio de um input
# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua
# sendo o mesmo produto
# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a
# mensagem "Produto já existente, tente novamente"
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na
# lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa
'''
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
prod = str(input('Produto: ')).casefold()
if prod in produtos:
    print(f'O produto {prod} já está na lista. Tente novamente')
    exit()
else:
    produtos.append(prod)
    print(f'Produto {prod} cadastrado com succeso')
    print(produtos)
'''

# Exercício 2
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do
# produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem
# para o usuário tentar novamente
'''
produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]
prod = str(input('Produto: ')).casefold()
if prod in produtos:
    i_prod = produtos.index(prod)
    preco_prod = precos[i_prod]
    print(f'O produto {prod} custa R$ {preco_prod}')
else:
    print(f'O produto {prod} não está na lista. Tente novamente')
    exit()
'''
# Exercício 3
# Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para
#       cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para
#       cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
# - Printar no final o valor do bônus do funcionário
'''
val_vend = float(input('Valor de vendas do funcionario: '))
if val_vend > 5000:
    bonus = (2 * val_vend) + 1000
elif val_vend > 1000:
    bonus = 2 * val_vend
else:
    bonus = val_vend
print(f'Bônus do fundionário: R$ {bonus:.2f}')
'''
# Exercício 4
# Crie um programa que consiga descobrir qual dos vendedores vendeu mais
# As vendas dos vendedores são listas com a quantidade vendida por cada vendedor

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]

vend_1 = sum(vendas[0])
vend_2 = sum(vendas[1])
mai = vend_1
if vend_2 > mai:
    mai = vend_2
    print(f'O venderor 2 vendeu mais: R$ {vend_2:.2f}')
else:
    print(f'O vendedor 1 vendeu mais: R$ {vend_1:.2f}')

