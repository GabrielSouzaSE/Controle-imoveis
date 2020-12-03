from datetime import date
from Funcao import voltarMenu


class Professor:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self, nome=nome, matricula=matricula, data_nascimento=data_nascimento):

        if nome == '' and matricula == '':
            while True:
                try:
                    self.matricula = input('\nInforme a matrícula do professor: ')
                    assert self.matricula.isnumeric()

                    self.nome = input('\nInforme o nome do professor: ').strip().capitalize()
                    assert len(self.nome) >= 1

                    data = input('\nInforme a data de nascimento do professor (DD/MM/AAAA): ')
                    self.data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))

                    print('\nProfessor cadastrado.')
                    break

                except (AssertionError, ValueError):
                    voltar = voltarMenu()
                    if voltar.casefold() == 's':
                        break

        else:
            self.nome = nome
            self.matricula = matricula
            self.data_nascimento = data_nascimento

    def getNome(self):
        return self.nome


class Aluno:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self, nome=nome, matricula=matricula, data_nascimento=data_nascimento):
        if nome == '' and matricula == '':
            while True:
                try:
                    self.matricula = input('\nInforme a matrícula do aluno: ')
                    assert self.matricula.isnumeric()

                    self.nome = input('\nInforme o nome do aluno: ').strip().capitalize()
                    assert len(self.nome) >= 1

                    data = input('\nInforme a data de nascimento do aluno (DD/MM/AAAA): ')
                    self.data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))

                    print('\nAluno cadastrado.')
                    break

                except (AssertionError, ValueError):
                    voltar = voltarMenu()
                    if voltar.casefold() == 's':
                        break

        else:
            self.nome = nome
            self.matricula = matricula
            self.data_nascimento = data_nascimento

    def getNome(self):
        return self.nome


class Disciplina:
    codigo = ''
    nome = ''
    matricula_professor = ''

    def __init__(self, codigo=codigo, nome=nome, matricula_professor=matricula_professor):
        if codigo == '' and nome == '' and matricula_professor == '':
            while True:
                try:
                    self.codigo = str(input('\nInforme o código da disciplina: '))
                    assert self.codigo.isnumeric()

                    self.nome = input('\nInforme o nome da disciplina: ').strip().capitalize()
                    assert len(self.nome) >= 1

                    self.matricula_professor = input('\nInforme a matrícula do professor: ')
                    assert self.matricula_professor.isnumeric()
                
                    print('\nDisciplina cadastrada.')
                    break

                except AssertionError:
                    voltar = voltarMenu()
                    if voltar.casefold() == 's':
                        break
        else:
            self.codigo = str(codigo)
            self.nome = nome
            self.matricula_professor = matricula_professor

    def relatorioNotas(self, professor, notas):
        print(f'\nNome da Disciplina: {self.nome}'
              f'\nMatrícula do professor: {self.matricula_professor}'
              f'\nNome do Professor: {Professor.getNome(professor)}')
        for i in range(len(notas)):
            print(f'\nMatrícula do aluno: {Nota.getMatriculaAluno(notas[i])}'
                  # f'- Nome do aluno: {Aluno.getNome(alunos[i])} '
                  f'- Nota final: {Nota.calcularMedia(notas[i])}')


class Nota:
    codigo_disciplina = ''
    matricula_aluno = ''
    nota1 = 0.0
    nota2 = 0.0

    def __init__(self, codigo_disciplina=codigo_disciplina, matricula_aluno=matricula_aluno, nota1=nota1, nota2=nota2):
        if codigo_disciplina == '' and matricula_aluno == '':
            while True:
                try:
                    self.codigo_disciplina = str(input('\nInforme o código da disciplina: '))
                    assert self.codigo_disciplina.isnumeric()

                    self.matricula_aluno = input('\nInforme a matrícula do aluno: ')
                    assert self.matricula_aluno.isnumeric()

                    self.nota1 = float(input('\nInforme a primeira nota: '))
                    assert 0 <= self.nota1 <= 10

                    self.nota2 = float(input('\nInforme a segunda nota: '))
                    assert 0 <= self.nota2 <= 10

                    print('\nNotas cadastradas.')
                    break

                except (AssertionError, ValueError):
                    voltar = voltarMenu()
                    if voltar.casefold() == 's':
                        break

        else:
            self.codigo_disciplina = str(codigo_disciplina)
            self.matricula_aluno = matricula_aluno
            self.nota1 = nota1
            self.nota2 = nota2

    def calcularMedia(self):
        return round(((self.nota1 + self.nota2) / 2), 2)

    def getMatriculaAluno(self):
        return self.matricula_aluno
