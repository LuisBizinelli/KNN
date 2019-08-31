from leitor import matriz
from math import sqrt
from operator import itemgetter

#abrir arquivo
fileTreino = open("treino.data")
fileTeste = open ("teste.data")

matriz_treino = le_matriz(fileTreino)
matriz_teste = le_matriz(fileTeste)

k_list = [3,5,7,9,11]
d_list = [1, 2]

classes = 3
classe_indice = 4
atributos = 4

matriz_confusao = []

def init_matriz():
    global matriz_confusao
    matriz_confusao = [0] * classes
    for i in range (0,classes):
        matriz_confusao[i] = [0] * classes

def voto(distancias,k):
    c1 = 0
    c2 = 0
    c3 = 0 
    for i in range(0,k):
        if distancias[i][1] == 0:
            c1 += 1
        if distancias[i][1] == 1:
            c2 += 1
        if distancias[i][1] == 2:
            c3 += 1
    if c1 > c2 and c1 > c3:
        return 0
    elif c2 > c1 and c2 > c3:
        return 1
    else:
        return 2
def manhattan(x,y,attr):
    soma = 0
    for i in range (0,attr):
        soma += abs(x[i] - y [i])
    return soma

def euclidiana(x,y,attr):
    soma = 0
    for i in range (0,attr):
        soma += abs(x[i] - y[i]) ** 2

def adiciona matriz(x,y):
    matriz_confusao[x][y] += 1

def imprimir_matriz(matriz):
    for item in matriz:
        print(item)

def calcular_taxa(matriz_confusao):
    acertos = 0
    erros = 0
    for i in range (0,3):
        for j in range (0,3):
            if i == j:
                acertos += matriz_confusao[i][j]
            else:
                erros += matriz_confusao[i][j]
        total = acertos + erros
        return (acertos / total) * 100