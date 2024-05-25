from PIL import Image, ImageDraw
import numpy as np
import os
import glob
import matplotlib.pyplot as plt


def plot(M, nn, size=(300, 300)):
    plot = Image.new("L", size)
    draw = ImageDraw.Draw(plot)
    nodx = float(size[0]) / len(M)
    nody = float(size[1]) / len(M)
    for i in range(len(M)):
        for j in range(len(M)):
            stax = i * nodx
            stay = j * nody
            finx = (i + 1) * nodx
            finy = (j + 1) * nody
            lumi = 256 * (1 - M[i][j])
            draw.rectangle((stax, stay, finx, finy), outline=lumi, fill=lumi)
    del draw
    filena = "plot%6i.jpg" % nn
    filena = filena.replace(" ", "0")
    plot.save(filena)


def umamatriz(n):
    matriz = np.array([0 for i in range(n * n)]).reshape(n, n)
    return matriz


def umamatriz2(n):
    matriz = list(list(0 for i in range(n)) for j in range(n))
    return matriz


def counter(matriz):

    tam = len(matriz)
    counter = 0
    for y in range(tam):
        for x in range(tam):
            counter += matriz[y][x]
    return counter

def vizinhos(matriz):
    tam = len(matriz)
    matriz_cp=[ele[:]for ele in matriz]
    for i in range(tam):
        for j in range(tam):
            vizinhos = 0
            for line in range(i - 1, i + 2):
                for row in range(j - 1, j + 2):
                    vizinhos += matriz[line % tam][row % tam]
            vizinhos -= matriz[i][j]

            if vizinhos == 3:
                matriz_cp[i][j] = 1
            elif vizinhos == 3 or vizinhos == 2:
                matriz_cp[i][j] = matriz_cp[i][j]
            else:
                matriz_cp[i][j] = 0
    return matriz_cp


def jogo_da_vida(n=10, r=1000, i=1):
    matriz = umamatriz2(n)
    if (i ==1):
        matriz[5][6] = 1
        matriz[6][6] = 1
        matriz[7][6] = 1
        matriz[6][5] = 1
        matriz[7][4] = 1
    if (i ==2):

        matriz[5][5] = 1
        matriz[5][4] = 1
        matriz[5][6] = 1
        matriz[6][5] = 1
    if (i ==3):

        matriz[4][5] = 1
        matriz[4][6] = 1
        matriz[5][4] = 1
        matriz[5][5] = 1
        matriz[6][6] = 1
    if (i ==4):

        matriz[5][4] = 1
        matriz[5][5] = 1
        matriz[6][6] = 1
        matriz[4][6] = 1
        #'''
    if (i ==5):
        matriz[2][5] = 1
        matriz[3][4] = 1
        matriz[3][6] = 1
        matriz[8][5] = 1
        matriz[4][3] = 1
        matriz[5][3] = 1
        matriz[6][3] = 1
        matriz[7][4] = 1
        matriz[4][7] = 1
        matriz[5][7] = 1
        matriz[6][7] = 1
        matriz[7][6] = 1
        #'''
    if (i ==6):

        matriz[3][4] = 1
        matriz[3][5] = 1
        matriz[3][6] = 1
        matriz[6][5] = 1
        matriz[5][4] = 1
        matriz[7][4] = 1
        matriz[5][6] = 1
        matriz[7][6] = 1
        #'''
    bacs = list()
    t = 0
    tlist = list()
    while t < r:
        #print(matriz)
        bacs.append(counter(matriz))
        tlist.append(t)
        plot(matriz,t)
        matriz = vizinhos(matriz)
        t += 1
    return bacs, tlist


def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.JPG")]
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)


for i in range (1,7):
    if i==1:
        padrao1bac,padrao1t = jogo_da_vida(100, 2000,i)
    '''if i==2:
        padrao2bac,padrao2t = jogo_da_vida(100, 150,i)'''
    '''if i==3:
        padrao3bac,padrao3t = jogo_da_vida(100, 150,i)'''
    #if i==4:
        #padrao4bac,padrao4t = jogo_da_vida(100, 150,i)
    #if i==5:
        #padrao5bac,padrao5t = jogo_da_vida(100, 150,i)
    #if i ==6:
        #padrao6bac,padrao6t = jogo_da_vida(100, 150,i)

make_gif("C:/Users/Pichau/Desktop/jogodavida")

plt.plot(padrao1t,padrao1bac)
plt.xlabel('Numero de iterações')
plt.ylabel('Número de bactérias vivas')
plt.title('Padrão 1')
plt.savefig('padrao1.png')
plt.show()
#plt.savefig('padrao1.png')
'''
plt.plot(padrao2t,padrao2bac)
plt.xlabel('Numero de iterações')
plt.ylabel('Número de bactérias vivas')
plt.title('Padrão 2')


plt.savefig('padrao2.png')
plt.show()
plt.plot(padrao3t,padrao3bac)
plt.xlabel('Numero de iterações')
plt.ylabel('Número de bactérias vivas')
plt.title('Padrão 3')



plt.savefig('padrao3.png')
plt.show()
plt.plot(padrao4t,padrao4bac)
plt.xlabel('Numero de iterações')
plt.ylabel('Número de bactérias vivas')
plt.title('Padrão 4')


plt.savefig('padrao4.png')
plt.show()
plt.plot(padrao5t,padrao5bac)
plt.xlabel('Numero de iterações')
plt.ylabel('Número de bactérias vivas')
plt.title('Padrão 5')

#plt.show()
plt.savefig('padrao5.png')
plt.show()
plt.plot(padrao6t,padrao6bac)
plt.xlabel('Numero de iterações')
plt.ylabel('Número de bactérias vivas')
plt.title('Padrão 6')

#plt.show()
plt.savefig('padrao6.png')
plt.show()'''