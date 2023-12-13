#importo as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image, ImageOps
import os

#armazena as imagens
imagens = []

#variavel de controle de imagem
imagem_atual = 0

#armazena a imagem
imagem_Label = None

#armazena o caminho para a pasta
img_folder = ""

#função para carregar imagens
def load_images():
    global img_folder
    global imagens
    global imagem_Label

    if img_folder:
        imagens.clear()

        #pega um arquivo e faz uma lista com o que tem tudo no arquivo
        arquivos = os.listdir(img_folder)

        #percorre cada arquivo dentro de arquivos
        for arquivo in arquivos:

        #tenta abrir imagem
            try:
                img = Image.open(os.path.join(img_folder,arquivo))
            
            #defino o que fazer caso der errado (passar para o próximo)
            except:
                continue
        
            #defino o que fazer caso der certo (colocar a imagem)
            else:
                #redimenciono a imagem
                img = ImageOps.contain(img, (500,500))

                #adiciona a imagem na lista
                imagens.append(ImageTk.PhotoImage(img))

    else:
        #cria uma imagem preta caso não exista uma pasta
        img = Image.new("RGB", (500,500))
        imagens.append(ImageTk.PhotoImage(img))

    #exibe a primeira imagem
    imagem_Label = Label(root, image=imagens[0])

    #abro a imagem na janela
    imagem_Label.grid(row=0, column=0, columnspan=3)


#crio funções para o menu
def open_folder():
    #defino par1a escolher um arquivo
    global img_folder
    img_folder = filedialog.askdirectory()
    #defino mensagem e sons
    if img_folder:
        load_images()
    else:
        messagebox.showerror(title="abrindo diretório", message="Nenhum diretório foi selecionado")

#abro uma janela
root = Tk()
root.title("Laurinha")

#crio meu menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

#coloco funções para o menu
filemenu.add_command(label="Open", command= open_folder)
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

#coloco as funções no menu
menubar.add_cascade(label="File", menu=filemenu)

#coloco o menu na janela
root.config(menu=menubar)
load_images()

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
    #transformo as variáveis em global
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
root.bind("n", lambda event: next_image())
root.bind("p", lambda event: prev_image())
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