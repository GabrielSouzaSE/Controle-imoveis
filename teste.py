import pandas as pd
from datetime import date
# Definições das classes!
class Proprietario:
    proprietarios = []

    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

        if Proprietario.procurar(cpf) is None:
            Proprietario.proprietarios.append(self)

    @staticmethod
    def procurar(cpf):
        for proprietario in Proprietario.proprietarios:
            if proprietario.cpf == cpf:
                return proprietario
            return None


class Imovel:
    imoveis = []

    def __init__(self, codigo, cpf, tipo, endereco, valor_do_aluguel, status):
        self.codigo = codigo
        self.cpf = cpf
        self.tipo = tipo
        self.endereco = endereco
        self.valor_do_aluguel = valor_do_aluguel
        self.status = status

        if Imovel.procurar(codigo) is None:
            Imovel.imoveis.append(self)

    @staticmethod
    def procurar(codigo):
        for imovel in Imovel.imoveis:
            if imovel.codigo == codigo:
                return imovel
            return None

    @staticmethod
    def modificar_status(imovel, status):
        imovel.status = status


class Inquilino:
    inquilinos = []

    def __init__(self, nome, cpf, data_de_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento

        if Inquilino.procurar(cpf) is None:
            Inquilino.inquilinos.append(self)

    @staticmethod
    def procurar(cpf):
        for inquilino in Inquilino.inquilinos:
            if inquilino.cpf == cpf:
                return inquilino
        return None


class Aluguel:
    alugueis = []
    data_final = 'Sem data'

    def __init__(self, cpf_inquilino, codigo_imovel, data_inicio, data_final=data_final):
        self.cpf_inquilino = cpf_inquilino
        self.codigo_imovel = codigo_imovel
        self.data_inicio = data_inicio
        self.data_final = data_final

        if Aluguel.procurar(cpf_inquilino) is None:
            Aluguel.alugueis.append(self)

    @staticmethod
    def procurar(cpf_inquilino):
        for aluguel in Aluguel.alugueis:
            if aluguel.cpf_inquilino == cpf_inquilino:
                return aluguel
            return None
    
    @staticmethod
    def adicionar_fim_aluguel(aluguel,data_final):
        aluguel.data_final = data_final

    def calcular_comissao(self,data_atual,imovel):
        duracao = data_atual - self.data_inicio
        return print(f"A comissao calculada pro data atual: R${(duracao.days // 30) * (imovel.valor_do_aluguel * 0.1)}")
    
dados = pd.read_excel('Dados.xlsx','Proprietarios')
for i in range(len(dados)):
    nome = dados.loc[i][0]
    cpf = dados.loc[i][1]
    data_nascimento = dados.loc[i][2]
    data_nascimento = date(int(data_nascimento[:4]), int(data_nascimento[5:7]), int(data_nascimento[8:]))
    Proprietario(nome,str(cpf),data_nascimento)

dados = pd.read_excel('Dados.xlsx','Imoveis')
for i in range(len(dados)):
    codigo = dados.loc[i][0]
    cpf = dados.loc[i][1]
    tipo = dados.loc[i][2]
    endereco = dados.loc[i][3]
    valor_do_aluguel = dados.loc[i][4]
    status = dados.loc[i][5]
    Imovel(str(codigo),str(cpf),tipo,endereco,float(valor_do_aluguel),status)
    

dados = pd.read_excel('Dados.xlsx','Inquilinos')
for i in range(len(dados)):
    nome = dados.loc[i][0]
    cpf = dados.loc[i][1]
    dada_de_nascimento = dados.loc[i][2]
    Inquilino(nome,str(cpf),data_nascimento)

dados = pd.read_excel('Dados.xlsx','Alugueis')
for i in range(len(dados)):
    cpf_inquilino = dados.loc[i][0]
    codigo_imovel = dados.loc[i][1]
    data_inicio = dados.loc[i][2]
    data_final = dados.loc[i][3]
    Aluguel(str(cpf_inquilino),str(codigo_imovel),str(data_inicio),(data_final))

for i in Proprietario.proprietarios:
    print((i.data_nascimento))
    print(type(i.data_nascimento))