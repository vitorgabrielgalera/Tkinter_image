#importo as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image, ImageOps
import os

#crio funções para o menu
def open_file():
    #defino para escolher um arquivo
    folder_path = filedialog.askdirectory()
    #defino mensagem e sons
    if folder_path:
        messagebox.showinfo(title="abrindo diretório", message=f"O diretório selecionado foi: {folder_path}")
    else:
        messagebox.showerror(title="abrindo diretório", message="Nenhum diretório foi selecionado")

#abro uma janela
root = Tk()
root.title("Laurinha")

#crio meu menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

#coloco funções para o menu
filemenu.add_command(label="Open", command= open_file)
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

#coloco as funções no menu
menubar.add_cascade(label="File", menu=filemenu)

#coloco o menu na janela
root.config(menu=menubar)

#pega um arquivo e faz uma lista com o que tem tudo no arquivo
arquivos = os.listdir("imagens")

#armazena as imagens
imagens = []

#percorre cada arquivo dentro de arquivos
for arquivo in arquivos:

#tenta abrir imagem
    try:
        img = Image.open("imagens/" + arquivo)
        
    #defino o que fazer caso der errado (passar para o próximo)
    except:
        continue
    
    #defino o que fazer caso der certo (colocar a imagem)
    else:
        #redimenciono a imagem
        img = ImageOps.contain(img, (500,500))

        #adiciona a imagem na lista
        imagens.append(ImageTk.PhotoImage(img))

#exibe arquivos em um label
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()

#variavel de controle de imagem
imagem_atual = 0

#defino os parâmetros da imagem
imagem_Label = Label(root, image=imagens[imagem_atual])

#abro a imagem na janela
imagem_Label.grid(row=0, column=0, columnspan=3)

#defino as funções de avançae e voltar
def prev_image():

    #transformo as variáveis em globa
    global imagem_atual
    global imagem_Label
    global imagens

    #se a variavel for a primeira ela vai para a ultima
    if imagem_atual == 0:
        imagem_atual = len(imagens) - 1
    else:
        imagem_atual -= 1

    #apaga a imagem
    imagem_Label.grid_forget()

    #exibe a nova imagem
    imagem_Label = Label(root, image=imagens[imagem_atual])
    imagem_Label.grid(row=0, column=0, columnspan=3)

def next_image():
    #transformo as variáveis em globa
    global imagem_atual
    global imagem_Label
    global imagens

    #se a variavel for a primeira ela vai para a ultima
    if imagem_atual == len(imagens) - 1:
        imagem_atual = 0
    else:
        imagem_atual += 1

    #apaga a imagem
    imagem_Label.grid_forget()

    #exibe a nova imagem
    imagem_Label = Label(root, image=imagens[imagem_atual])
    imagem_Label.grid(row=0, column=0, columnspan=3)

#crio e posiciono os botões
prev = Button(root,text="anterior",command=prev_image, fg="black", bg="pink", font="Overthink")
prev.grid(row=1, column=0, sticky=E + W)

#o comando é um já pronto do Tk
sair = Button(root,text="sair", command=root.quit, fg="black", bg="pink", font="Overthink")
sair.grid(row=1, column=1, sticky=E + W)

next = Button(root,text="próxima",command=next_image, fg="black", bg="pink", font="Overthink")
next.grid(row=1, column=2, sticky=E + W)

#defino teclas para substituir os botôes
root.bind("<Button-1>", lambda event: next_image())
root.bind("<Button-3>", lambda event: prev_image())
root.bind("q", lambda event: root.quit())

#rodo a janela
root.mainloop()






#              _.--""`-..
#            ,'          `.
#          ,'          __  `.
#         /|          " __   \
#        , |           / |.   .
#        |,'          !_.'|   |
#      ,'             '   |   |
#     /              |`--'|   |
#    |                `---'   |
#     .   ,                   |                       ,".
#      ._     '           _'  |                    , ' \ `
#  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
#  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
#-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
#  `,         """"'     `.              ,'         |   |  ',,
#    `.      '            '            /          '    |'. |/
#      `.   |              \       _,-'           |       ''
#        `._'               \   '"\                .      |
#           |                '     \                `._  ,'
#           |                 '     \                 .'|
#           |                 .      \                | |
#           |                 |       L              ,' |
#           `                 |       |             /   '
#            \                |       |           ,'   /
#          ,' \               |  _.._ ,-..___,..-'    ,'
#         /     .             .      `!             ,j'
#        /       `.          /        .           .'/
#       .          `.       /         |        _.'.'
#        `.          7`'---'          |------"'_.'
#       _,.`,_     _'                ,''-----"'
#   _,-_    '       `.     .'      ,\
#   -" /`.         _,'     | _  _  _.|
#    ""--'---"""""'        `' '! |! /
#                            `" " 