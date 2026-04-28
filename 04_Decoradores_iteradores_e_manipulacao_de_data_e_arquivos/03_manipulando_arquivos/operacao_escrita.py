# O 'r' faz o Python ignorar os caracteres de escape (\U, \04, \03)
arquivo = open(
    r"C:\Users\Giovanna\Desktop\workspace\dio\formacao_python_fundamentals\04_Decoradores_iteradores_e_manipulacao_de_data_e_arquivos\03_manipulando_arquivos\teste.txt", 
    "w",
    encoding="utf-8" # encoding="utf-8" permite que o arquivo aceite acentos, cedilhas e emojis sem dar erro.
)
arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(['escrevendo', 'um', 'novo', 'texto'])
arquivo.writelines(['\n','escrevendo','\n', 'um','\n', 'novo','\n', 'texto'])
arquivo.writelines(['  escrevendo ', '  outro  ', '  novo  ', '  texto  '])
arquivo.writelines([
    '\n',
    'Bom Dia 🌞',
    '\n',
    'Boa Tarde ⛅',
    '\n',
    'Boa noite 🌙'
])
arquivo.write('\n')
arquivo.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')
arquivo.close()