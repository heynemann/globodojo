#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Módulo de código da solução do kata do globodojo da sessão do dia 8 de junho de 2010.'''

def monta_dado(entrada):
    retorno = []
    linha = ''
    count = 0
    for letra in entrada:
        linha += letra
        count += 1
        if count == 27:
            retorno.append(linha)
            linha = ''
            count = 0
    
    return retorno
    
def le_dados(dados):
    
    item = dados[0][:3] + dados[1][:3] + dados[2][:3] + dados[3][:3]
    
    return ""