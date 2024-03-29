# Criando um ambiente virtual

1- Abra o Powershell como Administrador da máquina e digite seguinte comando:

```ps
Set-ExecutionPolicy Unrestricted -Force
```

Este comando alterar a política de execução de scripts, permitindo a execução de scripts sem restrições de segurança atráves do PowerShell

2 - Crie um ambiente venv com nome do seu gosto:

```ps
python -m venv myvenv
```

Acoselho antes de digitar este programa, entrar no diretório atual dos seus projetos

3- Ppor fim ative o seu venv recém criado da seguinte maneira:

```ps
.\myvevn\Scripts\activate
```

Agora estamos dentro do ambiente virtual, para verificar se deu tudo certo digite o seguinte comando:

```ps
pip list
```
