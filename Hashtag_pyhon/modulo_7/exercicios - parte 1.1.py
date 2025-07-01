"""## 3. Cadastro de e-mails

- A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em
cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o
e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois
do '@' tem algum ponto, afinal:

- liragmail.com NÃO é um e-mail válido
- lira@gmail NÃO é um e-mail válido
- lira@gmail.com é um e-mail válido

Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de
inputs) e que verifique:
1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher
todos os dados corretamente
2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele
deve exibir uma mensagem de e-mail inválido

Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode
testar o que ele dá como resposta caso ele não encontre um item dentro da string
"""
while True:
    print('--' * 20)
    nome = str(input('Nome: ')).strip().title()
    if not all(parte.isalpha() for parte in nome.split()):
        print('Preecha corretamente o campo')
        input('Pressione Enter para continuar...')
        continue
    email = str(input('E-mail: ')).strip()
    if '@' not in email or '.' not in email.split('@')[-1]:
        print('E-mail inválido')
        input('Pressione Enter para continuar...')
        continue
    else:
        break
print('E-mail válido')
