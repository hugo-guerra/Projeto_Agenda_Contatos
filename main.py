from contato import Contato
from agenda import Agenda
import tkinter as tk

janela = tk.Tk()
#LEMBRAR: tk.Tk() -> é a chamada que cria a janela principal da aplicação Tkinter
janela.title("Minha Janela")
janela.geometry("600x700")

label_titulo = tk.Label(janela, text="Agenda de Contatos")
label_titulo.grid(row=0, column=0)

label_nome = tk.Label(janela, text="Nome: ")
label_nome.grid(row=1, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1)

label_telefone = tk.Label(janela, text="Telefone: ")
label_telefone.grid(row=2, column=0)

entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1)

label_email = tk.Label(janela, text="E-mail: ")














janela.mainloop()
#LEMBRAR: mainloop() -> método que inicia o loop principal de eventos do Tkinter, mantém a janela aberta
