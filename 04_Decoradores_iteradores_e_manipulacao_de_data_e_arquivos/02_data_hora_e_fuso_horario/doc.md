## Trabalhando com objetos date, datetime e time

- Link da documentação do Python
datetime
🔗: https://docs.python.org/pt-br/3.14/library/datetime.html#module-datetime

O objeto **timedelta** representa uma duração, a diferença entre duas datas ou horas.

### strftime (Date $\rightarrow$ String)
Você usa o *strftime* quando já tem a data no Python e quer "enfeitá-la" para mostrar ao usuário final.

### trptime (String $\rightarrow$ Date)
Você usa o *strptime* quando recebe um texto (de um input, de um arquivo de texto ou de um banco de dados) e precisa que o Python entenda que aquilo é uma data para poder fazer cálculos ou comparações.