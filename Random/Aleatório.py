import random							                                        # importamos o módulo random


valor = random.randint(1,30)					                            # Geramos um número aleatório no range de 1 a 30 e jogamos o resultado na variável valor
print(valor)							                                        # Exiba valor


# Gerando 5 números aleatórios inteiros num determinado range.

print('Gerar cinco números aleatórios entre 1 e 40: \n')	
for i in range(5):						                                    # Laço para gerar 5 números aleatórios do range entre 1 e 40.
	n = random.randint(1,40)				                                # Gera um número aleatório entre 1 e 40 e joga na variável n
	print(f'Número gerando: {n}')


# Gerando um número aleatório do tipo fluante

valor = random.random()						                                # Gera um número flutuante entre 0 e 1 e joga na variável valor
print(valor)							                                        # Exiba valor
print(f'Número gerado: {valor * 10}')				                      # Gera um número flutuante entre 1 e 10 e exibe

# Podemos ainda melhorar a saída com apenas duas casas decimais
print(f'Número gerado: {round(valor * 10, 2)}')

valor = random.uniform(1,100)
