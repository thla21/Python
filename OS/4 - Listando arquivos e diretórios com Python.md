O método os.listdir() em Python é usado para obter a lista de todos os arquivos e diretórios no diretório especificado.<br>
Se não especificarmos nenhum diretório, a lista de arquivos e diretórios no diretório de trabalho atual será retornada.

Exemplo: Este código lista todos os arquivos e diretórios no diretório raiz (“/”) .<br>
Ele usa a os.listdirfunção para obter a lista de arquivos e diretórios no caminho especificado e depois imprime os resultados.

```python
import os 
path = "/"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list) 
```

### Saída:

```
Arquivos e diretórios em '/':
['sys', 'run', 'tmp', 'boot', 'mnt', 'dev', 'proc', 'var', 'bin', 'lib64', 'usr',
'lib', 'srv', 'home', 'etc', 'opt', 'sbin', 'media']
```
