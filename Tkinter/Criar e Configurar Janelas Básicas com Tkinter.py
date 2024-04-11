import tkinter as tk			importa a biblioteca tkinter e chamamos um alias nesse caso tk

janela = tk.Tk()			janela recebe a bilioteca tk com o método Tk()

janela.title("Janela Principal")	Definimos o nome da janela
janela.geometry("500x400+200+100")	Definimos a sua geometria altura e largura além do acréscimo de deslocamento
janela.config(bg="ligthblue")		Definimos a cor do plano de fundo (background)

# janela.maxsize(800, 600)		Tamanho máximo de ajuste do redimencionamento da janela
# janela.minsize(300, 200)		Tamanho mínimo de ajuste do redimencionamento da janela
# janela.resizable(false, false)	Permite redimencionamento na altura e largura da janela, podendo também bloquear o ajuste.
# janela.state("zoomed")		Permite iniciar a janela em tela cheia.
# janela.attributes("-alpha", 0.6)	Define o nível de transparência da janela

janela.iconbitmap("thiago-henrique.ico")

janela.mainloop()			Chamamos o loop enquanto o tkiner aguarda algum evento


# Exemplo 02: Abrir outra janela ao clicar na janela principal

import tkinter as tk

def abrir_segunda_janela():
	segunda_janela = tk.Toplevel()
	segunda_janela.title("Segunda Janela")
	segunda_janela.config(bg="20EE70")

# Tamanho da segunda janela
largura_janela = 300
altura_janela = 200

# Obter as dimensões da tela do monitor
largura_tela = segunda_janela.winfo_screenwidth()
altura_tela = segunda_janela.winfo_screenheigth()

# Calcular as coordenadas para centralizar a janela 2
x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

# Definir a geometria da janela 2
segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
