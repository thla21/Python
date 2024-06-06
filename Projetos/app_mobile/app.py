import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro App"

    def cadastrar(e)
        print(produto.value)
        print(preco.value)

    txt_titulo=ft.Text("Títuulo do produto")
    produto = ft.TextField(label="Digite o título do produto", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do Produto')
    preco = ft.TextField(value="0", label="Digite o preço do produto", text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )
    
ft.app(target=main)