import pandas as pd
from datetime import date
from Classes import Proprietario, Imovel, Inquilino, Aluguel


def cadastrarProprietario():
    while True:
        try:
            nome = input('\nInforme o nome do proprietário: ').strip().capitalize()
            assert len(nome) >= 1

            cpf = str(input('\nInforme o CPF do proprietário (apenas números): '))
            assert cpf.isnumeric()
            if Proprietario.procurar(cpf) is not None:
                print('\nO CPF já está cadastrado no nosso banco de dados!')
                raise AssertionError

            data = input('\nInforme a data de nascimento do proprietário (DD/MM/AAAA): ')
            assert data[2] == '/' and data[4] == '/'
            data = date(int(data[6:]), int(data[3:5]), int(data[:2]))

            print('\nProprietário cadastrado com sucesso!')
            Proprietario(nome, str(cpf), data)
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

            cpf_prop = str(input('\nInforme o CPF do proprietário (apenas números): '))
            assert cpf_prop.isnumeric()
            if Proprietario.procurar(str(cpf_prop)) is None:
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
            Imovel(codigo, cpf_prop, tipo, endereco, valor, status)
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
            assert data[2] == '/' and data[4] == '/'
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
            cpf_inqui = str(input('\nInforme o CPF do inquilino (apenas números): '))
            assert cpf_inqui.isnumeric()
            if Inquilino.procurar(cpf_inqui) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            codigo_imovel = str(input('\nInforme o código do imóvel: '))
            assert codigo_imovel.isnumeric()
            imovel = Imovel.procurar(codigo_imovel)
            if imovel is None or imovel.status == 'Sim':
                print('\nO imóvel não está cadastrado no nosso banco de dados ou já existe um aluguel registrado nesse imóvel!')
                raise AssertionError

            data_inicio = input('\nInforme a data de início do aluguel (DD/MM/AAAA): ')
            assert data_inicio[2] == '/' and data_inicio[4] == '/'
            data_inicio = date(int(data_inicio[6:]), int(data_inicio[3:5]), int(data_inicio[:2]))

            print('\nAluguel registrado com sucesso!')
            Imovel.modificar_status(imovel, 'Sim')
            Aluguel(cpf_inqui, codigo_imovel, data_inicio)
            break

        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break


def finalizarAluguel():
    while True:
        try:
            cpf_inqui = str(input('\nInforme o CPF do inquilino (apenas números): '))
            assert cpf_inqui.isnumeric()
            if Inquilino.procurar(cpf_inqui) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            codigo_imovel = input('\nInforme o código do imóvel: ')
            assert codigo_imovel.isnumeric()
            imovel = Imovel.procurar(codigo_imovel)
            if imovel is None or imovel.status == 'Não':
                print('\nO imóvel não está cadastrado no nosso banco de dados ou não existe um aluguel registrado nesse imóvel!')
                raise AssertionError

            data_fim = input('\nInforme a data de final do aluguel (DD/MM/AAAA): ')
            assert data_fim[2] == '/' and data_fim[4] == '/'
            data_fim = date(int(data_fim[6:]), int(data_fim[3:5]), int(data_fim[:2]))
            aluguel = Aluguel.procurar(cpf_inqui)
            if aluguel.data_inicio > data_fim:
                print('\nFoi inserida uma data final antes da data de início do aluguel!')
                raise AssertionError

            print('\nAluguel finalizado com sucesso!')
            Imovel.modificar_status(imovel, 'Não')
            Aluguel.adicionar_fim_aluguel(aluguel, data_fim)
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
    print()
    if len(Proprietario.proprietarios) >= 1:
        print("Lista dos Proprietários: ")
        print(f"{'Nome':<12} {'CPF':<12} Data de nascimento")
        for proprietario in Proprietario.proprietarios:
            print(f'{proprietario.nome:<12} {proprietario.cpf:<12} {proprietario.data_nascimento}')
    else:
        print("Não existem proprietários no nosso banco de dados!")


def relatorioImoveis():
    print()
    if len(Imovel.imoveis) >= 1:
        print("Lista de Imoveis:")
        print(f"{'Código':<7} {'CPF do proprietário':<20} {'Nome do Proprietário':<21} {'Tipo':<12} {'Endereço':<10} "
              f"{'Valor do aluguel':<17} Status alugado")
        for imovel in Imovel.imoveis:
            proprietario = Proprietario.procurar(imovel.cpf)
            print(f"{imovel.codigo:<7} {proprietario.cpf:<20} {proprietario.nome:<21} {imovel.tipo:<12} "
                  f"{imovel.endereco:<10} R${imovel.valor_do_aluguel:<15} {imovel.status}")
    else:
        print("Não existem imóveis no nosso banco de dados! ")


def relatorioInquilinos():
    print()
    if len(Inquilino.inquilinos) >= 1:
        print("Lista de Inquilinos: ")
        print(f"{'Nome':<12} {'CPF':<12} Data de nascimento")
        for inquilino in Inquilino.inquilinos:
            print(f'{inquilino.nome:<12} {inquilino.cpf:<12} {inquilino.data_nascimento}')
    else:
        print("Não existem inquilinos no nosso banco de dados!")


def relatorioAluguel():
    print("\nRelatório de Aluguéis")
    if len(Aluguel.alugueis) >= 1:
        for aluguel in Aluguel.alugueis:
            inquilino = Inquilino.procurar(aluguel.cpf_inquilino)
            imovel = Imovel.procurar(aluguel.codigo_imovel)
            proprietario = Proprietario.procurar(imovel.cpf)
            print(f"\nNome do inquilino: {inquilino.nome} ")
            print(f"Código: {imovel.codigo}, Tipo: {imovel.tipo}, Endereço: {imovel.endereco}, Proprietário: {proprietario.nome}")
            print(f"Valor do Aluguel: {imovel.valor_do_aluguel}")
            print(f"Data do início do aluguel: {aluguel.data_inicio}")
            if aluguel.data_final != 'Sem data':
                print(f"Data do final do aluguel: {aluguel.data_final}")

    else:
        print("Não existem aluguéis cadastrados no nosso banco de dados!")


def relatorioComissao():  # relatorio_comissao python right way
    print("\nRelatório de Comissões\n")
    if len(Aluguel.alugueis) >= 1:
        for aluguel in Aluguel.alugueis:
            imovel = Imovel.procurar(aluguel.codigo_imovel)
            if imovel.status == 'Sim':
                print(f'Valor do aluguel: {round(imovel.valor_do_aluguel, 2)}')
                print(f'Data do início do aluguel: {aluguel.data_inicio}')
                print(f'Valor da comissão do imóvel {imovel.codigo}: R${round((imovel.valor_do_aluguel * 0.1), 2)}')
                aluguel.calcular_comissao(date.today(), imovel)
    else:
        print("Não existem aluguéis ativos no nosso banco de dados!")


def criarDataFrame():
    excel_writer = pd.ExcelWriter('Dados.xlsx')  # pylint: disable=abstract-class-instantiated
    proprietarios_dataframe = pd.DataFrame(columns=['Nome', 'CPF', 'Data de Nascimento'])
    imovel_dataframe = pd.DataFrame(columns=['Codigo', 'Cpf', 'Tipo', 'Endereco', 'Valor do aluguel', 'Status'])
    inquilinos_dataframe = pd.DataFrame(columns=['Nome', 'Cpf', 'Data de Nascimento'])
    aluguel_dataframe = pd.DataFrame(columns=['Cpf', 'Codigo', 'data inicial', 'data final'])
    proprietarios_dataframe.to_excel(excel_writer, 'Proprietarios', index=False)
    imovel_dataframe.to_excel(excel_writer, 'Imoveis', index=False)
    inquilinos_dataframe.to_excel(excel_writer, 'Inquilinos', index=False)
    aluguel_dataframe.to_excel(excel_writer, 'Alugueis', index=False)
    excel_writer.save()


def salvarDataframe():
    excel_writer = pd.ExcelWriter('Dados.xlsx')  # pylint: disable=abstract-class-instantiated

    i = 0
    dados_proprietarios = pd.read_excel('Dados.xlsx', 'Proprietarios')
    for proprietario in Proprietario.proprietarios:
        linha = [proprietario.nome, proprietario.cpf, str(proprietario.data_nascimento)]
        dados_proprietarios.loc[i] = linha
        i += 1
    dados_proprietarios.to_excel(excel_writer, 'Proprietarios', index=False)

    i = 0
    dados_imoveis = pd.read_excel('Dados.xlsx', 'Imoveis')
    for imovel in Imovel.imoveis:
        linha = [imovel.codigo, imovel.cpf, imovel.tipo, imovel.endereco, imovel.valor_do_aluguel, imovel.status]
        dados_imoveis.loc[i] = linha
        i += 1
    dados_imoveis.to_excel(excel_writer, 'Imoveis', index=False)

    i = 0
    dados_inquilinos = pd.read_excel('Dados.xlsx', 'Inquilinos')
    for inquilino in Inquilino.inquilinos:
        linha = [inquilino.nome, inquilino.cpf, str(inquilino.data_nascimento)]
        dados_inquilinos.loc[i] = linha
        i += 1
    dados_inquilinos.to_excel(excel_writer, 'Inquilinos', index=False)

    i = 0
    dados_alugueis = pd.read_excel('Dados.xlsx', 'Alugueis')
    for aluguel in Aluguel.alugueis:
        linha = [aluguel.cpf_inquilino, aluguel.codigo_imovel, str(aluguel.data_inicio), str(aluguel.data_final)]
        dados_alugueis.loc[i] = linha
        i += 1
    dados_alugueis.to_excel(excel_writer, 'Alugueis', index=False)
    excel_writer.save()


def ExcelparaMemoria():
    dados = pd.read_excel('Dados.xlsx', 'Proprietarios')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        cpf = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        data_nascimento = date(int(data_nascimento[:4]), int(data_nascimento[5:7]), int(data_nascimento[8:]))
        Proprietario(nome, str(cpf), data_nascimento)

    dados = pd.read_excel('Dados.xlsx', 'Imoveis')
    for i in range(len(dados)):
        codigo = dados.loc[i][0]
        cpf = dados.loc[i][1]
        tipo = dados.loc[i][2]
        endereco = dados.loc[i][3]
        valor_do_aluguel = dados.loc[i][4]
        status = dados.loc[i][5]
        Imovel(str(codigo), str(cpf), tipo, endereco, float(valor_do_aluguel), status)

    dados = pd.read_excel('Dados.xlsx', 'Inquilinos')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        cpf = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        data_nascimento = date(int(data_nascimento[:4]), int(data_nascimento[5:7]), int(data_nascimento[8:]))
        Inquilino(nome, str(cpf), data_nascimento)

    dados = pd.read_excel('Dados.xlsx', 'Alugueis')
    for i in range(len(dados)):
        cpf_inquilino = dados.loc[i][0]
        codigo_imovel = dados.loc[i][1]
        data_inicio = dados.loc[i][2]
        data_inicio = date(int(data_inicio[:4]), int(data_inicio[5:7]), int(data_inicio[8:]))
        data_final = dados.loc[i][3]
        if data_final != 'Sem data':
            data_final = date(int(data_final[:4]), int(data_final[5:7]), int(data_final[8:]))
        Aluguel(str(cpf_inquilino), str(codigo_imovel), data_inicio, data_final)
