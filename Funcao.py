import pandas as pd
from datetime import date
import Classe


def buscarDisciplina(busca, listaDisc):
    for i in range(len(listaDisc)):
        if listaDisc[i].codigo == busca:
            return listaDisc[i]

    return False


def buscarProfessor(disciplina, listaProf):
    for i in range(len(listaProf)):
        if str(listaProf[i].matricula) == str(disciplina.matricula_professor):
            return listaProf[i]

def voltarMenu():
    while True:
        try:
            voltar = input('\nInformação inválida! Deseja voltar para o Menu? [S/N] ').strip()[0]
            assert voltar.casefold() == 's' or voltar.casefold() == 'n'
            return voltar

        except (AssertionError, IndexError):
            print('\nOpção inválida! Informe "SIM" ou "NÃO".')

def validar_professor(lista_professores):
    while True:
        try:
            condicao = ''
            matricula = input('\nInforme a matrícula do professor: ')
            assert matricula.isnumeric()
            for i in range(len(lista_professores)):
                if matricula == lista_professores[i].matricula:
                    print("Já existe um professor cadastrado com essa matricula!")
                    condicao = True
                    break 
            if condicao == True:
                break
            nome = input('\nInforme o nome do professor: ').strip().capitalize()
            assert len(nome) >= 1
            data = input('\nInforme a data de nascimento do professor (DD/MM/AAAA): ')
            data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))
            professor = Classe.Professor(nome,matricula,data_nascimento)
            lista_professores.append(professor)
            print("Professor cadastrado com sucesso!")
            break
        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break

def validar_aluno(lista_alunos):
     while True:
        try:
            condicao = ''
            matricula = input('\nInforme a matrícula do aluno: ')
            assert matricula.isnumeric()
            for i in range(len(lista_alunos)):
                if matricula == lista_alunos[i].matricula:
                    print("Já existe um aluno cadastrado com essa matricula!")
                    condicao = True
                    break
            if condicao == True:
                break
            nome = input('\nInforme o nome do aluno: ').strip().capitalize()
            assert len(nome) >= 1
            data = input('\nInforme a data de nascimento do aluno (DD/MM/AAAA): ')
            data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))
            aluno = Classe.Aluno(nome,matricula,data_nascimento)
            lista_alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")
            break 
            break
        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break

def validar_disciplina(lista_disciplinas):
    while True:
        try:
            condicao = ''
            codigo = str(input('\nInforme o código da disciplina: '))
            assert codigo.isnumeric()
            for i in range(len(lista_disciplinas)):
                if codigo == lista_disciplinas[i].codigo:
                    print("Já existe uma disciplina cadastrada com esse código!")
                    condicao = True
                    break
            if condicao == True:
                break
            nome = input('\nInforme o nome da disciplina: ').strip().capitalize()
            assert len(nome) >= 1
            matricula_professor = input('\nInforme a matrícula do professor: ')
            assert matricula_professor.isnumeric()
            disciplina = Classe.Disciplina(codigo,nome,matricula_professor)
            lista_disciplinas.append(disciplina)
            print('\nDisciplina cadastrada.')
            break  
        except AssertionError:
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break

def validar_nota(lista_notas):
    while True:
        try:
            condicao = ''
            codigo_disciplina = str(input('\nInforme o código da disciplina: '))
            assert codigo_disciplina.isnumeric()
            matricula_aluno = str(input('\nInforme a matrícula do aluno: '))
            assert matricula_aluno.isnumeric()
            for i in range(len(lista_notas)):
                if (codigo_disciplina,matricula_aluno) == (lista_notas[i].codigo_disciplina,lista_notas[i].matricula_aluno):
                    print("Este aluno já está cadastrado!")
                    condicao = True
                    break
            if condicao == True:
                break
            nota1 = float(input('\nInforme a primeira nota: '))
            assert 0 <= nota1 <= 10
            nota2 = float(input('\nInforme a segunda nota: '))
            assert 0 <= nota2 <= 10
            print('\nNotas cadastradas.')
            nota = Classe.Nota(str(codigo_disciplina),str(matricula_aluno),nota1,nota2)
            lista_notas.append(nota)
            break
        except (AssertionError, ValueError):
            voltar = voltarMenu()
            if voltar.casefold() == 's':
                break

def criarDataFrame():
    df = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])  # Dataframe Professor
    df2 = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])  # Dataframe Aluno
    df3 = pd.DataFrame(columns=['Codigo', 'Nome', 'Matricula do professor'])  # Dataframe Disciplinas
    df4 = pd.DataFrame(columns=['Codigo da Disciplina', 'Matrícula do aluno', 'Nota 1', 'Nota 2'])  # Dataframe Notas
    excel_writer = pd.ExcelWriter("Dados.xlsx")
    df.to_excel(excel_writer,'Professores', index=False)
    df2.to_excel(excel_writer,'Alunos', index=False)
    df3.to_excel(excel_writer,'Disciplinas', index=False)
    df4.to_excel(excel_writer,'Notas', index=False)
    excel_writer.save()


def salvarDataframe(lista_de_professores, lista_de_alunos, lista_de_disciplinas, lista_de_notas):
    excel_writer = pd.ExcelWriter('Dados.xlsx')
    i = 0
    dados_professor = pd.read_excel('Dados.xlsx','Professores')
    for professor in lista_de_professores:
        linha = [professor.nome, str(professor.matricula), professor.data_nascimento]
        dados_professor.loc[i] = linha
        i += 1
    dados_professor.to_excel(excel_writer, 'Professores', index=False)

    i = 0
    dados_alunos = pd.read_excel('Dados.xlsx','Alunos')
    for aluno in lista_de_alunos:
        linha = [aluno.nome, str(aluno.matricula), aluno.data_nascimento]
        dados_alunos.loc[i] = linha
        i += 1
    dados_alunos.to_excel(excel_writer,'Alunos', index=False)

    i = 0
    dados_disciplinas = pd.read_excel('Dados.xlsx','Disciplinas')
    for disciplina in lista_de_disciplinas:
        linha = [str(disciplina.codigo), disciplina.nome, str(disciplina.matricula_professor)]
        dados_disciplinas.loc[i] = linha
        i += 1
    dados_disciplinas.to_excel(excel_writer, 'Disciplinas', index=False)

    i = 0
    dados_notas = pd.read_excel('Dados.xlsx','Notas')
    for nota in lista_de_notas:
        linha = [str(nota.codigo_disciplina), str(nota.matricula_aluno), float(nota.nota1), float(nota.nota2)]
        dados_notas.loc[i] = linha
        i += 1
    dados_notas.to_excel(excel_writer, 'Notas', index=False)
    excel_writer.save()


def getDataFramefromExcel(lista_de_professores, lista_de_alunos, lista_de_disciplinas,
                          lista_de_notas):
    # Professor
    dados = pd.read_excel('Dados.xlsx','Professores')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        matricula = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        professor = Classe.Professor(nome, str(matricula), data_nascimento)
        lista_de_professores.append(professor)
    # Aluno
    dados = pd.read_excel('Dados.xlsx','Alunos')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        matricula = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        aluno = Classe.Aluno(nome, str(matricula), data_nascimento)
        lista_de_alunos.append(aluno)
    # Disciplina
    dados = pd.read_excel('Dados.xlsx','Disciplinas')
    for i in range(len(dados)):
        codigo = int(dados.loc[i][0])
        nome = str(dados.loc[i][1])
        matricula_professor = dados.loc[i][2]
        disciplina = Classe.Disciplina(int(codigo), nome, str(matricula_professor))
        lista_de_disciplinas.append(disciplina)
    # Notas
    dados = pd.read_excel('Dados.xlsx','Notas')
    for i in range(len(dados)):
        codigo_da_disciplina = dados.loc[i][0]
        matricula_aluno = dados.loc[i][1]
        nota1 = dados.loc[i][2]
        nota2 = dados.loc[i][3]
        notas = Classe.Nota(int(codigo_da_disciplina), str(matricula_aluno), float(nota1), float(nota2))
        lista_de_notas.append(notas)
