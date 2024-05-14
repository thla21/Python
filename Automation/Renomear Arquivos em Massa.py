import os

os.chdir('C:\\Teste')                                                                      # Definimos o diretório onde será executado o código.
print(f'Diretório atual: {os.getcwd()}')                                                   # Exibimos o diretório referente.

padrao_nome =  input('Qual o padrão de nomes de arquivos a usar (sem a extensão)? ')       # Criamos uma variável que recebe uma entrada de dados.

for contador, arq in enumerate(os.listdir()):                                              # Criamos um laço for com duas variáveis (contador e arq) onde é arq é o arquivo a ser mudado.
	if os.path.isfile(arq):                                                                  # Criamos a condicional 'if' para identificar apenas arquivos a serem modificados seus nomes.
		name_arq, exten_arq = os.path.splitext(arq)                                            # Separamos a extensão do nome do arquivo con a função os.path.splitext().
		nome_arq = padrao_nome + ' ' + str(contador)                                           # A variável nome_arq recebe a variável padrao_nome mais a função string da variável contador.

		nome_novo = f'{nome_arq}{exten_arq}'                                                   # A variável nome_novo recebe a variável nome_arq mais a exten_arq.
		os.rename(arq, nome_novo)                                                              # O nome da atual variável arq recebe o nome da variável nome_novo.

print(f'\nArquivos Renomeados! ')
