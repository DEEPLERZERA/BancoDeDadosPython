from tkinter import*
from tkinter import Tk, StringVar, ttk

################# cores ###############
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde


janela = Tk()
janela.title("")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(height= FALSE, width= FALSE)
style = ttk.Style(janela)
style.theme_use("clam")

janela.mainloop()