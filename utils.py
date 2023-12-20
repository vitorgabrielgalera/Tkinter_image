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
def load_images(root):
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
def open_folder(root):
    #defino par1a escolher um arquivo
    global img_folder
    img_folder = filedialog.askdirectory()
    #defino mensagem e sons
    if img_folder:
        load_images(root)
    else:
        messagebox.showerror(title="abrindo diretório", message="Nenhum diretório foi selecionado")

#defino as funções de avançae e voltar
def prev_image(root):

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

def next_image(root):
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