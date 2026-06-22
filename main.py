from contato import Contato
from agenda import Agenda
import tkinter as tk

janela = tk.Tk()
#LEMBRAR: tk.Tk() -> é a chamada que cria a janela principal da aplicação Tkinter
janela.title("Minha Janela")
janela.geometry("600x700")

agenda = Agenda()

label_titulo = tk.Label(janela, text="Agenda de Contatos")
label_titulo.grid(row=0, column=0)

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=1, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1)

label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.grid(row=2, column=0)

entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1)

label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=3, column=0)

entry_email = tk.Entry(janela)
entry_email.grid(row=3, column=1)

label_categoria = tk.Label(janela, text="Categoria:")
label_categoria.grid(row=4, column=0)

entry_categoria = tk.Entry(janela)
entry_categoria.grid(row=4, column=1)

def cadastrar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    categoria = entry_categoria.get()

    agenda.cadastros_contatos(nome, telefone, email, categoria)

    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.grid(row=5, column=0)

botao_buscar = tk.Button(janela, text="Buscar")
botao_buscar.grid(row=5, column=1)

botao_limpar = tk.Button(janela, text="Limpar")
botao_limpar.grid(row=5, column=2)

lista_contatos = tk.Listbox(janela, width=60, height=15)
lista_contatos.grid(row=6, column=0)

def atualizar_lista():
    lista_contatos.delete(0, tk.END)

    for contato in agenda.listar_contatos():
        lista_contatos.insert(tk.END, f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | E-mail: {contato[3]} | Categoria: {contato[4]}")















janela.mainloop()
#LEMBRAR: mainloop() -> método que inicia o loop principal de eventos do Tkinter, mantém a janela aberta
