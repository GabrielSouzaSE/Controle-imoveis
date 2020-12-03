from Classe import Professor, Aluno, Disciplina, Nota
from Funcao import buscarDisciplina, buscarProfessor, voltarMenu, criarDataFrame, \
    salvarDataframe, getDataFramefromExcel, validar_professor, validar_aluno, validar_disciplina, validar_nota

try:
    open('Dados.xlsx', 'r')

except IOError:
    print('Criando novos arquivos...')
    criarDataFrame()

listaProp = []
listaImovel = []
listaInquilino = []
lista = []
notas = []
alunos = []

getDataFramefromExcel(listaProf, listaAluno, listaDisc, listaNota)

while True:
    print('\nMenu de Imvel\n\n'
          '1 - Cadastrar Proprietário\n'
          '2 - Cadastrar Imóvel\n'
          '3 - Cadastrar Inquilino\n'
          '4 - Registrar Aluguel\n'
          '5 - Finalizar Aluguel\n'
          '6 - Relatório de Proprietários\n'
          '7 - Relatório de Imóveis\n'
          '8 - Relatório de Inquilinos\n'
          '9 - Relatório de Aluguéis\n'
          '10 - Relatório de Comissões\n'
          '0 - Sair\n')

    escolha = input('Escolha uma das opções acima: ')

    if escolha == '0':
        salvarDataframe()
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
