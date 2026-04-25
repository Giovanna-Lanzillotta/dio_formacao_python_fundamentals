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
    
    # Aqui esta a implementação do gerador
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
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
    # utilizando o ContaIterador
    for conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []
    pass