#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Módulo de testes da solução do kata do globodojo da sessão do dia 8 de junho de 2010.'''

import code
from ocr_input import *
from nose.tools import assert_equals

def test_montagem_dos_dados_de_input():
    assert len(code.monta_dado(test_data_0)) == 4, '%s' % len(code.monta_dado(test_data_0))

def test_obtem_zero():
    dados = code.monta_dado(test_data_0)
    resultado = code.le_dados(dados)
    assert_equals(resultado, result_0)

def test_le_dados_retorna_array_com_dados_nulos():
    dados = [
    ' _  _  _  _  _  _  _  _  _ ',
    '| || || || || || || || || |',
    '|_||_||_||_||_||_||_||_||_|',
    '                           ']
    resultado = code.le_dados(dados)
    
    assert_equals(resultado[0], '0')
    
def test_le_dados_retorna_array_com_dados_retorna_1():
    dados = [
    '                           ',
    '  |  |  |  |  |  |  |  |  |',
    '  |  |  |  |  |  |  |  |  |',
    '                           ',]
    
    resultado = code.le_dados(dados)
    assert_equals(resultado[0], '1')

