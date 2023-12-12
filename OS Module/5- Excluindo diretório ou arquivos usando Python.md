O módulo OS prova diferentes métodos para remover diretórios e arquivos em Python. Estes são:

Usando `os.remove()`<br>
Usando `os.rmdir()`<br>
Usando `os.remove()`

O método os.remove() em Python é usado para remover ou excluir um caminho de arquivo.<br>
Este método não pode remover ou excluir um diretório. Se o caminho especificado for um diretório, OSError será gerado pelo método.

Exemplo: suponha que os arquivos contidos na pasta sejam file1.txt e file2.txt. Este código remove um arquivo chamado “file1.txt”<br>
do local especificado “D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/”. Ele usa a os.remove função para excluir o arquivo no caminho especificado.

```python
import os 
file = 'file1.txt'
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
path = os.path.join(location, file) 
os.remove(path) 
```

#### Saída:

Apenas permanecerá p file2.txt.

### Usando os.rmdir()

O método os.rmdir() em Python é usado para remover ou excluir um diretório vazio.<br>
OSError será gerado se o caminho especificado não for um diretório vazio.

Exemplo: suponha que os diretórios sejam `Nerds` `NerdsforNerds` e `gfg`. Este código tenta remover um diretório chamado `Nerds` localizado em<br>
“D:/Pycharm projects/”. Ele usa a os.rmdir função para excluir o diretório. Se o diretório estiver vazio, ele será removido.<br>
Se contiver arquivos ou subdiretórios, você poderá encontrar um erro.

```python
import os 
directory = "Nerds"
parent = "D:/Pycharm projects/"
path = os.path.join(parent, directory) 
os.rmdir(path) 
```

#### Saída:


