# DESAFIO

## Introdução

Com os novos conhecimentos adquiridos sobre decoradores, geradores e iteradores, você foi engarregado de
implementar as aseguintes funcionalidades no sistema:

- Decorador de log
- Gerador de relatórios
- Iterador personalizado

### Decorador de log
Implemente um decorador que seja aplicado a todas as funções de transações(depósito, saque, crição de 
conta,etc).Esse decorador deve registrar(printar) a data e hora de cada transação, bem como o tipo de transação.

### Gerador de relatórios
Crie um gerador que permita iterar sobre as transações de uma conta e retorne , uma a uma, as transações
que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo
(por exemplo, apenas saques ou apenas depósitos).

### Iterador personalizado
Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco,
retornando informações básicas de cada conta(número, saldo atual, etc)

Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes
funcionalidades no sistema:

- Estabelecer um limite de 10 transações diárias para uma conta
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o
número de transações permitidas para aquele dia.
- Mostre no extrato, a data e hora de todas as transações.