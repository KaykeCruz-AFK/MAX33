push = lambda pilha, item: pilha.append(item)
pop = lambda pilha: pilha.pop() if pilha else None
is_empty = lambda pilha: len(pilha) == 0

carrinho = []

print("=== Carrinho de Compras ===")

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover último item")
    print("3 - Mostrar carrinho")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        produto = input("Produto: ")
        qtd = int(input("Quantidade: "))
        preco = float(input("Preço unitário: R$ "))
        push(carrinho, [produto, qtd, preco])
        print(f"{produto} adicionado.")

    elif opcao == '2':
        removido = pop(carrinho)
        if removido:
            print(f"Removido: {removido[0]}")
        else:
            print("Carrinho vazio.")

    elif opcao == '3':
        if is_empty(carrinho):
            print("Carrinho vazio.")
        else:
            print("\nProduto       Quantidade    Preço Unitário    Total")
            total_geral = 0
            for prod, qtd, preco in carrinho:
                total = qtd * preco
                total_geral += total
                print(f"{prod:<13} {qtd:<12} R${preco:<15.2f} R${total:.2f}")
            print(f"Total geral: R${total_geral:.2f}")

    elif opcao == '0':
        break

    else:
        print("Opção inválida.")

print("\nObrigado!")
