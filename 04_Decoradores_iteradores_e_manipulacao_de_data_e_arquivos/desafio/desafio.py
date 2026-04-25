# DESAFIO

import textwrap
from abc import ABC,abstractclassmethod, abstractproperty
from datetime import datetime

# Aqui esta a parte do iterador personalizado
# Inicio da classe ContaIterador
class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self._contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._contador]
            self._contador +=1
            return f"""
            🏦 Agência:\t{conta.agencia}
            🏧Número:\t{conta.numero}
            👤 Titular:\t{conta.cliente.nome}
            💰 Saldo:\t{conta.saldo:.2f}
            """
        except IndexError:
            raise StopIteration
# Fim da classe ContaIterador


# Inicio da classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = []
#Fim da classe Cliente


# Inicio da classe Pessoa Fisica
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        # super() foi usado para chamar o construtor da classe pai Cliente
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
#Fim da classe Pessoa Fisica


# Inicio da classe Conta
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
# Fim da classe Conta

# Adicionando os @propety para pemitir que o Iterador acesse os dados
    @property
    def saldo(self): return self._saldo
    
    @property
    def numero(self): return self._numero
    
    @property
    def agencia(self): return self._agencia
    
    @property
    def cliente(self): return self._cliente

# Inicio da classe Conta Corrente que estende de Conta
class ContaCorrente(Conta):
    pass
# Fim da classe conta corrente


# Inicio da classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor" : transacao.valor,
                "data" : datetime.now().strftime("%d-%m-%y %H:%M:%s"),
            }
        )
    
    # Aqui esta a implementação do gerador
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
# fim da classe Historico


#---- inicio das classes de transação-------
# Inicio da classe Transacao
class Transacao(ABC):
    pass
# fim da classe Transacao


# Inicio da classe Saque que estende Transacao
class Saque(Transacao):
    pass
# Fim da classe Saque


# Inicio da classe Deposito que estende Transacao
class Deposito(Transacao):
    pass
# Fim da classe Deposito


# Aqui esta a parte de decorador de Log
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{data_hora}] Função executada: {func.__name__}")
        return resultado
    return envelope


def menu():
    pass

def filtar_cliente(cpf, clientes):
    for cliente in clientes: # FOR será usado para percorrer cada objeto cliente de uma lista de clientes
        if cliente.cpf == cpf: # Verifica se o cpf do objeto é igual ao cpf colocado
            return cliente # Caso encontre ele irá retornar o cliente encontrado
    return None # Se o loop acabar e não encontrar o cliente ele irá retornar None


@log_transacao
def depositar(clientes):
    pass

@log_transacao
def sacar(clientes):
    pass

@log_transacao
def exibir_extrato(clientes):
    pass

@log_transacao
def criar_cliente(clientes):
    pass

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    pass


def listar_contas(contas):
    # utilizando o ContaIterador
    for conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []
    pass