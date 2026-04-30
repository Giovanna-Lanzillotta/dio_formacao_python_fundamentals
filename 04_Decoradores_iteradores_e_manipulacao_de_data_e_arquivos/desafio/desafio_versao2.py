# DESAFIO

import textwrap
from abc import ABC,abstractclassmethod, abstractmethod, abstractproperty
from datetime import datetime, timezone
from pathlib import Path

# Define o caminho da pasta raiz do projeto, garantindo que o código encontre os arquivos de log e dados independente de onde for executado
ROOT_PATH = Path(__file__).parent

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
            return f"""
            🏦 Agência:\t{conta.agencia}
            🏧Número:\t{conta.numero}
            👤 Titular:\t{conta.cliente.nome}
            💰 Saldo:\t{conta.saldo:.2f}
            """
        except IndexError:
            raise StopIteration
        finally:
            self._contador += 1
# Fim da classe ContaIterador


# Inicio da classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] # cria uma lista vazia para armazenar as conta de um cliente
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
    
    def __repr__(self) -> str:
      return f"<{self.__class__.__name__}: ( '{self.cpf}')>"
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
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor" : transacao.valor,
                "data" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    
    # Aqui esta a implementação do gerador
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao
        

    
    def transacoes_do_dia(self):
        data_atual = datetime.now().date()

        # Cria uma lista vazia para guardar a informação de hoje
        filtradas = []
        for transacao in self.transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()

            # Confere se a data da transacao é igual a data de hoje
            if data_atual == data_transacao:
                filtradas.append(transacao) # Se sim adiciona na lista

        return filtradas # após percorrer tudo retorna a lista cheia ou vazia
        
    # fim da classe Historico


#---- inicio das classes de transação-------
# Inicio da classe Transacao
class Transacao(ABC):
    pass
# fim da classe Transacao


# Inicio da classe Saque que estende Transacao
class Saque(Transacao):
    @property
    @abstractmethod
    def valor(self): 
        pass

    @abstractmethod
    def registrar(self, conta): 
        pass
# Fim da classe Saque


# Inicio da classe Deposito que estende Transacao
class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        conta.Historico.adicionar_transacao(self)
# Fim da classe Deposito


# Aqui esta a parte de decorador de Log
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)

        # Obtém a data e hora atual e formata numa string no formato padrão
        data_hora = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        # modo a = append, que adiciona novas informações no arquivo
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(
            f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"
            )

        return resultado
    
    return envelope

# Aqui fica o menu
def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ======================================
    => """

    # strip faz com que o menu não quebre
    return input(textwrap.dedent(menu_text)).strip().lower()
# Aqui termina o menu

def filtar_cliente(cpf, clientes):
    for cliente in clientes: # FOR será usado para percorrer cada objeto cliente de uma lista de clientes
        if cliente.cpf == cpf: # Verifica se o cpf do objeto é igual ao cpf colocado
            return cliente # Caso encontre ele irá retornar o cliente encontrado
    return None # Se o loop acabar e não encontrar o cliente ele irá retornar None

def recuperar_conta_cliente(cliente):
    pass

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado ❌ ")

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

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
   
    transacoes = conta.historico.gerar_relatorio(tipo_transacao=None)

    for transacao in transacoes:
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "💫 Não foram realizadas movimentações 💫"

    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==============================")


# Aqui começa a função criar_cliente
@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF: ")

    #Após ver o cpf verifica se o cliente já possui cadastro
    cliente = filtar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com este CPF cadastrado")
        return

    nome = input("Infrme o nome completo: ")

    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")

    endereco = input("Informe o endereço: ")

    # Após preencher os dados um novo cliente é cadastrado
    novo_cliente = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)

    # novo_cliente é adicionado a clientes
    clientes.append(novo_cliente)
    print("🎉 Cliente cadastrado com sucesso 🎉")
# Aqui termica a função criar_cliente


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
    
    while True:
        opcao = menu()

        if opcao == "d":
            print("Opção depositar escolhida")
            depositar(clientes)
        elif opcao == "s":
            print("Opção sacar escolhida")
            sacar(clientes)
        elif opcao == "e":
            print("Opção extrato escolhida")
            exibir_extrato(clientes)
        elif opcao == "nu":
            print("Opção criar cliente escolhida")
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n Operação inválida, por favor selecione novamente a operação desejada!")


# Chama a função main
main()