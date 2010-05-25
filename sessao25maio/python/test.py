#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Módulo de testes da solução do kata do globodojo da sessão do dia 25 de maio de 2010.'''

import code

def test_retorna_um():
    assert code.avalia_numero(1) == 1

def test_tres_retorna_fizz():
    assert code.avalia_numero(3) == 'fizz'

def test_cinco_retorna_buzz():
    assert code.avalia_numero(5) == 'buzz'

def test_quinze_retorna_fizzbuzz():
    assert code.avalia_numero(15) == 'fizzbuzz'

def test_fizz_de_um_a_cem():
    for numero in range(1,101):
        if numero % 3 == 0:
            texto = code.avalia_numero(numero)
            assert 'fizz' in texto

def test_buzz_de_um_a_cem():
    for numero in range(1,101):
        if numero % 5 == 0:
            texto = code.avalia_numero(numero)
            assert 'buzz' in texto, 'eu esperava que aparece buzz em algo mas apareceu %s para o numero %s' % (texto, numero)
            
def test_fizzbuzz_de_um_a_cem():
    for numero in range(1,101):
        if (numero % 5 == 0) and (numero % 3 == 0):
            texto = code.avalia_numero(numero)
            assert 'fizzbuzz' == texto
            
def test_nao_multiplo_de_tres_retorna_fizz():
    for numero in range(1,101):
        if numero % 3 != 0:
            type(numero) == int

def test_nao_multiplo_de_cinco_retorna_buzz():
    for numero in range(1,101):
        if numero % 5 != 0:
            type(numero) == int

def test_numero_contendo_tres_retorna_fizz():
    assert code.avalia_numero(13) == 'fizz'
    
def test_numero_contendo_cinco_retorna_buzz():
    valor  = code.avalia_numero(52)
    assert valor == 'buzz', 'Eu esperava buzz mas apareceu %s ' % valor
    
# def test_numero_contendo_cinco_retorna_buzz():
#     valor  = code.avalia_numero(51)
#     assert valor == 'fizzbuzz', 'Eu esperava fizzbuzz mas apareceu %s ' % valor