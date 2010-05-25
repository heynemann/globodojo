#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Módulo de código da solução do kata do globodojo da sessão do dia 25 de maio de 2010.'''

def avalia_numero(numero):
    fizz = 'fizz'
    buzz = 'buzz'
    retorno = numero
    
    eh_mult_5 = (numero % 5 == 0)
    eh_mult_3 = (numero % 3 == 0)
    contem_5  = ('5' in str(numero))
    contem_3 = ('3' in str(numero))
    
    if eh_mult_5 and eh_mult_3 or (contem_3 and '5' in str(numero)):
        retorno = 'fizzbuzz'
    elif eh_mult_3 or :
        retorno = fizz
    elif eh_mult_5 == 0 or ('5' in str(numero)):
        retorno = buzz
        
    return retorno