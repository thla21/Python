Considere o Current Working Directory (CWD) como uma pasta onde o Python está operando.<br>
Sempre que os arquivos são chamados apenas pelo nome, o Python assume que ele inicia no CWD,<br>
o que significa que a referência somente ao nome será bem-sucedida apenas se o arquivo estiver no CWD do Python.<br>
Nota: A pasta onde o script Python está sendo executado é conhecida como Diretório Atual. Este não é o caminho onde o script Python está localizado.

#### Obtendo o diretório de trabalho atual:

Para obter a localização do diretório de trabalho atual, os.getcwd() é usado.

Este código usa o módulo ' para obter e imprimir o diretório de trabalho atual (CWD) do script Python.<br>
Ele recupera o CWD usando ' e depois o imprime no console.os'os.getcwd()'

```python
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 
```

##### Resultado:

Diretório de trabalho atual: /home/<usuário>/Desktop/gfg
