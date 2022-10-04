from tkinter import*
from tkinter import Tk, StringVar, ttk
from xml.dom.minidom import Entity
from tkcalendar import Calendar, DateEntry
from datetime import datetime
from PIL import Image, ImageTk 

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


frameCima = Frame(janela, width = 1043, height = 50, bg = co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg = co1, pady = 20, relief="flat")
frameMeio.grid(row=1, column=0, pady = 1, padx= 0, sticky = NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg = co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady = 0, padx= 1, sticky = NSEW)

app_img = Image.open("caderno.jpg")
app_img = app_img.resize((45,45)) 
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text = "Inventário Doméstico", width = 900, compound=LEFT, relief=RAISED, anchor = NW, font = ('Verdana 20 bold'), bg = co1, fg = co4) 
app_logo.place(x=0, y=0)


#Criando entradas

l_nome = Label(frameMeio, text = "Nome", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width = 30, justify = "left", relief = "solid")
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text = "Sala/Área", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width = 30, justify = "left", relief = "solid")
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text = "Descrição", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width = 30, justify = "left", relief = "solid")
e_descricao.place(x=130, y=71)

l_model = Label(frameMeio, text = "Marca/Modelo", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width = 30, justify = "left", relief = "solid")
e_model.place(x=130, y=101)

l_cal = Label(frameMeio, text = "Data de Compra", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width = 30, justify = "left", relief = "solid")
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text = "Valor da compra", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width = 30, justify = "left", relief = "solid")
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text = "Número de série", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width = 30, justify = "left", relief = "solid")
e_serial.place(x=130, y=191)


#Criando botões
l_carregar = Label(frameMeio, text = "Carregar Imagem", font = ('Verdana 10 bold'), bg = co1, fg = co4, height = 1, anchor = NW)
l_carregar.place(x=10, y=220)
botao_carregar = Button(frameMeio, compound = CENTER, anchor= CENTER, text = "Carregar".upper(), width = 30, overrelief = RIDGE, font=("Ivy 8"), bg = co1, fg = co0)
botao_carregar.place(x=130, y=221)

img_add = Image.open("add.jpg")
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button(frameMeio, image = img_add,  compound = LEFT, anchor = NW, text = "Adicionar".upper(), width = 95, overrelief = RIDGE, font=("Ivy 8"), bg = co1, fg = co0)
botao_inserir.place(x=330, y=10)

img_update = Image.open("reload.jpg")
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)
botao_atualizar = Button(frameMeio, image = img_update,  compound = LEFT, anchor = NW, text = "Atualizar".upper(), width = 95, overrelief = RIDGE, font=("Ivy 8"), bg = co1, fg = co0)
botao_atualizar.place(x=330, y=50)

img_item = Image.open("carregar.jpg")
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)
botao_ver = Button(frameMeio, image = img_item,  compound = LEFT, anchor = NW, text = "Ver item".upper(), width = 95, overrelief = RIDGE, font=("Ivy 8"), bg = co1, fg = co0)
botao_ver.place(x=330, y=221)

img_delete = Image.open("remove.jpg")
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frameMeio, image = img_delete,  compound = LEFT, anchor = NW, text = "Deletar".upper(), width = 95, overrelief = RIDGE, font=("Ivy 8"), bg = co1, fg = co0)
botao_deletar.place(x=330, y=90)

l_total = Label(frameMeio, text = "Total de itens", font = ('Ivy 17 bold'), bg = co7, fg = co1, relief=FLAT,height = 2, width = 14,anchor = CENTER)
l_total.place(x=450, y=17)
l_valor_total = Label(frameMeio, text="Valor total de todos os itens ", anchor = NW, font = ('Ivy 10 bold'), bg = co7, fg = co1)
l_valor_total.place(x=450, y = 12)

#Quantidade total de itens
l_qtd = Label(frameMeio, font = ('Ivy 25 bold'), bg = co7, fg = co1, relief=FLAT,height = 2, width = 10,anchor = CENTER)
l_qtd.place(x=450, y=90)
l_qtd_itens = Label(frameMeio, text="Quantidade total de itens ", anchor = NW, font = ('Ivy 10 bold'), bg = co7, fg = co1)
l_qtd_itens.place(x=460, y = 92)

def mostrar():
    tabela_head = ["#Item", "Nome", "Sala/Área", "Descrição", "Marca/Modelo", "Data de Compra", "Valor da compra", "Número de série"]

    lista_itens = []

    tree = ttk.Treeview(frameBaixo, selectmode="extended", columns=tabela_head, show="headings")
    vsb =ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='EW')

    hd = ["center", "center", "center", "center", "center", "center", "center", "center"]
    h  = [40, 150, 100, 160, 130, 100, 100, 100]

    n = 0

    for co1 in tabela_head:
        tree.heading(co1, text=co1.tile(), anchor=CENTER)
        tree.column(co1, width=h[n], anchor=hd[n])
        n += 1
    for item in lista_itens:
        tree.insert("", "end", values=item)    

     

janela.mainloop()


