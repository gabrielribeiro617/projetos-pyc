meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
'''
tot = 0
tot_met = 0
for item in vendas:
    if item[1] >= meta:
        tot_met += item[1]
    tot += item[1]
porc = (tot_met / tot) * 100
print(f'{porc:.2f}% dos vendedores bateram a meta.')
'''
'''
vend_met = []
tot = 0
for item in vendas:
    if item[1] >= meta:
        vend_met.append(item[1])
    tot += item[1]
porc = (sum(vend_met) / tot) * 100
print(f'{porc:.2f}% dos vendedores bateram a meta.')
'''

so_vend = []
for item in vendas:
    so_vend.append(item[1])
i_mai = so_vend.index(max(so_vend))
print(f'{vendas[i_mai][0]} foi o vendedor que mais vendeu {max(so_vend)}')
