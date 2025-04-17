# pagamentos.py
from mesas_pedidos import mesas
from cozinha import cardapio

def menu_pagamentos():
    numero = input("Número da mesa para pagamento: ")
    if numero not in mesas or mesas[numero]["status"] != "ocupada":
        print("Mesa inválida ou não ocupada.\n")
        return

    total = 0
    for pedido in mesas[numero]["pedidos"]:
        prato = cardapio[pedido["prato"]]
        total += prato["preco"]

    print(f"Subtotal: R$ {total:.2f}")
    taxa = input("Aplicar taxa de serviço de 10%? (s/n): ")
    if taxa.lower() == "s":
        total *= 1.10

    desconto = input("Aplicar desconto (em %)? (ex: 10): ")
    if desconto.isdigit():
        total *= (1 - int(desconto)/100)

    print(f"Total final: R$ {total:.2f}")
    pagamento = input("Forma de pagamento (dinheiro/cartão): ").strip().lower()
    if pagamento == "dinheiro":
        valor = float(input("Valor pago: R$ "))
        if valor < total:
            print("Valor insuficiente para pagar a conta. Pagamento cancelado.\n")
            return
        troco = valor - total
        print(f"Troco: R$ {troco:.2f}")
    else:
        print("Pagamento registrado no cartão.")

    mesas[numero]["status"] = "livre"
    mesas[numero]["clientes"] = []
    mesas[numero]["pedidos"] = []
    print("Mesa fechada com sucesso!\n")
