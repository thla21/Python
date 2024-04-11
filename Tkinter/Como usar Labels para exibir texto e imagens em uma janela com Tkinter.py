########################################################################################
########Como usar Labels para exibir texto e imagens em uma janela com Tkinter##########
########################################################################################

# labels com Tkinter
# Exemplo 1: Label Simples

import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de Labels")

# Criar um label
label = tk.label(janela, text="Aula de labels")

# Empacotar o label na janela
label.pack()

# Loop principal
janela.mainloop()

# Exemplo 2: Label Simples

import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de Labels")

# Mostrar um label comum
label1 = ttk.label(
	janela,
	text = "Texto do Label 1",
	font = "Helvetica", 18)
)
label1.pack(ipadx=10, ipady=30)

# Segundo label
label2 = ttk.label(
	janela,
	text = "Texto do Label 2",
	font = "Arial", 20),
	foreground = "blue"
)
label2.pack(ipadx=10, ipady=60)

janela.mainloop()

# Exemplo 3: Carregando imagem no label

import tkinter as tk
from tkinter import ttk, PhotoImage

def centralizar_imagem(event):
	largura_janela = janela.winfo.width()
	altura_janela = janela.winfo.height()
	largura_imagem = imagem.width()
	altura_imagem = imagem.height()

	posicao_x = (largura_janela - largura_imagem) // 2
	posicao_y = (altura_janela - altura_imagem) // 2

	lb1_imagem.place(x=posicao_x, y=posicao_y)

# Criar janela
janela = tk.Tk()
janela.title("Exibir imagem")
janela.geometry("400x250")

# Carregar a imagem
imagem = PhotoImage(file="<nome do arquivo>")

# Criar label e exibir imagem
lb1_imagem = ttk.Label(janela, image=imagem)

# Centralizar imagem ao reimensionar janela
janela.bind(",Configure>", centralizar_imagem)

# Inserir o label na janela
lbl_imagem.pack(ipady=20)

# Adcionar label comum
lbl_comum = ttk.Label()
	janela,
	text="Treinamentos Ti",
	foreground="purple",
	bakcground="lightgreen",
	anchor="center",
	bordewidth=3,
	relief="groove"
)
lbl_comum.pack(ipadx=10, ipady=20)

# Loop principal
janela.mainloop()
