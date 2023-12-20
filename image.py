#importo as bibliotecas
from tkinter import *
from utils import *

#armazena as imagens
imagens = []

#variavel de controle de imagem
imagem_atual = 0

#armazena a imagem
imagem_Label = None

#armazena o caminho para a pasta
img_folder = ""

#abro uma janela
root = Tk()
root.title("Fotos")

#crio meu menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

#coloco funções para o menu
filemenu.add_command(label="Open", command= lambda : open_folder(root))
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

#coloco as funções no menu
menubar.add_cascade(label="File", menu=filemenu)

#coloco o menu na janela
root.config(menu=menubar)
load_images(root)

#passo o root para o utils
load_images(root)
prev_image(root)
next_image(root)

#crio e posiciono os botões
prev = Button(root,text="anterior",command=lambda : prev_image(root), fg="white", bg="black", font="Overthink")
prev.grid(row=1, column=0, sticky=E + W)

#o comando é um já pronto do Tk
sair = Button(root,text="sair", command=root.quit, fg="white", bg="black", font="Overthink")
sair.grid(row=1, column=1, sticky=E + W)

next = Button(root,text="próxima",command=lambda : next_image(root), fg="white", bg="black", font="Overthink")
next.grid(row=1, column=2, sticky=E + W)

#defino teclas para substituir os botôes
root.bind("n", lambda event: next_image(root))
root.bind("p", lambda event: prev_image(root))
root.bind("q", lambda event: root.quit(root))

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