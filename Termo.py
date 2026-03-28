'''
Classe que descreve um termo de um polinômio
* Todo termo é descrito por: a * xˆn
    - a multiplica x
    - x é a variavél da equação
    - n é a potencia de x
* X pode ser declarado sem valor se este é desconhecido
Isabelly Faria - 27/03/2026
'''
class Termo:
    #Valores iniciais da instancia
    def __init__(a=1, n=0, x = None):
        self.multiplicador = a
        self.potencia = p
        self.valor = n
    #Métodos para definir valores
    def setMultiplicador(a=1):
        self.multiplicador = a
    def setPotencia(n=0):
        self.potencia = n
    def setValor(x=None):
        self.potencia = p
    #Métodos para obter valores
    def getMultiplicador()
        return self.multiplicador
    def getPotencia():
        return self.potencia
    def getValor():
        return self.valor
        
    