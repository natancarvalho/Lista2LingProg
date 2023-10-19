#Lista de Exercícios 2 - Linguagens de Programação
#ECA 2023.2
#UFRJ
#Natã dos Santos Carvalho

#Exercício 1
class Bola:
    cor = "azul"
    circunferencia = 30
    material = "plastico"

    def trocaCor(self, cor):
        self.cor = cor

    def mostrarCor(self):
        print(self.cor)

#Exercício 2
class Quadrado:
    tamanho_lado = 10

    def mudarValorLado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mostrarTamanhoLado(self):
        print(self.tamanho_lado)

    def calcularArea(self):
        area = float(self.tamanho_lado)** 2
        print("Area do quadrado: ",area,"m².")

#Exercício 3
class Retangulo:
    comprimento = 10
    largura = 7

