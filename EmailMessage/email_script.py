from email.message import EmailMessage                            # Chamamos o módulo email.message da bilbioteca EmailMessage
import sntplib
import ssl
import os
import minetypes

email_senha = open('pass', 'r').read()                            # Abrimos o arquivo pass.txt que contém a senha do gmail
email_origem = '<email de origem>'                                # Criamos a instancia do email de origem
email_destino = '<email de destino>'                              # Criamos a instancia do email de destino

assunto = 'Cotação de produtos de TI'
body = open('corpo_email.txt', 'r').read()                        # Abrimos o arquivo corpo_email.txt com permissão read-only e instanciamos para variável body.

mensagem = EmailMessage()                                         # Instaciamos a biblioteca EmailMessage para a variável mensagem.

mensagem["From"] = email_origem
mensagem["To"] = email_destino
mensagem["Subject"] = assunto

mensagem.set_content(body)                                              # 
safe = ssl.create_default_context()                                     # Criamos uma instancia para criptografia ssl do email.

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp      # Passamos como parametros o servidor SMTP do gmail e sua porta 
	smtp.login(email_origem, email_senha)
	smtp.sendmail(email_origem, email_destino, mesagem.as_string())

# Criar um arquivo pass.txt contendo a senha de acesso ao e-mail.

# Criar um arquivo corpo_email.txt com o seguinte conteúdo

"""
Prezados, bom dia"

Gostaria de solicitar uma cotação para ativos de redes wireless, conforme ficou combinado na ligação de ontem.

Att,

Dpto. Egenharia
fone: (xx) xxxx-xxxx
email: xxxxxxxxxxxxxxxxxxxx@xxxxx.com.br
"""
