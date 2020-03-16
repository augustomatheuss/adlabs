#!/usr/bin/python
# -*- coding: utf-8 -*-


# Tipos básicos em Python


# Imprimindo mensagem para o usuário.
print('Olá!')

# Este bloco faz isso.
# cmd 1
# cmd 2
# cmd 3

# Variáveis - Tipo Inteiro
matricula = 12  # 23 0 14

# Variáveis - Tipo Flutuante
pi = 3.14  # 2.0

# Variáveis - Tipo Char
mychar = 'f'  # '0' '*'
matricula = str(matricula) + '!!'  # DEBUG STEP TRHOUGH

# Variáveis - Tipo String
nome = 'Arvore'  # 'Hello' 'Dia' 'Sol'

opInt = pi * 10 * 3.14
# %d é inteiro
# %f é flutuante
# %s é string
st = '!'
print('O resultado é %f %s' % (pi, st))  # se trocar o %f por %d, é feito um cast de flutuante para inteiro
print('O resultado é %.2f' % pi)


# Operações comuns entre strings.
# https://docs.python.org/3.3/library/string.html

# 'A r v o r e'
#  0 1 2 3 4 5
print(nome.index('r'))

# Concatenacao de Strings
nome = nome + ' H'
print(nome)

# Variáveis - Tipo Boolean
x = True  # False
