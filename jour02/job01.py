class Personne:
    def __init__(self):
        age = 14
        self.age = age

    def afficherAge(self):
        print (self.age)

    def bonjour(self):
        print ("Hello")

    def modifierAge(self, age):
        self.age = age
        print("L'age de l'eleve est de", self.age, "ans")

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)
        self.affichageAge()

    def allerEnCours(self):
        print ("Je vais en cours")

    def affichageAge(self):
        print ("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignée):
        self.matiereEnseignée = matiereEnseignée

    def enseigner():
        print("Le cours va commencer")

personne1 = Personne()
eleve1 = Eleve()