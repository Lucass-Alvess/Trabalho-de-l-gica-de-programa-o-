print("Bem-vindo à Loja de Gelados do Lucas Oliveira")

#Exibe o cardápio
print("------------------------------------------------------------")
print("-----------------------------Cardápio-----------------------")
print("------------------------------------------------------------")
print("| Tamanho | Cupuaçu (CP) | Açaí (AC)  |")
print("|---------|--------------|------------|")
print("|    P    |   R$ 9.00    |  R$ 11.00  |")
print("|    M    |  R$ 14.00    |  R$ 16.00  |")
print("|    G    |  R$ 18.00    |  R$ 20.00  |")
print("------------------------------------------------------------")

#Acumulador de pedidos
total_pedido = 0

#Entrada do sabor com validação
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
    if sabor != 'CP' and sabor != 'AC':
        print("Sabor inválido. Tente novamente")
        continue

    #Entrada do tamanho com validação
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print("Tamanho inválido. Tente novamente")
        continue

    #Determinar o preço
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9.00
        elif tamanho == 'M':
            preco = 14.00
        else:
            preco = 18.00
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11.00
        elif tamanho == 'M':
            preco = 16.00
        else:
            preco = 20.00

    # Mostra o pedido e valor
    nome_sabor = "Cupuaçu" if sabor == 'CP' else "Açaí"
    print(f"Você pediu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}")

    # Soma ao total
    total_pedido += preco

    # Pergunta se quer pedir mais
    mais = input("Deseja mais alguma coisa? (S/N): ").upper()
    if mais != 'S':
        break 

# Exibe o total da compra
print(f"\nValor total a ser pago: R$ {total_pedido:.2f}")
