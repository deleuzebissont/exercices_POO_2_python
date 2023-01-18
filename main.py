import random


def number():
    nombre_1 = random.randint(1, 6)
    nombre_2 = random.randint(1, 6)
    nombre_3 = random.randint(1, 6)
    nombre_4 = random.randint(1, 6)
    liste = [nombre_1, nombre_2, nombre_3, nombre_4]
    # la liste met les valeurs en ordre croissant
    liste.sort()
    # on elemine la valeur la plus petite
    liste.pop(0)
    # on stock la valeur des donnees additiones dans une variable
    nombre = sum(liste)
    return nombre


class npc:
    def __init__(self):
        # on definit toutes nos variables soit par None ou pas le nombre cree dans la fonction ci dessus ou encore
        # par un nombre aleatoire en particulier (classe_armure ou point_de_vie)
        self.name = None
        self.race = None
        self.espece = None
        self.profession = None
        self.force = number()
        self.agilite = number()
        self.constitution = number()
        self.intelligence = number()
        self.sagesse = number()
        self.charisme = number()
        self.classe_armure = random.randint(1, 12)
        self.point_de_vie = random.randint(1, 20)

    def afficher_caracteristiques(self):
        print(f"""
       Caracteristiques :
       Force : {self.force}
       Agilite : {self.agilite}
       Constitution : {self.constitution}
       Intelligence : {self.intelligence}
       Sagesse : {self.sagesse}
       Charisme : {self.charisme}
       Classe armure : {self.classe_armure}
       Point de vie : {self.point_de_vie}
       Nom : {self.name}
       Race : {self.race}
       Espece : {self.espece}
       Profession : {self.profession}
       """)


class kobold(npc):
    # on recoit la cible en parametre et la quantite de dommage un peu plus bas
    def attaquer(self, cible):
        return

    def subir_dommage(self, quantite_de_dommage):
        return


class Heros(npc):
    # on recoit la cible en parametre et la quantite de dommage un peu plus bas
    def attaquer(self, cible):
        return

    def subir_dommage(self, quantite_de_dommage):
        return
