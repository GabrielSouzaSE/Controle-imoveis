from Classe import Professor, Aluno, Disciplina, Nota
from Funcao import buscarDisciplina, buscarProfessor, voltarMenu, criarDataFrame, \
    salvarDataframe, getDataFramefromExcel, validar_professor, validar_aluno, validar_disciplina, validar_nota

try:
    open('Dados.xlsx', 'r')

except IOError:
    print('Criando novos arquivos...')
    criarDataFrame()

listaProf = []
listaAluno = []
listaDisc = []
listaNota = []
notas = []
alunos = []

getDataFramefromExcel(listaProf, listaAluno, listaDisc, listaNota)

while True:
    print('\nMenu da Escola\n\n'
          '1 - Cadastro de Professores\n'
          '2 - Cadastro de Alunos\n'
          '3 - Cadastro de Disciplinas\n'
          '4 - Cadastro de Notas\n'
          '5 - Relatório de Notas\n'
          '0 - Sair\n')

    escolha = input('Escolha uma das opções acima: ')

    if escolha == '0':
        salvarDataframe(listaProf, listaAluno, listaDisc, listaNota)
        print('\nFim do programa.')
        break

    elif escolha == '1':
        validar_professor(listaProf)

    elif escolha == '2':
        validar_aluno(listaAluno)

    elif escolha == '3':
        validar_disciplina(listaDisc)

    elif escolha == '4':
        validar_nota(listaNota)

    elif escolha == '5':
        while True:
            try:
                buscaDisc = input('\nInforme o código da Disciplina: ')

                disc = buscarDisciplina(buscaDisc, listaDisc)
                assert disc is not False
                prof = buscarProfessor(disc, listaProf)
                print(listaNota[0].codigo_disciplina)
                for i in range(len(listaNota)):
                    if listaNota[i].codigo_disciplina == disc.codigo:
                        notas.append(listaNota[i])
                Disciplina.relatorioNotas(disc, prof, notas)
                notas = []
                break

            except AssertionError:
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    break

    else:
        print('\nOpção invalida! Digite novamente.')
