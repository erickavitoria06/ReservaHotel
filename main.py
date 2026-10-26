from datetime import datetime
from models import Cliente, QuartoSolteiro, QuartoCasal, Suite, Reserva

def exibir_menu():
    print("      SISTEMA DE RESERVAS DE HOTEL     ")
    print("1. Cadastrar Cliente")
    print("2. Listar Quartos Disponíveis")
    print("3. Realizar Reserva")
    print("4. Listar Reservas Ativas")
    print("5. Sair")

def cadastrar_cliente(clientes):
    print("\n CADASTRO DE CLIENTE ")
    nome = input("Nome completo: ")
    documento = input("Documento (CPF): ")
    contato = input("Telefone/Contato: ")
    
    novo_cliente = Cliente(nome, documento, contato)
    clientes.append(novo_cliente)
    print(f"Sucesso! Cliente {nome} cadastrado.")

def listar_quartos(quartos):
    print("\n LISTA DE QUARTOS ")
    for quarto in quartos:
        print(quarto)

def realizar_reserva(clientes, quartos, reservas):
    print("\n REALIZAR RESERVA ")
    if not clientes:
        print("Aviso: Cadastre um cliente primeiro.")
        return

    doc_cliente = input("Digite o CPF do cliente: ")
    cliente_encontrado = next((c for c in clientes if c.documento == doc_cliente), None)

    if not cliente_encontrado:
        print("Erro: Cliente não encontrado.")
        return

    quartos_disponiveis = [q for q in quartos if q.status == "Disponível"]
    if not quartos_disponiveis:
        print("Desculpe, não há quartos disponíveis.")
        return

    print("\nQuartos disponíveis:")
    for q in quartos_disponiveis:
        print(q)

    # Tratamento de exceções para conversão de números e datas
    try:
        num_quarto = int(input("\nDigite o número do quarto desejado: "))
        quarto_encontrado = next((q for q in quartos if q.numero == num_quarto and q.status == "Disponível"), None)

        if not quarto_encontrado:
            print("Erro: Quarto inválido ou já ocupado.")
            return

        str_inicio = input("Data de Check-in (DD/MM/AAAA): ")
        str_fim = input("Data de Check-out (DD/MM/AAAA): ")

        # Uso da biblioteca datetime para validação e conversão de datas
        data_inicio = datetime.strptime(str_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(str_fim, "%d/%m/%Y")

        if data_inicio >= data_fim:
            print("Erro: A data de check-out deve ser posterior ao check-in.")
            return

        nova_reserva = Reserva(cliente_encontrado, quarto_encontrado, data_inicio, data_fim)
        reservas.append(nova_reserva)
        quarto_encontrado.status = "Ocupado"
        print("Reserva realizada com sucesso!")

    except ValueError:
        print("Erro: Formato de número ou data inválido! Use o formato correto (DD/MM/AAAA).")

def listar_reservas(reservas):
    print("\n--- RESERVAS ATIVAS ---")
    if not reservas:
        print("Nenhuma reserva registrada.")
    for r in reservas:
        print(r)

def main():
    clientes = []
    
    # Inicializando com quartos usando herança
    quartos = [
        QuartoSolteiro(101),
        QuartoCasal(102),
        Suite(103)
    ]
    reservas = []

    # Estrutura de repetição do menu principal
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        # Estruturas de decisão
        if opcao == "1":
            cadastrar_cliente(clientes)
        elif opcao == "2":
            listar_quartos(quartos)
        elif opcao == "3":
            realizar_reserva(clientes, quartos, reservas)
        elif opcao == "4":
            listar_reservas(reservas)
        elif opcao == "5":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 1 e 5.")

if __name__ == "__main__":
    main()