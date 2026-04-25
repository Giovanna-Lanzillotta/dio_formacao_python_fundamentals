# DESAFIO

import textwrap
from abc import ABC,abstractclassmethod, abstractproperty
from datetime import datetime

# Inicio da classe ContaIterador
class ContaIterador:
    def __init__(self, contas):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
# Fim da classe ContaIterador


# Inicio da classe Cliente
class Cliente:
    pass
#Fim da classe Cliente


# Inicio da classe Pessoa Fisica
class PessoaFisica(Cliente):
    pass
#Fim da classe Pessoa Fisica


# Inicio da classe Conta
class Conta:
    pass
# Fim da classe Conta


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
    
    def gerar_relatorio(self, tipo_transacao=None):
        pass
# fim da classe Historico


# Inicio da classe Transacao
class Transacao(ABC):
    pass
# fim da classe Transacao


# Inicio da classe Saque que estende Transacao
class Saque:
    pass
# Fim da classe Saque


# Inicio da classe Deposito que estende Transacao
class Deposito:
    pass
# Fim da classe Deposito


def log_transacao(func):
    pass


def menu():
    pass

def filtar_cliente(cpf, clientes):
    pass


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
    # TODO : alterar implementação, para utilizar a classe ContaIterador
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []
    pass