class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print('je suis '+ self.prenom+ ' '+ self.nom)

John = Personne('Doe', 'John')
Jean = Personne('Dupond', 'Jean')

John.SePresenter()
Jean.SePresenter()