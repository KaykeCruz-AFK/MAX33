carrinho = []

carrinho.append(["Arroz", 2, 5.50])
carrinho.append(["Feijão", 1, 7.30])
carrinho.append(["Macarrão", 3, 4.20])


print("Carrinho de compras:")
print("Produto     Quantidade    Preço Unitário    Total")
for item in carrinho:
    produto, quantidade, preco = item
    total = quantidade * preco
    print(f"{produto:<12} {quantidade:<12} R${preco:<15.2f} R${total:.2f}")


if carrinho:
    removido = carrinho.pop()
    print(f"\nProduto removido: {removido[0]}")
else:
    print("\nCarrinho vazio, nada para remover.")


print("\nCarrinho atualizado:")
print("Produto     Quantidade    Preço Unitário    Total")
for item in carrinho:
    produto, quantidade, preco = item
    total = quantidade * preco
    print(f"{produto:<12} {quantidade:<12} R${preco:<15.2f} R${total:.2f}")
