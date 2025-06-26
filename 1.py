# Questão 1

class Viagem:
    def __init__(self, viajante, destino,):
        self.viajante = viajante
        self.destino = destino

    def exibirdestino(self):
        print("-" *45)
        print(f"Viajante: {self.viajante}\nDestino: {self.destino}")

listadestinos = []
def cadastrardestino():
    nome = input("Insira o nome do viajante -- ")
    destino = int(input("Nós temos 5 destinos disponíveis! Escolha um\n[1] Tóquio\n[2] Toronto\n[3] Bordéus\n[4] Brasília\n[5] Berlim\n\n"))
    if destino == 1:
        destino = "Tóquio"
    elif destino == 2:
        destino = "Toronto"
    elif destino == 3:
        destino = "Bordéus"
    elif destino == 4:
        destino = "Brasília"
    elif destino == 5:
        destino = "Berlim"
    else:
        print("Destino inválido!")
    viajar = Viagem(nome, destino)
    listadestinos.append(viajar)

    for pessoa in listadestinos:
        pessoa.exibirdestino()

cadastrardestino()