import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import cadastro_cursor
import tela_cadastro
import tela_livro
import tela_material
import tela_acervo


#cores--------------------------------------------------------------------------------------------
cor1 = "#ffffff"  # branca

#janela------------------------------------------------------------------------------------------
def show(data):
    janela_adm = tk.Toplevel()
    janela_adm.title("Administrador")
    janela_adm.geometry("800x600")
    janela_adm.configure(background=cor1)
    janela_adm.resizable(width=False, height=False)

    def consultar():
        tela_acervo.show_acervo(data)

#Dividindo a janela------------------------------------------------------------------------------------------
    barra_titulo = Frame(janela_adm, width=800, height=200, relief="flat")
    barra_titulo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    barra_dados = Frame(janela_adm, width=800, height=400, relief="flat")
    barra_dados.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    tk.Label(barra_titulo, text="Menu Administrador", font=("Verdana", 30, "bold")).grid(padx=250)

    botao_login = tk.Button(barra_dados, text="Cadastrar Livros",font=("Verdana", 12, "bold"),  command=lambda: tela_livro.show_cadastro(data))
    botao_login.grid()

    botao_login = tk.Button(barra_dados, text="Cadastrar Materiais Didáticos",font=("Verdana", 12, "bold"),  command=lambda: tela_material.show_cadastro(data))
    botao_login.grid()

    botao_cadastro = tk.Button(barra_dados, text="Cadastrar Usuários", font=("Verdana", 12, "bold"), command=lambda:tela_cadastro.show_cadastro(data))
    botao_cadastro.grid()
    
    botao_consulta = tk.Button(barra_dados, text="Consultar Acervo",font=("Verdana", 12, "bold"), command=lambda:consultar(data))
    botao_consulta.grid()
                
    # janela_menu.mainloop()
