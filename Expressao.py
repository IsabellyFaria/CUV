'''
Classe que descreve o comportamento das expressões.
Uma expressão é representada como uma árvore, em que cada nó pode ser uma operação ou uma função.

Isabelly Faria - 28/03/2026
'''
class Expressao:
    # Valores iniciais da instância
    def __init__(self, raiz):
        self.raiz = raiz
        self.solucoes = []

    #Retorna raiz
    def getRaiz(self):
        return self.raiz
    
    #Retorna as soluções
    def getSolucao(self):
        return self.solucoes
    
    #Determina Raiz
    def setRaiz(self, r):
        self.raiz = r
    
    #Adiciona solução
    def setSolucao(self, s):
        self.solucoes.append(s)

    