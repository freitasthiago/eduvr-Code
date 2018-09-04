class Materia:
    materiaCount=0

    def __init__ (self,nome,descricao):
        self.nome=nome
        self.descricao=descricao
        Materia.materiaCount+=1
    
    def QtdMaterias(self):
        print ("Total de matérias cadastradas %d" % Materia.materiaCount)
    
    def DadosMateria(self):
        print("Nome: ",self.nome,"\nDescrição: ",self.descricao)

disciplinas=["Física","Química","Biologia","História","Geografia","Ciências"]

disciplina1=Materia("Física", "Disciplina interessante")
disciplina2=Materia("Química", "Disciplina interessante")

disciplina1.DadosMateria()
disciplina2.DadosMateria()