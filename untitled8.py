print("=== Métodos de Pagamento de Transporte ===")
metodos_disponiveis = ["Dinheiro", "Cartão de Crédito", "Pix", "Vale Transporte"]
valor_passagem = 8.50

for i in range(len(metodos_disponiveis)):
    print(f"{i + 1}. {metodos_disponiveis[i]}")

try:
    escolha = int(input("Escolha o método de pagamento (1-4): "))
    if escolha < 1 or escolha > 4:
        print("Opção inválida.")
    else:
        metodo_escolhido = metodos_disponiveis[escolha - 1]
        quantidade = int(input("Quantas passagens deseja pagar? "))
        fila_pagamentos = []

        tipo_pagamento = "À vista"
        parcelas = 1

        if metodo_escolhido == "Cartão de Crédito":
            print("Você deseja:")
            print("1. Pagar à vista")
            print("2. Parcelar")
            escolha_cartao = int(input("Escolha uma opção (1 ou 2): "))
            if escolha_cartao == 2:
                parcelas = int(input("Em quantas parcelas deseja dividir? "))
                tipo_pagamento = f"Parcelado em {parcelas}x"
            elif escolha_cartao == 1:
                tipo_pagamento = "À vista"
            else:
                print("Opção inválida. Considerando pagamento à vista.")

        for i in range(quantidade):
            pagamento = {
                "metodo": metodo_escolhido,
                "valor": valor_passagem,
                "transacao": i + 1,
                "tipo_pagamento": tipo_pagamento,
                "parcelas": parcelas if tipo_pagamento != "À vista" else None
            }
            fila_pagamentos.append(pagamento)

        print("\n--- Processando Pagamentos ---")
        total_pago = 0
        while len(fila_pagamentos) > 0:
            pagamento = fila_pagamentos.pop(0)
            print(f"Transação #{pagamento['transacao']}: {pagamento['metodo']} - {pagamento['tipo_pagamento']} - R$ {pagamento['valor']:.2f}")
            if pagamento["parcelas"]:
                valor_parcela = pagamento["valor"] / pagamento["parcelas"]
                print(f"    Parcelas de R$ {valor_parcela:.2f} em {pagamento['parcelas']}x")
            total_pago += pagamento["valor"]

        print(f"\nTotal pago: R$ {total_pago:.2f}")

except ValueError:
    print("Entrada inválida. Use apenas números.")
