#importo as bibliotecas
from tkinter import *
from PIL import ImageTk, Image, ImageOps
import os

#abro uma janela
root = Tk()
root.iconbitmap("zoo_ecosystem_exotic_wildlife_wild_animal_fauna_nature_capybara_icon_259316.ico")
root.title("capivaras")

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
prev = Button(root,text="prev",command=prev_image, fg="white", bg="black", font="Overthink")
prev.grid(row=1, column=0, sticky=E + W)

#o comando é um já pronto do Tk
sair = Button(root,text="sair", command=root.quit, fg="white", bg="black", font="Overthink")
sair.grid(row=1, column=1, sticky=E + W)

next = Button(root,text="next",command=next_image, fg="white", bg="black", font="Overthink")
next.grid(row=1, column=2, sticky=E + W)

#rodo a janela
root.mainloop()