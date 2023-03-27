class Personne():

    def __init__(self, prenom, nom):
       self.prenom = prenom
       self.nom = nom

    def SePresenter(self):
        print ("Je suis " + self.prenom + " " + self.nom)

pers1 = Personne("John", "Doe")
pers2 = Personne("Jean", "Dupond")
pers1.SePresenter()
pers2.SePresenter()