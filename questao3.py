print("Bem-vindo à Copiadora do Lucas Oliveira")

# Função para escolher o tipo de serviço
def escolha_servico():
    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input(">> ").upper()

        # Verificação de entrada
        if servico == "DIG":
            return 1.10
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")

# Função para ler número de páginas com validação e aplicar desconto
def num_pagina():
    while True:
        try:
            paginas = int(input("\nEntre com o número de páginas: "))
            if paginas < 20:
                return paginas
            elif 20 <= paginas < 200:
                return paginas * 0.85  # 15% de desconto
            elif 200 <= paginas < 2000:
                return paginas * 0.80  # 20% de desconto
            elif 2000 <= paginas < 20000:
                return paginas * 0.75  # 25% de desconto
            else:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

# Função para escolher serviço extra
def servico_extra():
    while True:
        print("\nDeseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        opcao = input(">> ")

        if opcao == "1":
            return 15.00
        elif opcao == "2":
            return 40.00
        elif opcao == "0":
            return 0.00
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Parte principal do programa 
try:
    valor_servico = escolha_servico()               # Escolhe o serviço
    paginas_com_desconto = num_pagina()             # Lê e aplica desconto nas páginas
    valor_extra = servico_extra()                   # Escolhe adicional

    total = (valor_servico * paginas_com_desconto) + valor_extra

    # Exibe resumo da compra
    print(f"\nTotal: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {paginas_com_desconto:.0f} + extra: {valor_extra:.2f})")

except Exception as erro:
    print("Ocorreu um erro inesperado:", erro)
