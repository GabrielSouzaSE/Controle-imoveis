import pandas as pd
from datetime import date
from Classes import Proprietario, Imovel, Inquilino, Aluguel


def cadastrarProprietario():
    while True:
        try:
            nome = input('\nInforme o nome do proprietário: ').strip().capitalize()
            assert len(nome) >= 1

            cpf = input('\nInforme o CPF do proprietário (apenas números): ')
            assert cpf.isnumeric()
            if Proprietario.procurar(cpf) is not None:
                print('\nO CPF já está cadastrado no nosso banco de dados!')
                raise AssertionError

            data = input('\nInforme a data de nascimento do proprietário (DD/MM/AAAA): ')
            data = date(int(data[6:]), int(data[3:5]), int(data[:2]))

            print('\nProprietário cadastrado com sucesso!')
            Proprietario(nome, cpf, data)
            break

        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break


def cadastrarImovel():
    while True:
        try:
            codigo = input('\nInforme o código do imóvel: ')
            assert codigo.isnumeric()
            if Imovel.procurar(codigo) is not None:
                print('\nO código do imóvel já está cadastrado no nosso banco de dados!')
                raise AssertionError

            cpf_prop = input('\nInforme o CPF do proprietário (apenas números): ')
            assert cpf_prop.isnumeric()
            if Proprietario.procurar(cpf_prop) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            print('\n1 - Casa\n'
                  '2 - Apartamento')

            escolha = input('\nInforme o tipo do imóvel a partir das opções acima: ')

            if escolha == '1':
                tipo = 'Casa'
            elif escolha == '2':
                tipo = 'Apartamento'
            else:
                raise AssertionError

            endereco = input('\nInforme o endereço do imóvel: ')
            assert len(endereco) >= 1

            valor = float(input('\nInforme o valor do aluguel: '))
            status = 'Não'
            print('\nImóvel cadastrado com sucesso!')
            Imovel(codigo, cpf_prop, tipo, endereco, valor,status)
            break

        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break


def cadastrarInquilino():
    while True:
        try:
            nome = input('\nInforme o nome do inquilino: ').strip().capitalize()
            assert len(nome) >= 1

            cpf = input('\nInforme o CPF do inquilino (apenas números): ')
            assert cpf.isnumeric()
            if Inquilino.procurar(cpf) is not None:
                print('\nO CPF já está cadastrado no nosso banco de dados!')
                raise AssertionError

            data = input('\nInforme a data de nascimento do inquilino (DD/MM/AAAA): ')
            data = date(int(data[6:]), int(data[3:5]), int(data[:2]))

            print('\nInquilino cadastrado com sucesso!')
            Inquilino(nome, cpf, data)
            break

        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break


def registrarAluguel():
    while True:
        try:
            cpf_inqui = input('\nInforme o CPF do inquilino (apenas números): ')
            assert cpf_inqui.isnumeric()
            if Inquilino.procurar(cpf_inqui) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            codigo_imovel = input('\nInforme o código do imóvel: ')
            assert codigo_imovel.isnumeric()
            if Imovel.procurar(codigo_imovel) is None:
                print('\nO código do imóvel não está cadastrado no nosso banco de dados!')
                raise AssertionError

            data_inicio = input('\nInforme a data de início do aluguel (DD/MM/AAAA): ')
            data_inicio = date(int(data_inicio[6:]), int(data_inicio[3:5]), int(data_inicio[:2]))

            print('\nAluguel registrado com sucesso!')
            Aluguel(cpf_inqui, codigo_imovel, data_inicio)
            break

        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break


def finalizarAluguel():
    while True:
        try:
            cpf_inqui = input('\nInforme o CPF do inquilino (apenas números): ')
            assert cpf_inqui.isnumeric()
            if Inquilino.procurar(cpf_inqui) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            codigo_imovel = input('\nInforme o código do imóvel: ')
            assert codigo_imovel.isnumeric()
            if Imovel.procurar(codigo_imovel) is None:
                print('\nO código do imóvel não está cadastrado no nosso banco de dados!')
                raise AssertionError

            data_fim = input('\nInforme a data de início do aluguel (DD/MM/AAAA): ')
            data_fim = date(int(data_fim[6:]), int(data_fim[3:5]), int(data_fim[:2]))

            print('\nAluguel finalizado com sucesso!')
            Aluguel(cpf_inqui, codigo_imovel, data_fim)
            break

        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break


def voltarMenu():
    while True:
        try:
            voltar = input('\nInformação inválida! Deseja voltar para o Menu? [S/N] ').strip()[0]
            assert voltar.casefold() == 's' or voltar.casefold() == 'n'
            return voltar

        except (AssertionError, IndexError):
            print('\nOpção inválida! Informe "SIM" ou "NÃO".')


def relatorioProprietarios():
    if len(Proprietario.proprietarios) >= 1:
        print("Lista dos Proprietários: ")
        for proprietario in Proprietario.proprietarios:
            print(f"Nome: {proprietario.nome} Cpf: {proprietario.cpf} Data de Nascimento: {proprietario.data_nascimento}")
    else:
        print("Não tem proprietário no nosso banco de dados!")


def relatorioImoveis():
    if len(Imovel.imoveis) >= 1:
        print("Lista de Imoveis:")
        for imovel in Imovel.imoveis:
            proprietario = Proprietario.procurar(imovel.cpf)
            print(f"Código: {imovel.codigo} Cpf: {proprietario.cpf} Nome do Proprietário: {proprietario.nome} "
                  f"Tipo: {imovel.tipo} Endereço: {imovel.endereco} Valor do Aluguel: {imovel.valor_do_aluguel} "
                  f"Status Alugado: {imovel.status}")
    else:
        print("Não tem Imóveis no nosso banco de dados! ")


def relatorioInquilinos():
    if len(Inquilino.inquilinos) >=1:
        print("Lista de Inquilinos: ")
        for inquilino in Inquilino.inquilinos:
            print(f'Nome: {inquilino.nome} Cpf: {inquilino.cpf} Data de nascimento: {inquilino.data_de_nascimento} ')
    else:
        print("Não tem Inquilinos no nosso banco de dados!")
