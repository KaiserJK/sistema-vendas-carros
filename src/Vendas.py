import json
import os


# Cria os arquivos JSON caso não existam
def criar_arquivos_json():

    arquivos = [
        "Carros.json",
        "Clientes.json",
        "funcionarios.json",
        "Vendas.json"
    ]

    for arquivo in arquivos:

        if not os.path.exists(arquivo):

            with open(arquivo, "w") as f:

                json.dump({}, f, indent=4)


criar_arquivos_json()


# Carrega os dados do JSON
def carregar_dados(arquivo):

    with open(arquivo, 'r') as f:

        return json.load(f)


# Salva dados no JSON
def salvar_dados(arquivo, dados):

    with open(arquivo, 'w') as f:

        json.dump(dados, f, indent=4)


# Cadastro de carros
def CadastrarCarro(Modelo, Marca):

    carros = carregar_dados('Carros.json')

    carros[Modelo] = Marca

    salvar_dados('Carros.json', carros)

    print("Carro cadastrado com sucesso!")


# Cadastro de clientes
def CadastrarCliente(CPF, Nome):

    clientes = carregar_dados('Clientes.json')

    clientes[CPF] = Nome

    salvar_dados('Clientes.json', clientes)

    print("Cliente cadastrado com sucesso!")


# Cadastro de funcionários
def CadastrarFuncionario(Idfuncionario, Nome):

    funcionarios = carregar_dados('funcionarios.json')

    funcionarios[Idfuncionario] = Nome

    salvar_dados('funcionarios.json', funcionarios)

    print("Funcionário cadastrado com sucesso!")


# Registra vendas e remove carro do estoque
def Vendas():

    funcionarios = carregar_dados('funcionarios.json')
    clientes = carregar_dados('Clientes.json')
    carros = carregar_dados('Carros.json')
    vendas = carregar_dados('Vendas.json')

    # Mostra os dados cadastrados
    print("\n=== FUNCIONÁRIOS ===")
    print(json.dumps(funcionarios, indent=4))

    print("\n=== CLIENTES ===")
    print(json.dumps(clientes, indent=4))

    print("\n=== CARROS ===")
    print(json.dumps(carros, indent=4))

    vendedor = input("\nQual o vendedor? ")
    cliente = input("Qual o cliente? ")
    carro = input("Qual o carro vendido? ")

    # Verifica se o carro existe
    if carro not in carros:

        print("Carro não encontrado!")
        return

    # Cria ID automático da venda
    id_venda = str(len(vendas) + 1)

    # Registra a venda
    vendas[id_venda] = {
        "Vendedor": vendedor,
        "Cliente": cliente,
        "Carro": carro
    }

    # Remove carro vendido
    del carros[carro]

    salvar_dados('Vendas.json', vendas)
    salvar_dados('Carros.json', carros)

    print("Venda registrada com sucesso!")
    print("Carro removido do estoque!")


# Menu principal
Func = int(input(
    'Informe o que deseja usar\n'
    'Para cadastrar um carro digite "1"\n'
    'Para cadastrar um funcionário digite "2"\n'
    'Para cadastrar um cliente digite "3"\n'
    'Para realizar uma venda digite "4"\n'
    'Entrada do usuario: '
))


# Cadastro de carros
if Func == 1:

    CadastrarCarro(
        input("Qual o modelo do veículo? "),
        input("Qual a marca do carro? ")
    )


# Cadastro de funcionários
elif Func == 2:

    CadastrarFuncionario(
        input("Qual ID do funcionário? "),
        input("Qual o nome do funcionário? ")
    )


# Cadastro de clientes
elif Func == 3:

    CadastrarCliente(
        input("Qual o CPF do cliente? "),
        input("Qual o nome do cliente? ")
    )


# Registro de vendas
elif Func == 4:

    Vendas()


# Opção inválida
else:

    print("Opção inválida!")