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
            if Imovel.procurar(cpf_prop) is None:
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
            
            print('\nImóvel cadastrado com sucesso!')
            Imovel(codigo, cpf_prop, tipo, endereco, valor)
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

            data = input('\nInforme a data de nascimento do proprietário (DD/MM/AAAA): ')
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
            if Aluguel.procurar(cpf_inqui) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            codigo_imovel = input('\nInforme o código do imóvel: ')
            assert codigo_imovel.isnumeric()
            if Aluguel.procurar(cpf) is None:
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
            if Aluguel.procurar(cpf_inqui) is None:
                print('\nO CPF não está cadastrado no nosso banco de dados!')
                raise AssertionError

            codigo_imovel = input('\nInforme o código do imóvel: ')
            assert codigo_imovel.isnumeric()
            if Aluguel.procurar(codigo_imovel) is None:
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

def relatorio_proprietarios():
    if len(Proprietario.proprietarios) >= 1:
        print("Lista dos Proprietários: ")
        for proprietario in Proprietario.proprietarios:
            print(f"Nome: {proprietario.nome} Cpf: {proprietario.cpf} Data de Nascimento {proprietario.data_nascimento}")
    else:
        print("Não tem proprietário no nosso banco de dados!")

# def criarDataFrame():
#     df = pd.DataFrame(columns=['Nome', 'CPF', 'Data de Nascimento'])  # Dataframe Proprietário
#     df2 = pd.DataFrame(columns=['Codigo', 'CPF do proprietário', 'Tipo', 'Endereço', 'Valor do Aluguel', 'Status Alugado'])  # Dataframe Imóvel
#     df3 = pd.DataFrame(columns=['Nome', 'CPF', 'Data de Nascimento'])  # Dataframe Inquilino
#     df4 = pd.DataFrame(columns=['Codigo da Disciplina', 'Matrícula do aluno', 'Nota 1', 'Nota 2'])  # Dataframe Notas
#     excel_writer = pd.ExcelWriter("Dados.xlsx")
#     df.to_excel(excel_writer, 'Proprietário', index=False)
#     df2.to_excel(excel_writer, 'Imóvel', index=False)
#     df3.to_excel(excel_writer, 'Inquilino', index=False)
#     df4.to_excel(excel_writer, 'Notas', index=False)
#     excel_writer.save()


# def salvarDataframe(lista_de_professores, lista_de_alunos, lista_de_disciplinas, lista_de_notas):
#     excel_writer = pd.ExcelWriter('Dados.xlsx')
#     i = 0
#     dados_professor = pd.read_excel('Dados.xlsx', 'Professores')
#     for professor in lista_de_professores:
#         linha = [professor.nome, str(professor.matricula), professor.data_nascimento]
#         dados_professor.loc[i] = linha
#         i += 1
#     dados_professor.to_excel(excel_writer, 'Professores', index=False)

#     i = 0
#     dados_alunos = pd.read_excel('Dados.xlsx', 'Alunos')
#     for aluno in lista_de_alunos:
#         linha = [aluno.nome, str(aluno.matricula), aluno.data_nascimento]
#         dados_alunos.loc[i] = linha
#         i += 1
#     dados_alunos.to_excel(excel_writer, 'Alunos', index=False)

#     i = 0
#     dados_disciplinas = pd.read_excel('Dados.xlsx', 'Disciplinas')
#     for disciplina in lista_de_disciplinas:
#         linha = [str(disciplina.codigo), disciplina.nome, str(disciplina.matricula_professor)]
#         dados_disciplinas.loc[i] = linha
#         i += 1
#     dados_disciplinas.to_excel(excel_writer, 'Disciplinas', index=False)

#     i = 0
#     dados_notas = pd.read_excel('Dados.xlsx', 'Notas')
#     for nota in lista_de_notas:
#         linha = [str(nota.codigo_disciplina), str(nota.matricula_aluno), float(nota.nota1), float(nota.nota2)]
#         dados_notas.loc[i] = linha
#         i += 1
#     dados_notas.to_excel(excel_writer, 'Notas', index=False)
#     excel_writer.save()


# def getDataFramefromExcel(lista_de_professores, lista_de_alunos, lista_de_disciplinas,
#                           lista_de_notas):
#     # Professor
#     dados = pd.read_excel('Dados.xlsx', 'Professores')
#     for i in range(len(dados)):
#         nome = dados.loc[i][0]
#         matricula = dados.loc[i][1]
#         data_nascimento = dados.loc[i][2]
#         professor = Classe.Professor(nome, str(matricula), data_nascimento)
#         lista_de_professores.append(professor)
#     # Aluno
#     dados = pd.read_excel('Dados.xlsx', 'Alunos')
#     for i in range(len(dados)):
#         nome = dados.loc[i][0]
#         matricula = dados.loc[i][1]
#         data_nascimento = dados.loc[i][2]
#         aluno = Classe.Aluno(nome, str(matricula), data_nascimento)
#         lista_de_alunos.append(aluno)
#     # Disciplina
#     dados = pd.read_excel('Dados.xlsx', 'Disciplinas')
#     for i in range(len(dados)):
#         codigo = int(dados.loc[i][0])
#         nome = str(dados.loc[i][1])
#         matricula_professor = dados.loc[i][2]
#         disciplina = Classe.Disciplina(int(codigo), nome, str(matricula_professor))
#         lista_de_disciplinas.append(disciplina)
#     # Notas
#     dados = pd.read_excel('Dados.xlsx', 'Notas')
#     for i in range(len(dados)):
#         codigo_da_disciplina = dados.loc[i][0]
#         matricula_aluno = dados.loc[i][1]
#         nota1 = dados.loc[i][2]
#         nota2 = dados.loc[i][3]
#         notas = Classe.Nota(int(codigo_da_disciplina), str(matricula_aluno), float(nota1), float(nota2))
#         lista_de_notas.append(notas)
