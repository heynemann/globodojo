#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Módulo de código da solução do kata do globodojo da sessão do dia 22 de junho de 2010.'''

class Cesta(object):
    
    def __init__(self):
        self.livros = []
        self.livros_diferentes = []
        self.preco_unitario = 8.0

    def adiciona(self, livro):
        self.livros.append(livro)
        
        if not livro in self.livros_diferentes:
            self.livros_diferentes.append(livro)
        
    def obtem_preco(self):
        # desconto = len(self.livros_diferentes)
        carrinho = len(self.livros) * self.preco_unitario 
        return carrinho
        