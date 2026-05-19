import json
import os


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

def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)


def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)


def CadastrarCarro(Modelo, Marca):

    carros = carregar_dados('Carros.json')

    carros[Modelo] = Marca

    salvar_dados('Carros.json', carros)

    print("Carro cadastrado com sucesso!")


def CadastrarCliente(CPF, Nome):

    clientes = carregar_dados('Clientes.json')

    clientes[CPF] = Nome

    salvar_dados('Clientes.json', clientes)

    print("Cliente cadastrado com sucesso!")


def CadastrarFuncionario(Idfuncionario, Nome):

    funcionarios = carregar_dados('funcionarios.json')

    funcionarios[Idfuncionario] = Nome

    salvar_dados('funcionarios.json', funcionarios)

    print("Funcionário cadastrado com sucesso!")


def Vendas(Vendedor, Cliente, Carro):

    vendas = carregar_dados('Vendas.json')

    id_venda = str(len(vendas) + 1)

    vendas[id_venda] = {
        "Vendedor": Vendedor,
        "Cliente": Cliente,
        "Carro": Carro
    }

    salvar_dados('Vendas.json', vendas)

    print("Venda registrada com sucesso!")


Func = int(input(
    'Informe o que deseja usar\n'
    'Para cadastrar um carro digite "1"\n'
    'Para cadastrar um funcionário digite "2"\n'
    'Para cadastrar um cliente digite "3"\n'
    'Para realizar uma venda digite "4"\n'
    'Entrada do usuario: '
))

if Func == 1:

    CadastrarCarro(
        input("Qual o modelo do veículo? "),
        input("Qual a marca do carro? ")
    )

elif Func == 2:

    CadastrarFuncionario(
        input("Qual ID do funcionário? "),
        input("Qual o nome do funcionário? ")
    )

elif Func == 3:

    CadastrarCliente(
        input("Qual o CPF do cliente? "),
        input("Qual o nome do cliente? ")
    )

elif Func == 4:

    carros = carregar_dados('Carros.json')
    clientes = carregar_dados('Clientes.json')
    funcionarios = carregar_dados('funcionarios.json')

    print("\n=== FUNCIONÁRIOS ===")
    print(json.dumps(funcionarios, indent=4))

    print("\n=== CLIENTES ===")
    print(json.dumps(clientes, indent=4))

    print("\n=== CARROS ===")
    print(json.dumps(carros, indent=4))

    Vendas(
        input("\nQual o vendedor? "),
        input("Qual o cliente? "),
        input("Qual o carro vendido? ")
    )
else:
    print("Opção inválida!")