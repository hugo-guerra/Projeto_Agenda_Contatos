from contato import Contato
from agenda import Agenda
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
#LEMBRAR: tk.Tk() -> é a chamada que cria a janela principal da aplicação Tkinter
janela.title("Minha Janela")
janela.geometry("600x700")

for i in range(5):
    janela.columnconfigure(i, weight=1)
janela.rowconfigure(7, weight=1)

agenda = Agenda()

label_titulo = tk.Label(janela, text="Agenda de Contatos")
label_titulo.grid(row=0, column=0)

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=1, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, sticky="ew")

label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.grid(row=2, column=0)

entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1, sticky="ew")

label_email = tk.Label(janela, text="E-mail:")
label_email.grid(row=3, column=0)

entry_email = tk.Entry(janela)
entry_email.grid(row=3, column=1, sticky="ew")

label_categoria = tk.Label(janela, text="Categoria:")
label_categoria.grid(row=4, column=0)

entry_categoria = tk.Entry(janela)
entry_categoria.grid(row=4, column=1, sticky="ew")

label_busca = tk.Label(janela, text="Buscar:")
label_busca.grid(row=5, column=0)

entry_busca = tk.Entry(janela)
entry_busca.grid(row=5, column=1, sticky="ew")

id_editado = None

def atualizar_lista():
    lista_contatos.delete(0, tk.END)

    for contato in agenda.listar_contatos():
        lista_contatos.insert(tk.END, f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | E-mail: {contato[3]} | Categoria: {contato[4]}")

def cadastrar():
    nome = entry_nome.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Nome é obrigatório!")
        #LEMBRAR: messagebox.showwarning() -> é uma função do Tkinter que exibe uma caixa de diálogo de aviso para o usuário
    else:
        telefone = entry_telefone.get()
        email = entry_email.get()
        categoria = entry_categoria.get()

        agenda.cadastros_contatos(nome, telefone, email, categoria)

        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)

        atualizar_lista()

def buscar():
    busca = entry_busca.get()
    
    if busca == "":
        messagebox.showwarning("Aviso", "Campo vazio!")
    else:
        resultados = agenda.buscar_contatos(busca)

        lista_contatos.delete(0, tk.END)

        if resultados:
            for contato in resultados:
                lista_contatos.insert(tk.END, f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]} | E-mail: {contato[3]} | Categoria: {contato[4]}")
        else:
            messagebox.showwarning("Aviso", "Nenhum contato encontrado!")

def remover():
    selecao = lista_contatos.curselection() 
    #LEMBRAR: .curselection() -> é usado principalmente em widgets como Listbox do Tkinter para descobrir quais itens estão selecionados pelo usuário
    if selecao:
        texto = lista_contatos.get(selecao[0])
        partes = texto.split(" | ")
        contato_id = int(partes[0].split(" ")[1])

        agenda.remover_contato(contato_id)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Nem um contato foi selecionado!")

def editar():
    global id_editado

    if id_editado is None:
        selecao = lista_contatos.curselection()

        if selecao:
            texto = lista_contatos.get(selecao[0])
            partes = texto.split(" | ")
            id_editado = int(partes[0].split(" ")[1])

            contato = agenda.buscar_por_id(id_editado)

            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, contato[1])

            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, contato[2])

            entry_email.delete(0, tk.END)
            entry_email.insert(0, contato[3])

            entry_categoria.delete(0, tk.END)
            entry_categoria.insert(0, contato[4])

            botao_editar.config(text="Salvar")
        else:
            messagebox.showwarning("Aviso", "Selecione um contato para editar!")
    else:
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        categoria = entry_categoria.get()

        agenda.editar_contato(id_editado, nome, telefone, email, categoria)

        botao_editar.config(text="Editar")
        id_editado = None
        atualizar_lista()

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.grid(row=6, column=0)

botao_buscar = tk.Button(janela, text="Buscar", command=buscar)
botao_buscar.grid(row=6, column=1)

botao_editar = tk.Button(janela, text="Editar", command=editar)
botao_editar.grid(row=6, column=2,)

botao_remover = tk.Button(janela, text="Remover", command=remover)
botao_remover.grid(row=6, column=3,)

botao_limpar = tk.Button(janela, text="Limpar")
botao_limpar.grid(row=6, column=4,)

lista_contatos = tk.Listbox(janela, height=15)
lista_contatos.grid(row=7, column=0, sticky="nsew", columnspan=5)

atualizar_lista()
janela.mainloop()
#LEMBRAR: mainloop() -> método que inicia o loop principal de eventos do Tkinter, mantém a janela aberta
