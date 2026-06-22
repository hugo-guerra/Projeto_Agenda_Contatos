from contato import Contato
from agenda import Agenda
import tkinter as tk

janela = tk.Tk()
#LEMBRAR: tk.Tk() -> é a chamada que cria a janela principal da aplicação Tkinter
janela.title("Minha Janela")
janela.geometry("600x700")

label = tk.Label(janela, text="Agenda de Contatos")
label.grid(row=0, column=0)



janela.mainloop()
#LEMBRAR: mainloop() -> método que inicia o loop principal de eventos do Tkinter, mantém a janela aberta
