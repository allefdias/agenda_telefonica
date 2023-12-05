from tkinter import *
from tkinter import ttk
from tkinter import  messagebox

agenda = [
    {'nome': 'Jonas', 'telefone': '859888-3333','categoria': 'Amigos'}
]

index = None



#COMO LISTAR ITENS EM UMA TABELA
def atualizarTabela():
    # LIMPANDO A TABELA
    # get_children -> Retorna as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)
    #PARA CADA CONTATO NA LISTA CRIA-SE UMA NOVA LINHA
    for contato in agenda:
        tabela.insert("", END, values=(contato['nome'],
                                              contato['telefone'],
                                              contato['categoria']))



def limparCampos():
    txtNome.delete(0,END)
    txtTelefone.delete(0,END)
    comboCategoria.set('')

def adicionarContato():
    nome = txtNome.get()
    telefone = txtTelefone.get()
    categoria = comboCategoria.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    agenda.append(contato)
    messagebox.showinfo('Sucesso!','Contato adicionado com sucesso!')
    atualizarTabela()
    limparCampos()

def tabelaClique(event):
    # PEGANDO A LINHA SELECIONADA
    # RETORNA O CÓDIGO DA LINHA EM UMA TUPLA
    linhaSelecionada= tabela.selection()[0]
    global index
    # OBTENDO O INJDICE DA LINHA A PARTIR DO CODIGO DA LINHA
    index = tabela.index(linhaSelecionada)
    contato = agenda[index]
    limparCampos()
    txtNome.insert(0,contato['nome'])
    txtTelefone.insert(0,contato['telefone'])
    comboCategoria.set(contato['categoria'])



def editarContato():
    agenda[index]= {
        "nome": txtNome.get(),
        "telefone": txtTelefone.get(),
        "categoria": comboCategoria.get()
    }
    limparCampos()
    atualizarTabela()
    messagebox.showinfo('Sucesso!', 'Dados alterados com sucesso!')


def deletar():
    opcao = messagebox.askyesno('Tem certeza?', 'Deseja remover o contato?')
    if opcao:
        agenda.remove(agenda[index])
        messagebox.showinfo('Sucesso!','Contato removido com sucesso!')
        limparCampos()
        atualizarTabela()






janela= Tk()
janela.title('Agenda Telefonica')
janela.geometry('+-800-100')



labelNome = Label(janela, text= 'Nome', fg= 'navy',font='Tahoma 14 bold')
labelNome.grid(row=0, column=0)

txtNome = Entry(janela,font='Tahoma 14',width=27)
txtNome.grid(row=0, column=1)



labelTelefone = Label(janela, text='Telefone',fg='navy',font='Tahoma 14 bold')
labelTelefone.grid(row=1,column= 0 )

txtTelefone = Entry(janela,font='Tahoma 14',width=27)
txtTelefone.grid(row=1, column=1)



labelCategorias= Label(janela,text='Categoria',fg ='navy',font='Tahoma 14 bold',width=20)
labelCategorias.grid(row=2, column=0)
categorias= ['Amigos','Trabalho','Familia']
comboCategoria= ttk.Combobox(janela, values=categorias,font='Tahoma 14', width=25)
comboCategoria.grid(row=2, column=1)



btnAdicionar = Button(janela,text='Adicionar',fg='navy', bg='white',
                      font='Tahoma 12 bold',width= 8, command=adicionarContato)
btnAdicionar.grid(row=3,column= 0)



btnEditar = Button(janela, text='Editar',fg='navy',bg= 'white',
                   font='Tahoma 12 bold', width=8, command= editarContato)
btnEditar.grid(row=3, column=1)



btnRemover = Button(janela, text='Remover',fg='navy',bg= 'white',
                   font='Tahoma 12 bold', width=8, command= deletar)
btnRemover.grid(row=3, column=2)




#COMO CRIAR UMA TABELA (TreeView)
colunas= ['Nome', 'Telefone','Categorias']
tabela= ttk.Treeview(janela, columns=colunas, show='headings')
#  show='headings' -> Oculta a coluna com o id da linha
for coluna in colunas:
    #renomeando a coluna
    tabela.heading(coluna,text=coluna)
tabela.grid(row=4, columnspan=3)

#CRIANDO UMA BIND
tabela.bind('<ButtonRelease-1>',tabelaClique)








atualizarTabela()
janela.mainloop()