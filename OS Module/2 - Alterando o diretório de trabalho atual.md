Para alterar o diretório de trabalho atual (CWD), o método os.chdir() é usado.<br>
Este método altera o CWD para um caminho especificado. Leva apenas um único argumento como um novo caminho de diretório.<br>
Nota: O diretório de trabalho atual é a pasta na qual o script Python está operando.

Exemplo: o código verifica e exibe o diretório de trabalho atual (CWD) duas vezes: antes e depois de alterar o diretório um nível acima usando.<br>
Ele fornece um exemplo simples de como trabalhar com o diretório de trabalho atual em Python. os.chdir('../')

```python
import os 
def current_path(): 
	print("Current working directory before") 
	print(os.getcwd()) 
	print() 
current_path() 
os.chdir('../') 
current_path() 
```

#### Saída:

```
Diretório de trabalho atual antes de 
C:\Users\Nikhil Aggarwal\Desktop\gfg 
Diretório de trabalho atual depois de 
C:\Users\Nikhil Aggarwal\Desktop
```
