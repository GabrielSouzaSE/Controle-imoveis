from Funcao import cadastrarProprietario, cadastrarImovel, cadastrarInquilino, registrarAluguel, finalizarAluguel,\
                   relatorioProprietarios, relatorioImoveis, relatorioInquilinos,relatorioComissao,relatorioAluguel,criarDataFrame,salvarDataframe,ExcelparaMemoria
from datetime import date
import Classes 

try:
    open('Dados.xlsx', 'r')
except IOError:
    print('Criando novos arquivos...')
    criarDataFrame()

ExcelparaMemoria()
while True:
    print('\nMenu de Imóvel\n\n'
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
        cadastrarProprietario()

    elif escolha == '2':
        cadastrarImovel()

    elif escolha == '3':
        cadastrarInquilino()

    elif escolha == '4':
        registrarAluguel()

    elif escolha == '5':
        finalizarAluguel()

    elif escolha == '6':
        relatorioProprietarios()

    elif escolha == '7':
        relatorioImoveis()
    
    elif escolha == '8':
        relatorioInquilinos()

    elif escolha == '9':
        relatorioAluguel()

    elif escolha == '10':
        data_atual = input('\nInforme a data de atual(DD/MM/AAAA): ')
        data_atual = date(int(data_atual[6:]), int(data_atual[3:5]), int(data_atual[:2]))
        relatorioComissao(data_atual)
    else:
        print('\nOpção invalida! Digite novamente.')
