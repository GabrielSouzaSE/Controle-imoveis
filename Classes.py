#Definições das classes!
class Proprietario():
    proprietarios = []
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        if Proprietario.procurar(cpf) == None:
            Proprietario.proprietarios.append(self)
        
    @staticmethod
    def procurar(cpf):
        for proprietario in Proprietario.proprietarios:
            if proprietario.cpf == cpf:
                return proprietario
            return None

class Imovel():
    imoveis = []
    def __init__(self,codigo,cpf,tipo,endereço,valor_do_aluguel,status):
        self.codigo = codigo
        self.cpf = cpf
        self.tipo = tipo
        self.endereço = endereço
        self.valor_do_aluguel = valor_do_aluguel
        self.status = status
        if Imovel.procurar(codigo) == None:
            Imovel.imoveis.append(self)

    @staticmethod
    def procurar(codigo):
        for imovel in Imovel.imoveis:
            if imovel.codigo == codigo:
                return imovel
            return None
    @staticmethod
    def modificar_status(imovel):
        imovel.status = 'SIM'


class Inquilino():
    inquilinos = []
    def __init__(self,nome,cpf,data_de_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        if Inquilino.procurar(cpf) == None:
            Inquilino.inquilinos.append(self)

    @staticmethod
    def procurar(cpf):
        for inquilino in Inquilino.inquilinos:
            if inquilino.cpf == cpf:
                return inquilino
        return None

class Aluguel():
    alugueis = []
    def __init__(self,cpf_inquilino,codigo_imovel,data_inicio,data_final):
        self.cpf_inquilino = cpf_inquilino
        self.codigo_imovel = codigo_imovel
        self.data_inicio = data_inicio
        self.data_final = data_final
        if Aluguel.procurar(cpf_inquilino) == None:
            Aluguel.alugueis.append(self)

    @staticmethod
    def procurar(cpf_inquilino):
        for aluguel in Aluguel.alugueis:
            if aluguel.cpf_inquilino == cpf_inquilino:
                return aluguel
            return None
