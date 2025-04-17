from estoque import menu_estoque
from cozinha import menu_cozinha
from mesas_pedidos import menu_mesas
from pagamentos import menu_pagamentos
from relatorios import menu_relatorios

def menu_principal():
    while True:
        print("\n=== GALINHADA DO CHEFÃO ===")
        print("1. Gestão de Estoque")
        print("2. Gestão da Cozinha")
        print("3. Gestão de Mesas e Pedidos")
        print("4. Gestão de Pagamentos")
        print("5. Relatórios")
        print("0. Sair")
        op = input("Escolha uma opção: ")

        if op == "1":
            menu_estoque()
        elif op == "2":
            menu_cozinha()
        elif op == "3":
            menu_mesas()
        elif op == "4":
            menu_pagamentos()
        elif op == "5":
            menu_relatorios()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu_principal()