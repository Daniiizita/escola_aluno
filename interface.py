import tkinter as tk
from tkinter import ttk

# Define a janela principal
janela = tk.Tk()
janela.title("Gerenciamento de Alunos")

# Define um frame para o formulário de cadastro
frame_cadastro = ttk.Frame(janela)
frame_cadastro.pack()

# Define os rótulos para o formulário de cadastro
lbl_nome = ttk.Label(frame_cadastro, text="Nome:")
lbl_data_nascimento = ttk.Label(frame_cadastro, text="Data de Nascimento:")
lbl_situacao = ttk.Label(frame_cadastro, text="Situação:")

# Define os campos de entrada para o formulário de cadastro
txt_nome = ttk.Entry(frame_cadastro)
txt_data_nascimento = ttk.Entry(frame_cadastro)
txt_situacao = ttk.Entry(frame_cadastro)

# Define os botões para o formulário de cadastro
btn_cadastrar = ttk.Button(frame_cadastro, text="Cadastrar")
btn_limpar = ttk.Button(frame_cadastro, text="Limpar")

# Define a posição dos widgets no formulário de cadastro
lbl_nome.grid(row=0, column=0)
txt_nome.grid(row=0, column=1)
lbl_data_nascimento.grid(row=1, column=0)
txt_data_nascimento.grid(row=1, column=1)
lbl_situacao.grid(row=2, column=0)
txt_situacao.grid(row=2, column=1)
btn_cadastrar.grid(row=3, column=0)
btn_limpar.grid(row=3, column=1)

# Define um frame para a tabela de alunos
frame_tabela = ttk.Frame(janela)
frame_tabela.pack()

# Define a tabela de alunos
tabela_alunos = ttk.Treeview(frame_tabela)
tabela_alunos["columns"] = ("Nome", "Data de Nascimento", "Situação")
tabela_alunos.column("#0", width=0, stretch=False)
tabela_alunos.column("Nome", width=200)
tabela_alunos.column("Data de Nascimento", width=100)
tabela_alunos.column("Situação", width=100)
tabela_alunos.heading("#0", text="ID")
tabela_alunos.heading("Nome", text="Nome")
tabela_alunos.heading("Data de Nascimento", text="Data de Nascimento")
tabela_alunos.heading("Situação", text="Situação")

# Define um botão para adicionar um novo aluno
btn_adicionar = ttk.Button(frame_tabela, text="Adicionar")

# Define a posição dos widgets na tabela de alunos
tabela_alunos.grid(row=0, column=0, sticky="nsew")
btn_adicionar.grid(row=1, column=0, sticky="nsew")

# Define a função para cadastrar um novo aluno
def cadastrar_aluno():
    # Obtém os dados do formulário
    nome = txt_nome.get()
    data_nascimento = txt_data_nascimento.get()
    situacao = txt_situacao.get()

    # Adiciona o aluno à tabela
    tabela_alunos.insert("", "end", values=(nome, data_nascimento, situacao))

# Define a função para limpar os campos do formulário
def limpar_campos():
    txt_nome.delete(0, tk.END)
    txt_data_nascimento.delete(0, tk.END)
    txt_situacao.delete(0, tk.END)

# Define a função para adicionar um novo aluno
btn_cadastrar.config(command=cadastrar_aluno)

# Define a função para limpar os campos do formulário
btn_limpar.config(command=limpar_campos)

# Inicializa a janela
janela.mainloop()
