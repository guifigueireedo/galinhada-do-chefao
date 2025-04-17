from cozinha import cardapio, verificar_ingredientes_disponiveis, receitas
from estoque import estoque
pedidos = []
mesas = {}

def cadastrar_mesa():
    numero = input("Número da mesa: ")
    capacidade = input("Capacidade da mesa: ")
    status = "livre"
    mesas[numero] = {"capacidade": capacidade, "status": status, "clientes": [], "pedidos": []}
    print("Mesa cadastrada!\n")

def atribuir_cliente():
    numero = input("Número da mesa: ")
    nome_cliente = input("Nome do cliente: ")
    if numero in mesas and mesas[numero]["status"] == "livre":
        mesas[numero]["clientes"].append(nome_cliente)
        mesas[numero]["status"] = "ocupada"
        print("Cliente atribuído com sucesso!\n")
    else:
        print("Mesa não encontrada ou ocupada.\n")

def fazer_pedido():
    numero = input("Número da mesa: ")
    if numero not in mesas or mesas[numero]["status"] != "ocupada":
        print("Mesa inválida ou não ocupada.\n")
        return

    while True:
        cod_prato = input("Código do prato (ou 0 para encerrar): ")
        if cod_prato == "0":
            break
        if cod_prato not in cardapio:
            print("Prato não encontrado.\n")
            continue
        if not verificar_ingredientes_disponiveis(cod_prato):
            print("Ingredientes insuficientes para esse prato.\n")
            continue

        for cod_ing, qtd in receitas[cod_prato].items():
            estoque[cod_ing]["quantidade"] -= qtd

        pedido = {"prato": cod_prato, "status": "solicitado"}
        mesas[numero]["pedidos"].append(pedido)
        pedidos.append((numero, pedido))
        print(f"Pedido de '{cardapio[cod_prato]['nome']}' registrado para a mesa {numero}.\n")

def consultar_mesas():
    for numero, mesa in mesas.items():
        print(f"Mesa {numero} | Capacidade: {mesa['capacidade']} | Status: {mesa['status']} | Clientes: {mesa['clientes']}")
        for p in mesa["pedidos"]:
            print(f"  Pedido: {cardapio[p['prato']]['nome']} | Status: {p['status']}")
    print()

def atualizar_status_pedidos():
    print("\n--- ATUALIZAR STATUS DOS PEDIDOS ---")
    for numero, mesa in mesas.items():
        for idx, pedido in enumerate(mesa["pedidos"]):
            nome_prato = cardapio[pedido["prato"]]["nome"]
            status = pedido["status"]
            print(f"{numero}-{idx}: {nome_prato} | Status: {status}")

    selecao = input("Digite o código do pedido (mesa-índice) ou 0 para voltar: ")
    if selecao == "0":
        return

    try:
        mesa_num, index = selecao.split("-")
        index = int(index)
        pedido = mesas[mesa_num]["pedidos"][index]
        status_atual = pedido["status"]

        print(f"Status atual: {status_atual}")
        print("1. Receber pedido (vai para 'recebido')")
        print("2. Iniciar preparo (vai para 'em preparo')")
        print("3. Marcar como entregue")

        opcao = input("Escolha a nova etapa: ")

        if opcao == "1" and status_atual == "solicitado":
            pedido["status"] = "recebido"
        elif opcao == "2" and status_atual == "recebido":
            pedido["status"] = "em preparo"
        elif opcao == "3" and status_atual == "em preparo":
            pedido["status"] = "entregue"
        else:
            print("Transição de status inválida.")
    except:
        print("Entrada inválida.")

def menu_mesas():
    while True:
        print("\n=== GESTÃO DE MESAS E PEDIDOS ===")
        print("1. Cadastrar Mesa")
        print("2. Atribuir Cliente à Mesa")
        print("3. Fazer Pedido")
        print("4. Consultar Mesas")
        print("5. Atualizar status dos pedidos")
        print("0. Voltar")
        op = input("Escolha uma opção: ")
        if op == "1":
            cadastrar_mesa()
        elif op == "2":
            atribuir_cliente()
        elif op == "3":
            fazer_pedido()
        elif op == "4":
            consultar_mesas()
        elif op == "5":
            atualizar_status_pedidos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
