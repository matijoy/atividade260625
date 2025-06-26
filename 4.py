# Questão 4

class Agenda:
    def __init__(self, data, evento):
        self.data = data
        self.evento = evento
    
    def exibiragenda(self):
        print(f"Evento -- {self.evento}\nDia -- {self.data}")

listaagenda = []

def cadastraragenda():
    evento = input("Insira o nome do evento -- ")
    data = input("Insira a data -- ")
    eventocompleto = Agenda(data,evento)
    listaagenda.append(eventocompleto)

def removerevento():
    if listaagenda == []:
        print("Lista vazia")
    else:
        pesquisa = input("Insira o nome do evento que você deseja remover -- ")
        for resultado in listaagenda:
            if pesquisa in resultado.evento:
                listaagenda.remove(resultado)
            else:
                print("Evento não encontrado!")

def exibiragenda():
    if listaagenda == []:
        print("Agenda vazia!")
    else:
        print("===== Agenda =====")
        for agenda in listaagenda:
            Agenda.exibiragenda(agenda)

def menu():
    opcao = int(input("AGENDA\n1 - Cadastrar um evento\n2 - Remover um evento\n3 - Exibir a agenda\n4 - Sair\n"))
    if opcao == 1:
        cadastraragenda()
        menu()
    if opcao == 2:
        removerevento()
        menu()
    if opcao == 3:
        exibiragenda()
        menu()
    if opcao < 1 or opcao > 4:
        print("Opção inválida")
        menu()

menu()