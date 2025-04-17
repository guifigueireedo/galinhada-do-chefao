# relatorios.py
from mesas_pedidos import pedidos
from cozinha import cardapio

def menu_relatorios():
    print("\n=== RELATÓRIOS ===")
    total_vendas = {}
    total_valor = 0
    mesas_set = set()

    for mesa, pedido in pedidos:
        nome = cardapio[pedido["prato"]]["nome"]
        preco = cardapio[pedido["prato"]]["preco"]
        total_valor += preco
        mesas_set.add(mesa)
        if nome not in total_vendas:
            total_vendas[nome] = 0
        total_vendas[nome] += 1

    print(f"Total de vendas: R$ {total_valor:.2f}")
    print(f"Média por mesa: R$ {total_valor/len(mesas_set) if mesas_set else 0:.2f}")
    print("Itens mais vendidos:")
    for item, qtd in sorted(total_vendas.items(), key=lambda x: x[1], reverse=True):
        print(f" - {item}: {qtd} vendido(s)")
    print()
