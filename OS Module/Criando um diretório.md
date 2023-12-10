Existem diferentes métodos disponíveis no módulo OS para criar um diretório. Estes são:

`os.mkdir()`<br>
`os.makedirs()`<br>

#### Usando `os.mkdir()`:

O método `os.mkdir()` em Python é usado para criar um diretório chamado path com o modo numérico especificado. Este método gera FileExistsError se o diretório a ser criado já existir.

Exemplo:<br>
Este código cria dois diretórios: “nerdfornerd ” dentro do diretório “D:/Pycharm Projects/” e “Nerd” dentro do diretório “D:/Pycharm Projects”.<br>
O primeiro diretório é criado usando o `os.mkdir()` método sem especificar o modo.<br>
O segundo diretório é criado usando o mesmo método, mas é fornecido um modo específico ( ), que concede permissões de leitura e gravação.<br>
O código então imprime mensagens para indicar que os diretórios foram criados.0o666

```python
import os
directory = "nerdfornerd"
parent_dir = "D:/Pycharm projects/"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "Nerd"
parent_dir = "D:/Pycharm projects"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
```

#### Saída:

```
Diretório 'GeeksforGeeks' criado 
Diretório 'Geeks' criado
```
