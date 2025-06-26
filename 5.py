class Aluno:
    def __init__(self, aluno):
        self.aluno = aluno

    def exibiraluno(self):
        print(f"Aluno(a) -- {self.aluno}")

class Professor:
    def __init__(self, prof):
        self.prof = prof

    def exibirprofessor(self):
        print(f"Professor(a) -- {self.prof}")

class Curso:
    def __init__(self, curso):
        self.curso = curso

    def exibircurso(self):
        print(f"Curso -- {self.curso}")

alunos = []
profs = []
cursos = []

def cadastroaluno():
    aluno = input("Insira o nome do aluno que você deseja cadastrar -- ")
    aluno = Aluno(aluno)
    alunos.append(aluno)

def cadastroprof():
    professor = input("Insira o nome do professor que você deseja cadastrar -- ")
    professor = Professor(professor)
    profs.append(professor)

def cadastrocurso():
    curso = input("Insira o nome do curso que você deseja cadastrar -- ")
    curso = Curso(curso)
    cursos.append(curso)

def exibirtudo():
    print("==== Alunos ====")
    for a in alunos:
        Aluno.exibiraluno(a)
    print("==== Professores ====")
    for p in profs:
        Professor.exibirprofessor(p)
    print("==== Cursos ====")
    for c in cursos:
        Curso.exibircurso(c)

def exibiralunos():
    print("==== Alunos ====")
    if alunos == []:
        print(" ")
    else:
        for a in alunos:
            Aluno.exibiraluno(a)

def exibirprofessores():
    if profs == []:
        print(" ")
    else:
        print("==== Professores ====")
        for p in profs:
            Professor.exibirprofessor(p)

def exibircursos():
    if cursos == []:
        print(" ")
    else:
        print("==== Cursos ====")
        for c in cursos:
            Curso.exibircurso(c)

def removeraluno():
    if alunos == []:
        print("Não há alunos")
    else:
        pesquisa = input("Insira o nome do(a) aluno(a) que você deseja remover -- ")
        for remalu in alunos:
            if pesquisa in remalu.aluno:
                alunos.remove(remalu)
            else:
                print("Aluno(a) não encontrado(a)")

def removerprof():
    if profs == []:
        print("Não há professores")
    else:
        pesquisa = input("Insira o nome do(a) professor(a) que você deseja remover -- ")
        for rempro in profs:
            if pesquisa in rempro.prof:
                profs.remove(rempro)
            else:
                print("Professor(a) não encontrado(a)")

def removercurso():
    if cursos == []:
        print("Não há cursos")
    else:
        pesquisa = input("Insira o nome do curso que você deseja remover -- ")
        for remcur in cursos:
            if pesquisa in remcur.curso:
                cursos.remove(remcur)
            else:
                print("Curso não encontrado(a)")


def menu():
    opcao = int(input("MENU\n1 - Cadastrar um(a) aluno(a)\n2 - Cadastrar um(a) professor(a)\n3 - Cadastrar um curso\n4 - Exibir tudo\n5 - Remover aluno(a), professor(a) ou curso\n6 - Sair\n"))
    if opcao == 1:
        cadastroaluno()
        menu()
    if opcao == 2:
        cadastroprof()
        menu()
    if opcao == 3:
        cadastrocurso()
        menu()
    if opcao == 4:
        exibirtudo()
        menu()
    if opcao == 5:
        escolha = int(input("ESCOLHA O QUE VOCÊ DESEJA REMOVER\n1 - Aluno(a)\n2 - Professor(a)\n3 - Curso\n"))
        if escolha == 1:
            removeraluno()
            menu()
        if escolha == 2:
            removerprof()
            menu()
        if escolha == 3:
            removercurso()
            menu()
        if escolha < 1 or escolha > 3:
            print("Opção inválida!")
            menu()
    if opcao < 1 or opcao > 6:
        print("Opção inválida")
        menu()

menu()