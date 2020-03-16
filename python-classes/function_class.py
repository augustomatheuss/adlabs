#!/usr/bin/python
# -*- coding: utf-8 -*-


# Funções em Python


import math


pi = 3.14  # pi é variável global, todo mundo enxerga


def ola():
    """
    Procedimento que imprime a mensagem "Olá!"
    :return:
    """
    print('Ola!')


def dist_ponto_ponto(x1, y1, x2, y2):
    """
    Função que calcula a distância entre dois pontos bidimensionais
    :param x1: Coordenada x do ponto 1
    :param y1: Coordenada y do ponto 1
    :param x2: Coordenada x do ponto 2
    :param y2: Coordenada y do ponto 2
    :return: Distância entre os pontos 1 e 2
    """
    dist_x = math.pow(x1-x2, 2.0)
    dist_y = math.pow(y1-y2, 2.0)
    return math.sqrt(dist_x+dist_y)


def area_circulo(raio):
    """
    Função que calcula a área de um círculo
    :param raio: Raio do círculo
    :return: Área do círculo
    """
    global pi  # Enxerga a variável no escopo global, pois a função tem um escopo local!
    return 2*pi*math.pow(raio, 2.0)


# dist_x é diferente do escopo da dist_x da funcao dist_ponto_ponto
dist_x = 47564168148
acertou = False
tentativa = 1
while not acertou:
    print('Tentativa %d\n' % tentativa)
    raio = input('\nQual o raio do circulo: ')
    x = input('Qual a posição do projétil em x: ')
    y = input('Qual a posição do projétil em y: ')
    dist = dist_ponto_ponto(float(x), float(y), 10.0, 10.0)
    if dist <= float(raio):
        print('O projétil acertou o alvo na tentativa %d'
              '.\n\tDistância com o raio do círculo: %f' % (tentativa, dist))
        acertou = True
    else:
        print('O projétil não acertou o alvo. Tente Novamente!')
        tentativa += 1
