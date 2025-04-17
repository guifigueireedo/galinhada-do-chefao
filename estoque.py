# estoque.py com suporte a lotes
import datetime

estoque = {}

def cadastrar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    unidade = input("Unidade de medida (ex: kg, un, L): ")
    preco = float(input("Preço unitário: R$ "))

    if codigo not in estoque:
        estoque[codigo] = {
            "nome": nome,
            "unidade": unidade,
            "preco": preco,
            "lotes": []  # lista de dicionários
        }

    qtd = int(input("Quantidade: "))
    validade = input("Data de validade (AAAA-MM-DD): ")
    estoque[codigo]["lotes"].append({
        "quantidade": qtd,
        "validade": validade
    })

    print(f"Lote de '{nome}' cadastrado com sucesso!\n")

def consultar_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for codigo, produto in estoque.items():
        print(f"Produto: {produto['nome']} ({codigo}) | Unidade: {produto['unidade']} | Preço: R$ {produto['preco']}")
        for idx, lote in enumerate(produto["lotes"], start=1):
            print(f"  Lote {idx}: {lote['quantidade']} {produto['unidade']} | Validade: {lote['validade']}")
    print()

def atualizar_estoque():
    codigo = input("Código do produto a atualizar: ")
    if codigo in estoque:
        consultar_estoque()
        indice = int(input("Digite o número do lote que deseja atualizar: ")) - 1
        if 0 <= indice < len(estoque[codigo]["lotes"]):
            nova_qtd = int(input("Nova quantidade: "))
            estoque[codigo]["lotes"][indice]["quantidade"] = nova_qtd
            print("Lote atualizado!\n")
        else:
            print("Índice de lote inválido.\n")
    else:
        print("Produto não encontrado.\n")

def alertas_estoque():
    print("\n--- ALERTAS ---")
    hoje = datetime.date.today()
    for codigo, produto in estoque.items():
        for idx, lote in enumerate(produto["lotes"], start=1):
            validade = datetime.datetime.strptime(lote["validade"], "%Y-%m-%d").date()
            if lote["quantidade"] <= 3:
                print(f"Produto '{produto['nome']}', Lote {idx} com estoque baixo (Qtd: {lote['quantidade']})")
            if (validade - hoje).days <= 3:
                print(f"Produto '{produto['nome']}', Lote {idx} perto do vencimento! (Vence em {lote['validade']})")
    print()

def menu_estoque():
    while True:
        print("1. Cadastrar Produto")
        print("2. Consultar Estoque")
        print("3. Atualizar Estoque")
        print("4. Ver Alertas")
        print("0. Voltar ao menu principal")
        op = input("Escolha uma opção: ")

        if op == "1":
            cadastrar_produto()
        elif op == "2":
            consultar_estoque()
        elif op == "3":
            atualizar_estoque()
        elif op == "4":
            alertas_estoque()
        elif op == "0":
            break
        else:
            print("Opção inválida. Tente novamente.\n")