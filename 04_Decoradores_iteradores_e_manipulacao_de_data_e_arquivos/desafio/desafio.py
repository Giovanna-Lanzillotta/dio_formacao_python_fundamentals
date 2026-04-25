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
        self.conta = [] # cria uma lista vazia para armazenar as conta de um cliente
        self.indice_conta = 0 # contador para saber o numero de contas

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10: #Conta o numero de transacoes do dia e caso
            # o resultado for maior ou igual 10 ele mostra uma mensagem de alerta.
            print("\n@@@ ❗❗❗ Você excedeu o número de transações permitidas para hoje! ❗❗❗ @@@")
            return

        transacao.registrar(conta) # Adiciona na conta e atualiza o saldo

    # Conecta uma conta nova a ym cliente específico
    def adicionar_conta(self, conta):
        self.contas.append(conta) # Pega a conta criada e adiciona na lista 'self.contas' do cliente
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

    
    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()

        # Cria uma lista vazia para guardar a informação de hoje
        transacoes = []
        for transacao in self.transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()

            # Confere se a data da transacao é igual a data de hoje
            if data_atual == data_transacao:
                transacoes.append(transacao) # Se sim adiciona na lista

        return transacao # após percorrer tudo retorna a lista cheia ou vazia
        
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

def recuperar_conta_cliente(cliente):
    pass

@log_transacao
def depositar(clientes):
    pass

@log_transacao
def sacar(clientes):
    pass

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente:  ")

    # Usa a função filtar_clientes para achar o objeto 'cliente' na lista.
    cliente = filtar_cliente(cpf, clientes) 

    if not cliente:
        print("\n@@@ ❌Cliente não encontrado! ❌~@@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("========== EXTRATO ==========")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "💫 Não foram realizadas movimentações 💫"

    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==============================")


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