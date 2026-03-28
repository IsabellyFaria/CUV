'''
Classe que descreve um termo de um polinômio.
Todo termo é representado por: a * x^n

- a: coeficiente que multiplica x
- x: variável da equação
- n: expoente de x

A variável x pode ser declarada sem valor caso seja desconhecida.

Isabelly Faria - 27/03/2026
'''
class Termo:
    #Valores iniciais da instancia
    def __init__(self, a=1, n=0, x = None):
        self.multiplicador.self = a
        self.potencia = p
        self.valor = n
    #Métodos para definir valores
    def setMultiplicador(self, a=1):
        self.multiplicador = a
    def setPotencia(self, n=0):
        self.potencia = n
    def setValor(self, x=None):
        self.potencia = p
    #Métodos para obter valores
    def getMultiplicador(self):
        return self.multiplicador
    def getPotencia(self):
        return self.potencia
    def getValor(self):
        return self.valor
        
    