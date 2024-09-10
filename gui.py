import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from sqlalchemy.orm import Session
from services import *




def tela_inicial():
    # Criar a janela principal
    root = tk.Tk()
    root.title("Gerenciamento de Corridas")
    root.geometry("800x600") # Definir o tamanho da janela

    # Carregar a imagem
    try:
        imagem = Image.open("C:/Users/maiar/Downloads/image.png")  # Colocar caminho da pasta do projeto
        imagem = imagem.resize((500, 400), Image.LANCZOS)  # Redimensionar a imagem
        img = ImageTk.PhotoImage(imagem)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        img = None

    # Exibir a imagem na tela
    if img:
        lbl_imagem = tk.Label(root, image=img)
        lbl_imagem.grid(row=0, column=0, columnspan=2)

    # Criar os botões
    btn_cadastrar_corredor = ttk.Button(root, text="Cadastrar Corredor", command=lambda: tela_corredor(root))
    btn_cadastrar_corredor.grid(row=1, column=0, pady=10)

    btn_cadastrar_evento = ttk.Button(root, text="Cadastrar Evento", command=lambda: tela_evento(root))
    btn_cadastrar_evento.grid(row=1, column=1, pady=30)

    btn_cadastrar_categoria = ttk.Button(root, text="Cadastrar Categoria", command=lambda: tela_categoria(root))
    btn_cadastrar_categoria.grid(row=3, column=0, pady=10)

    btn_visualizar_dados = ttk.Button(root, text="Visualizar Dados", command=lambda: tela_consulta(root))
    btn_visualizar_dados.grid(row=4, column=0, pady=10)

    root.mainloop()

def tela_corredor(root): 
    telacorredor = tk.Toplevel(root) # criar tratamento para não deixar abrir mais de uma tela
    telacorredor.title("Cadastro corredor")
    telacorredor.geometry("800x600") 

    # Frames
    labelframe = ttk.Labelframe(telacorredor, text="Informações do Corredor", padding=(10, 10))
    labelframe.pack(side=tk.LEFT,anchor=tk.NW, padx=20, pady=20)
    content_frame = ttk.Frame(labelframe)
    content_frame.pack(padx=10, pady=10)

    # Variáveis para armazenar os valores dos inputs
    nome_str = tk.StringVar()
    idade_int = tk.IntVar()
    sexo_int = tk.IntVar()  
    ativo_int = tk.IntVar(value=1)  

    # Campo de entrada para o nome
    lbl_nome = ttk.Label(content_frame, text="Nome do Corredor: ")
    lbl_nome.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entry_nome = ttk.Entry(content_frame, textvariable=nome_str)
    entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

    # Campo de entrada para a data de nascimento
    lbl_data = ttk.Label(content_frame, text="Idade: ")
    lbl_data.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entry_data = ttk.Entry(content_frame, textvariable=idade_int)
    entry_data.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

    # Radio buttons para selecionar o sexo
    lbl_sexo = ttk.Label(content_frame, text="Sexo: ")
    lbl_sexo.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    radio_feminino = ttk.Radiobutton(content_frame, text="Feminino", variable=sexo_int, value=0)
    radio_feminino.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
    radio_masculino = ttk.Radiobutton(content_frame, text="Masculino", variable=sexo_int, value=1)
    radio_masculino.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

    # Checkbutton para definir se o corredor está ativo.
    check_ativo = ttk.Checkbutton(content_frame, text="Ativo", variable=ativo_int)
    check_ativo.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.W)

    # Botão para salvar o corredor
    btn_salvar = ttk.Button(content_frame, text="Salvar", command=lambda: salvar_corredor(
        nome_str.get(),
        idade_int.get(),
        sexo_int.get(),
        ativo_int.get()
    ))
    btn_salvar.grid(row=4, column=0, columnspan=3, pady=10, sticky=tk.E)



def tela_evento(root):
    telaevento = tk.Toplevel(root) # criar tratamento para não deixar abrir mais de uma tela
    telaevento.title("Cadastrar evento")
    telaevento.geometry("800x600")

def tela_categoria (root):
    telacategoria = tk.Toplevel(root) # criar tratamento para não deixar abrir mais de uma tela
    telacategoria.title("Cadastrar categoria")
    telacategoria.geometry("800x600")

def tela_consulta (root):
    telaconsulta = tk.Toplevel(root)
    telaconsulta.title ("Consultas")
    telaconsulta.geometry("1600x1200")
