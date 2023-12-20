# define enumerations using the Enum base class
from enum import Enum, auto

# TODO: Defina a classe Fruta que herda de Enum
class Fruta(Enum):
    Uva = 1
    Banana = 2
    Laranja = 3
    Tomate = 4
    Pera = auto()

def main():
    # TODO: Objetos enum possuem valores e tipos de fácil leitura
    #print(Fruta.Uva)
    #print(type(Fruta.Uva))
    #print(repr(Fruta.Uva))
    # TODO: Objetos enum possuem propriedades "name" (nome) e
    # "value" (valor)
    #print(Fruta.Uva.name, Fruta.Uva.value)
    # TODO: Mostre o valor gerado automaticamente para PERA)
    #print(Fruta.Pera.value)
    # TODO: É possível usar objetos enum como chaves
    frutas = dict()
    frutas[Fruta.Banana] = "Casca Amarela"
    print(frutas[Fruta.Banana])

if __name__ == "__main__":
    main()
