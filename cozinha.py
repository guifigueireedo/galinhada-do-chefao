from estoque import estoque

cardapio = {}
receitas = {}

def cadastrar_item_cardapio():
    codigo = input("Código do prato: ")
    nome = input("Nome do prato: ")
    descricao = input("Descrição do prato: ")
    preco = float(input("Preço: R$ "))

    cardapio[codigo] = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco
    }

    receitas[codigo] = {}
    print("Agora vamos cadastrar os ingredientes da receita.")
    while True:
        cod_ingrediente = input("Código do ingrediente (ou 0 pra sair): ")
        if cod_ingrediente == "0":
            break
        if cod_ingrediente not in estoque:
            print("Ingrediente não encontrado no estoque!")
            continue
        qtd = float(input(f"Quantidade necessária de '{estoque[cod_ingrediente]['nome']}': "))
        receitas[codigo][cod_ingrediente] = qtd

    print(f"Prato '{nome}' cadastrado com sucesso!\n")

def consultar_cardapio():
    print("\n--- CARDÁPIO ---")
    for codigo, prato in cardapio.items():
        print(f"Código: {codigo} | Nome: {prato['nome']} | Preço: R${prato['preco']:.2f}")
        print(f"Descrição: {prato['descricao']}")
        print("Ingredientes:")
        for ing_cod, qtd in receitas[codigo].items():
            nome = estoque[ing_cod]["nome"] if ing_cod in estoque else "Desconhecido"
            print(f"- {nome}: {qtd} {estoque[ing_cod]['unidade'] if ing_cod in estoque else ''}")
        print()
    print()

def verificar_ingredientes_disponiveis(codigo_prato):
    if codigo_prato not in receitas:
        print("Receita não encontrada.")
        return False

    ingredientes = receitas[codigo_prato]
    for cod_ingrediente, qtd_necessaria in ingredientes.items():
        if cod_ingrediente not in estoque:
            print(f"Ingrediente '{cod_ingrediente}' não está no estoque.")
            return False
        if estoque[cod_ingrediente]["quantidade"] < qtd_necessaria:
            print(f"Ingrediente '{estoque[cod_ingrediente]['nome']}' insuficiente.")
            return False
    return True

def menu_cozinha():
    while True:
        print("\n=== GESTÃO DA COZINHA ===")
        print("1. Cadastrar Item no Cardápio")
        print("2. Consultar Cardápio")
        print("3. Verificar Ingredientes de um Prato")
        print("0. Voltar ao menu principal")
        op = input("Escolha uma opção: ")

        if op == "1":
            cadastrar_item_cardapio()
        elif op == "2":
            consultar_cardapio()
        elif op == "3":
            cod = input("Código do prato: ")
            disponivel = verificar_ingredientes_disponiveis(cod)
            if disponivel:
                print("Todos os ingredientes estão disponíveis!")
            else:
                print("Ingredientes insuficientes ou ausentes.")
        elif op == "0":
            break
        else:
            print("Opção inválida.\n")