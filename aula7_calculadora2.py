# função é tudo que retorna valor
# método não retorna

class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def mul(self, valor_a, valor_b):
        return valor_a * valor_b

    def div(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.sub(5, 3))
print(calculadora.mul(100, 2))
print(calculadora.div(10, 2))