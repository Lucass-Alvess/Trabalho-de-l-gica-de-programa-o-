print('Bem-vindo à Loja do Lucas Oliveira')

# Entrada de dados: valor 
valor_produto = float(input('Entre com o valor do produto: '))
quantidade_produto = int(input('Entre com a quantidade do produto: '))

# Cálculo do valor total sem desconto
valor_total = valor_produto * quantidade_produto

# Cálculo do desconto 
if valor_total < 2500:
    desconto = 0  # Sem desconto
elif valor_total >= 2500 and valor_total < 6000:
    desconto = 0.04  # 4% de desconto
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 0.07  # 7% de desconto
else:
    desconto = 0.11  # 11% de desconto

# Cálculo do valor com desconto
valor_com_desconto = valor_total * (1 - desconto)

# Impressão dos valores totais
print(f'Valor Sem desconto: R$ {valor_total:.2f}')
print(f'Valor Com desconto: R$ {valor_com_desconto:.2f}')

