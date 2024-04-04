import os
import shutil
import time

diretorio_origem = 'C:\\caminho\do\diretorio_origem'                  # Diretório de origem
diretorio_destino = 'C:\\caminho\do\diretorio_destino'                # Diretório de destino


def clonar_arquivos(origem, destino):                              # Criamos uma nova função para clonar arquivos de um diretório para outro
    for root, dirs, files in os.walk(origem):
        for file in files:
            origem_arquivo = os.path.join(root, file)
            destino_arquivo = os.path.join(destino, file)
            shutil.copy2(origem_arquivo, destino_arquivo)
            print(f'Arquivo {file} clonado com sucesso!')


def verificar_novos_arquivos(diretorio):                           # Criamos uma nova função para verificar novos arquivos no diretório
    arquivos_anteriores = set(os.listdir(diretorio))
    while True:
        time.sleep(3600)                                           # Espera 1 hora (3600 segundos)
        arquivos_atuais = set(os.listdir(diretorio))
        novos_arquivos = arquivos_atuais - arquivos_anteriores
        if novos_arquivos:
            print("Novos arquivos encontrados:")
            for arquivo in novos_arquivos:
                print(arquivo)
            arquivos_anteriores = arquivos_atuais


clonar_arquivos(diretorio_origem, diretorio_destino)               # Clonar os arquivos inicialmente


verificar_novos_arquivos(diretorio_origem)                         # Iniciar verificação de novos arquivos a cada hora
