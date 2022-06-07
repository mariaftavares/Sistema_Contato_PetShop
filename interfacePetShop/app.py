from tkinter import *
from tkinter import ttk
import banco
from tkinter import messagebox


def pesquisarContato():
    listacontato.delete(*listacontato.get_children())
    t_nomepet = vnomepet.get()
    if(t_nomepet != ""):
        query = "SELECT * FROM CONTATOS WHERE NOME_PET LIKE '%"+t_nomepet+"%' "
        linha = banco.pesquisa(query)
        for i in linha:
            listacontato.insert("","end",values=i)

def popular():
    listacontato.delete(*listacontato.get_children())
    query = "SELECT * FROM CONTATOS ORDER BY ID "
    linhas = banco.pesquisa(query)
    for i in linhas:
        listacontato.insert("","end",values=i)
def alterarContato (idselecionado,vnome,vnomep,vraca,vidade,vcontato):
    if(vnomep!= "" and vcontato != ""):
        t_id = idselecionado
        t_nome =vnome
        t_nomep = vnomep
        t_raca= vraca
        t_idade= vidade
        t_contato= vcontato
        listacontato.delete(*listacontato.get_children())
        query1 = "UPDATE contatos SET NOME_PET = '"+t_nomep+"',NOME_RESPONSAVEL = '"+t_nome+"', RACA = '"+t_raca+"',IDADE = '"+t_idade+"',CONTATO = '"+t_contato+"' WHERE id in ('"+t_id+"')"
        banco.alterar(query1)
        query = "SELECT * FROM CONTATOS ORDER BY ID "
        linhas = banco.pesquisa(query)
        for i in linhas:
            listacontato.insert("","end",values=i)
        messagebox.showinfo(title = "Atualizar",message="Contato alterado com sucesso!")
    else:
         messagebox.showerror(title = "Erro ao atualizar",message="Os campos nome do pet e contato estão vazio, por favor informar.")    

def inserir (vnome,vnomep,vraca,vidade,vcontato):
    t_nome =vnome
    t_nomep = vnomep
    t_raca= vraca
    t_idade= vidade
    t_contato= vcontato
    if (t_nomep != "" and vcontato != "" ):
        listacontato.delete(*listacontato.get_children())
        query1 = "INSERT INTO contatos(NOME_RESPONSAVEL,NOME_PET,RACA,IDADE,CONTATO) VALUES ('"+t_nome+"','"+t_nomep+"','"+t_raca+"','"+t_idade+"','"+t_contato+"')"
        banco.alterar(query1)
        messagebox.showinfo(title = "Cadastro",message="Contato cadastrado com sucesso!")
        query = "SELECT * FROM CONTATOS ORDER BY ID "
        linhas = banco.pesquisa(query)
        for i in linhas:
            listacontato.insert("","end",values=i)
        
    else:
        messagebox.showerror(title = "Erro ao cadastrar",message="Nao foi informado o nome pet ou o contato, por favor inserir, sao dados obrigatorios")

def excluir():
    try:
        itemSelecionado = listacontato.selection()[0]
        valores = listacontato.item(itemSelecionado,"values")
        idselecionado = valores[0]
        query1 = " DELETE FROM contatos WHERE id in ('"+idselecionado+"')"
        messagebox.showinfo(title = "Excluir",message="Contato excluido com sucesso!")
        banco.alterar(query1)
        listacontato.delete(*listacontato.get_children())
        query = "SELECT * FROM CONTATOS ORDER BY ID "
        linhas = banco.pesquisa(query)
        for i in linhas:
            listacontato.insert("","end",values=i)
    except:
        messagebox.showerror(title = "Erro ao excluir",message="Nao foi selecionado o contato que deseja excluir.")  


   

def adicionar():
    inserirContato = Toplevel(app)
    inserirContato.title("Cadastrar Contato")
    inserirContato.geometry("500x300")
    inserirContato.configure(background="#FFEEEE")
    Label(inserirContato,text = "Nome do Responsavel:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=20,width=130,height=20)
    vnome = Entry(inserirContato)
    vnome.place(x=10,y=40,width=200,height=20)
    Label(inserirContato,text = "Nome do pet:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=60,width=100,height=20)
    vnomep = Entry(inserirContato)
    vnomep.place(x=10,y=80,width=200,height=20)
    Label(inserirContato,text = "Raca:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=102,width=100,height=20)
    vraca = Entry(inserirContato)
    vraca.place(x=10,y=120,width=100,height=20)
    Label(inserirContato,text = "Idade:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=140,width=100,height=20)
    vidade = Entry(inserirContato)
    vidade.place(x=10,y=160,width=70,height=20)
    Label(inserirContato,text = "Contato:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=180,width=100,height=20)
    vcontato = Entry(inserirContato)
    vcontato.place(x=10,y=200,width=150,height=20)
    Button(inserirContato,text="Cadastrar",bg='#ECE5C7',command=lambda:[inserir(vnome.get(),vnomep.get(),vraca.get(),vidade.get(),vcontato.get()),inserirContato.destroy()]).place(x=10,y=240,width=100,height=20)
    

def atualizar():
    try:
        itemSelecionado = listacontato.selection()[0]
        valores = listacontato.item(itemSelecionado,"values")
        idselecionado = valores[0]
        atualizarContato = Toplevel(app)
        atualizarContato.title("Atualizar Contato")
        atualizarContato.geometry("500x300")
        atualizarContato.configure(background="#FFEEEE")
        Label(atualizarContato,text = "Nome do Responsavel:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=20,width=130,height=20)
        vnome = Entry(atualizarContato)
        vnome.place(x=10,y=40,width=200,height=20)
        Label(atualizarContato,text = "Nome do pet:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=60,width=100,height=20)
        vnomep = Entry(atualizarContato)
        vnomep.place(x=10,y=80,width=200,height=20)
        Label(atualizarContato,text = "Raca:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=100,width=100,height=20)
        vraca = Entry(atualizarContato)
        vraca.place(x=10,y=120,width=100,height=20)
        Label(atualizarContato,text = "Idade:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=140,width=100,height=20)
        vidade = Entry(atualizarContato)
        vidade.place(x=10,y=160,width=70,height=20)
        Label(atualizarContato,text = "Contato:",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=180,width=100,height=20)
        vcontato = Entry(atualizarContato)
        vcontato.place(x=10,y=200,width=150,height=20)
        Button(atualizarContato,text="Alterar",bg='#ECE5C7',command=lambda:[alterarContato(idselecionado,vnome.get(),vnomep.get(),vraca.get(),vidade.get(),vcontato.get()),atualizarContato.destroy()]).place(x=10,y=240,width=100,height=25)
        
        
    except:
        messagebox.showerror(title = "Erro ao atualizar",message="Nao foi selecionado o contato que deseja atualizar.")       



def participantes():
    participantes = Toplevel(app)
    participantes.title("Participantes do grupo:")
    participantes.geometry("400x200")
    participantes.configure(background="#FFEEEE")
    Label(participantes,text="Nomes:",background="#FFEEEE",foreground ="#000000").place(x=5,y=20,width=50,height=20)
    Label(participantes,text="Maria Fernanda Moreira Tavares |Matricula =202009230849 ",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=40,width=350,height=20)
    Label(participantes,text="Leticia Silva Carvalho |Matricula = 202009230831",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=60,width=350,height=20)
    Label(participantes,text="Lauriane Da Silva Almeida |Matricula = 202103258964",background="#FFEEEE",foreground ="#000000",anchor=W).place(x=10,y=80,width=350,height=20)



    

app = Tk()
app.title("Pet Shop")
app.geometry("730x450")
app.configure(background = "#C1F4C5")
#####################################
quadroContatos = LabelFrame(app,text="Lista de Contatos",bg='#FFBED8')
quadroContatos.pack(fill="both",expand="yes",padx=10,pady=10)
listacontato = ttk.Treeview(quadroContatos,columns =('id','pet','responsavel','raca','idade','contato'),show='headings')
listacontato.column('id',minwidth=0,width=100)
listacontato.column('pet',minwidth=0,width=100)
listacontato.column('responsavel',minwidth=0,width=250)
listacontato.column('raca',minwidth=0,width=100)
listacontato.column('idade',minwidth=0,width=50)
listacontato.column('contato',minwidth=0,width=100)
listacontato.heading('id',text='ID')
listacontato.heading('pet',text='PET')
listacontato.heading('responsavel',text='RESPONSAVEL')
listacontato.heading('raca',text='RAÇA')
listacontato.heading('idade',text='IDADE')
listacontato.heading('contato',text='CONTATO')
listacontato.pack()
popular()
##################################
quadropesquisar = LabelFrame(app,text="Pesquisar contatos",bg='#FFBED8')
quadropesquisar.pack(fill="both",expand="yes",padx=10,pady=10)
Label(quadropesquisar,text = "Nome do pet:",bg='#FFBED8',foreground ="#000000",anchor=W).place(x=5,y=5,width=80,height=20)
vnomepet = Entry(quadropesquisar)
vnomepet.place(x=100,y=5,width=100,height=20)
buttonPesquisar = Button(quadropesquisar,text='Pesquisar',bg='#ECE5C7',command = pesquisarContato)
buttonPesquisar.place(x=210,y=5,width=100,height=23)
buttonMostratd = Button(quadropesquisar,text='Mostra Todos',bg='#ECE5C7',command = popular)
buttonMostratd.place(x=320,y=5,width=100,height=23)
######################################
quadroOpcoes = LabelFrame(app,text="Opções",bg='#FFBED8')
quadroOpcoes.pack(fill="both",expand="yes",padx=10,pady=10)
buttonInserir = Button(quadroOpcoes,text='Adicionar Contato',bg='#ECE5C7',command = adicionar)
buttonInserir.place(x=60,y=3,width=150,height=23)
buttonAtualizar =Button(quadroOpcoes,text='Atualizar Contato',bg='#ECE5C7',command = atualizar)
buttonAtualizar.place(x=250,y=3,width=150,height=23)
buttonExcluir =Button(quadroOpcoes,text='Excluir Contato',bg='#ECE5C7',command = excluir)
buttonExcluir.place(x=440,y=3,width=150,height=23)
#######################################
menubar = Menu(app,background='#C1F4C5')
app.config(menu=menubar)
sobre_menu = Menu(menubar,background='#C1F4C5')

sobre_menu.add_command(
    label='Participantes',
    command=participantes
)
sobre_menu.add_command(
    label='Exit',
    command=app.destroy
)


menubar.add_cascade(
    label="Sobre",
    menu=sobre_menu
)



app.mainloop()