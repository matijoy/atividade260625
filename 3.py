# Questão 3

class FeiraLivre:
    def __init__(self, solicitante, fruta):
        self.solicitante = solicitante
        self.fruta = fruta

    def exibirfruta(self):
        print("-" *45)
        print(f"Solicitante -- {self.solicitante}\nFruta -- {self.fruta}")

listafrutas = ["Maçã", "Laranja", "Uva", "Limão", "Pera"]
solicit = []
def cadastrarfruta():
    print("Lista de frutas --")
    for i in range(len(listafrutas)):
        print(f"Fruta {i+1} -- {listafrutas[i]}")
    nome = input("Insira o nome do solicitante -- ")
    numero = int(input("Escolha o número da Fruta que você quer -- "))
    if numero < 1 or numero > 5:
        print("Fruta inválida!")
    else:
        fruta = FeiraLivre(nome, listafrutas[numero-1])
        solicit.append(fruta)

        for i in solicit:
            FeiraLivre.exibirfruta(i)

cadastrarfruta()