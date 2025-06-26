# Questão 2

class Biblioteca:
    def __init__(self, solicitante, livro):
        self.solicitante = solicitante
        self.livro = livro

    def exibirlivro(self):
        print("-" *45)
        print(f"Solicitante -- {self.solicitante}\nLivro -- {self.livro}")

listalivros = ["A Laranja Mecânica", "1984", "Frankenstein", "Homem Aranha Nº1", "História 1: Primeira Guerra Mundial", "História 2: Segunda Guerra Mundial", "Peppa Pig", "O Alquimista", "Extraordinário", "Cuphead"]
solicit = []
def cadastrarlivro():
    print("Lista de livros --")
    for i in range(len(listalivros)):
        print(f"Livro {i+1} -- {listalivros[i]}")
    nome = input("Insira o nome do solicitante -- ")
    numero = int(input("Escolha o número do livro que você quer -- "))
    if numero < 1 or numero > 10:
        print("Livro inválido!")
    else:
        livro = Biblioteca(nome, listalivros[numero-1])
        solicit.append(livro)

        for i in solicit:
            Biblioteca.exibirlivro(i)

cadastrarlivro()