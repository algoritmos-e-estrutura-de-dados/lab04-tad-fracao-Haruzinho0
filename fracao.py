class Fracao:
    numerador = 1 
    denominador = 1


    ##metodo de fracao
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador


    ##metodo de somas de frações
    def add(self, fracao): 
        num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
        den = (self.denominador * fracao.denominador)
        return Fracao(num,den)


    def sub(self, fracao): ##subtração de fracao
        if(self.denominador == fracao.denominador) & (self.numerador != fracao.numerador):
            num = (self.numerador - fracao.numerador) 
            den = (self.denominador)
        elif(self.denominador == fracao.denominador) & (self.numerador == fracao.numerador):
            num = 0
            den = 0
        else :     
            num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
            den = (self.denominador * fracao.denominador)
        return Fracao(num,den)

    def mul(self, fracao): ##multiplicar a fracao
        num = (self.numerador * fracao.numerador) 
        den = (self.denominador * fracao.denominador)
        return Fracao(num,den)

    def simplify(self):
        for i in range(2, 10):
            if (self.numerador % i == 0 and self.denominador % i == 0):
                self.numerador = self.numerador / i
                self.denominador = self.denominador / i
                return f"{self.numerador}/{self.denominador}"
            else:
                print("nao é possivel simplificar")
        return

    def solve(self):
        return self.numerador/self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"    


fracao1 = Fracao(1,2)
fracao2 = Fracao(2,4)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mul(fracao2)
fracao6 = fracao2.simplify()
print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2.solve()}")
print(f"fracao3: {fracao3.solve()}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5.solve()}")
print(f"fracao6: {fracao6}")