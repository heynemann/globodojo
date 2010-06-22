#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Módulo de testes da solução do kata do globodojo da sessão do dia 22 de junho de 2010.'''

from nose.tools import assert_equals
from code import Cesta

# 8 pounds por livro
def test_adiciona_livro_retorna_preco():
    cesta = Cesta()
    cesta.adiciona('livro1')
    
    total = cesta.obtem_preco()
    assert_equals(total, 8.0, u'O preco de um livro é 8 pounds')
    assert len(cesta.livros) > 0

def test_verifica_quantidade_de_livros_iguais():
    cesta = Cesta()
    cesta.adiciona('livro1')
    cesta.adiciona('livro1')
    
    esperado = len(cesta.livros)
    
    assert_equals(esperado, 2, u'A cesta possui %s livros iguais' % esperado)
    
def test_verifica_quantidade_de_livros_diferentes():
    cesta = Cesta()
    cesta.adiciona('livro1')
    cesta.adiciona('livro1')
    cesta.adiciona('livro2')

    esperado = len(cesta.livros_diferentes)

    assert_equals(esperado, 2, u'A cesta possui %s livros diferentes' % esperado)

def test_adiciona_livros_iguais_retorna_precos_sem_desconto():
    cesta = Cesta()
    cesta.adiciona('livro1')
    cesta.adiciona('livro1')

    total = cesta.obtem_preco()
    esperado = 16.0
    assert_equals(total, esperado, u'O preco de um livro deveria ser %f pounds' % esperado)

def test_adiciona_livros_diferentes_retorna_precos_com_desconto():
    cesta = Cesta()
    cesta.adiciona('livro1')
    cesta.adiciona('livro2')

    total = cesta.obtem_preco()
    esperado = 16.0 * 0.95
    assert_equals(total, esperado, u'O preco de um livro é %f pounds deveria ser %f' % (total, esperado))
