class Pagamento:
    def __init__(self, tipo, valor, info_extra=None):
        self.tipo = tipo
        self.valor = valor
        self.info_extra = info_extra or {}
        self.status = 'pendente'

        self.processar_cartao = lambda: (
            print(f"Processando cartão {self.info_extra.get('numero_cartao')} em {self.info_extra.get('parcelas',1)} parcelas."),
            setattr(self, 'status', 'aprovado')
        )

        self.processar_boleto = lambda: (
            print(f"Boleto gerado com código: {self.info_extra.get('codigo_barras')}"),
            setattr(self, 'status', 'aguardando pagamento')
        )

        self.processar_pix = lambda: (
            print(f"Solicitando pagamento via Pix para a chave: {self.info_extra.get('chave_pix')}"),
            setattr(self, 'status', 'aprovado')
        )

        funcoes = {
            'cartao': self.processar_cartao,
            'boleto': self.processar_boleto,
            'pix': self.processar_pix
        }

        self.processar = funcoes.get(self.tipo, lambda: print(f"Tipo de pagamento '{self.tipo}' inválido."))

    def __str__(self):
        return f"{self.tipo.capitalize()}: R${self.valor:.2f} - Status: {self.status}"

class PilhaPagamentos:
    def __init__(self):
        self.pilha = []
        self.adicionar_pagamento = lambda pag: (self.pilha.append(pag), print(f"Pagamento adicionado: {pag}"))
        self.processar_todos = lambda: (
            [ (pag.processar(), print(f"Pagamento processado: {pag}")) for pag in iter(lambda: self.pilha.pop() if self.pilha else None, None) ]
        )

pilha = PilhaPagamentos()

while True:
    print("\nEscolha o método de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Boleto")
    print("3 - Pix")
    print("0 - Sair")

    escolha = input("Digite a opção: ")

    if escolha == '0':
        break

    valor = float(input("Digite o valor do pagamento: R$ "))

    if escolha == '1':
        numero_cartao = input("Número do cartão: ")
        parcelas = int(input("Número de parcelas: "))
        pag = Pagamento('cartao', valor, {'numero_cartao': numero_cartao, 'parcelas': parcelas})
    elif escolha == '2':
        codigo_barras = input("Código de barras do boleto: ")
        pag = Pagamento('boleto', valor, {'codigo_barras': codigo_barras})
    elif escolha == '3':
        chave_pix = input("Chave Pix: ")
        pag = Pagamento('pix', valor, {'chave_pix': chave_pix})
    else:
        print("Opção inválida.")
        continue

    pilha.adicionar_pagamento(pag)

print("\nProcessando pagamentos...")
pilha.processar_todos()
print("Todos os pagamentos foram processados!")
