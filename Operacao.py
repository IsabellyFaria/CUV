'''
Classe que descreve o comportamento das operações.
Uma operação é composta por um valor à esquerda e outro à direita de um símbolo matemático.

- Cada valor pode ser um termo ou outra operação

Isabelly Faria - 28/03/2026
'''

class Operacao:
    # Valores iniciais da instância
    def __init__(self, esquerda, direita, operador):
        self.esquerda = esquerda
        self.direita = direita
        self.operador = operador
    
    # Retorna a operação matemática entre os 2 valores
    def executar(self):
        match self.operador:
            case "+":
                return self.esquerda + self.direita
            case "-":
                return self.esquerda - self.direita
            case "*":
                return self.esquerda * self.direita
            case "/":
                return self.esquerda / self.direita
            case "^":
                return self.esquerda ** self.direita
    
    def calculaValor()