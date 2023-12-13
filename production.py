class Carte:
    def __init__(self, mana:int, name:str, desc:str):
        self.__cout=mana
        self.__nom=name
        self.__description=desc
    def getCout(self):
        return self.__cout
    def getNom(self):
        return self.__nom
    def getDescription(self):
        return self.__description

class Cristal(Carte):
    def __init__(self, mana:int, name:str, desc:str, val:int):
        Carte.__init__(self, mana, name, desc)
        self.__valeur=val
    def getValeur(self):
        return self.__valeur

class Creature(Carte):
    def __init__(self, mana:int, name:str, desc:str, hp:int, atk:int):
        Carte.__init__(self, mana, name, desc)
        self.__pv=hp
        self.__atq=atk
    def getPv(self):
        return self.__pv
    def getAtq(self):
        return self.__atq

    def perdPv(self, pv_perdus:int):
        self.__pv-=pv_perdus
    
    def meurs(self):
        if self.__pv<=0:
            return True
        return False

class Blast(Carte):
    def __init__(self, mana:int, name:str, desc:str, val:int):
        Carte.__init__(self, mana, name, desc)
        self.__valeur=val
    def getValeur(self):
        return self.__valeur

class Mage:
    def __init__(self, name:str, hand:list):
        self.__nom=name
        self.__pv=30
        self.__total=10
        self.__mana=1
        self.__main=hand
        self.__defausse=[]
        self.__zone=[]
    def getPv(self):
        return self.__pv
    def getNom(self):
        return self.__nom
    def getMana(self):
        return self.__mana
    def getTotal(self):
        return self.__total
    
    def perdPv(self, pv_perdus):
        self.__pv-=pv_perdus

    def jouerCarte(self, carte_jouee:Carte):
        if carte_jouee not in self.__main:
            print("Vous n'avez pas cette carte dans votre main.")
        elif carte_jouee.getCout()>self.__mana:
            print("Vous n'avez pas assez de Mana pour jouer cette carte.")
        else:
            self.__main.remove(carte_jouee)
            self.__zone.append(carte_jouee)
            self.__mana-=carte_jouee.getCout()
        
        if type(carte_jouee)==Cristal:
            self.__total+=carte_jouee.getValeur()
        if type(carte_jouee)==Blast:
            """il faudrait faire en sorte, dans une vraie partie, de récupérer les données du Mage et des Creatures adverses pour leur
            faire perdre des pv équivalents à la valeur du Blast"""
            print("Vous infligez des dégâts.")
                
    
    def recupMana(self):
        self.__mana=self.__total
    
    def attaquer(self, cible, attaquant:Creature):
        if attaquant not in self.__zone:
            print("Cette créature n'est pas présente sur votre zone de jeu.")
        else:
            cible.perdPv(attaquant.getAtq())
            if type(cible)==Creature and cible.getPv()>0:   #il faudrait pouvoir spécifier à qui appartient la créature attaquée : on attaque ici la creature en général
                attaquant.perdPv(cible.getAtq())
                if attaquant.meurs():
                    self.__zone.remove(attaquant)
                    self.__defausse.append(attaquant)

#TESTS

loup=Creature(1, "Loup", "C'est un loup", 5, 4)
renard=Creature(1, "Renard", "C'est un renard", 4, 3)
feu=Blast(3, "Boule de Feu", "C'est une boule de feu", 5)
cristal_faible=Cristal(1, "Cristal Faible", "C'est un cristal faible", 2)

jean=Mage("Jean", [loup, feu])
nicolas=Mage("Nicolas", [renard, cristal_faible])

print(nicolas.getPv())
jean.attaquer(nicolas, renard)
jean.attaquer(nicolas, loup)
jean.jouerCarte(loup)
jean.attaquer(nicolas, loup)
print(nicolas.getPv())
jean.jouerCarte(feu)
print(jean.getMana())
jean.recupMana()
print(jean.getMana())
jean.jouerCarte(feu)
print(jean.getMana())
print(nicolas.getMana())
nicolas.jouerCarte(cristal_faible)
print(nicolas.getMana())
nicolas.recupMana()
print(nicolas.getMana())
nicolas.jouerCarte(renard)
print(loup.getPv())
print(renard.getPv())
nicolas.attaquer(loup, renard)
print(loup.getPv())
print(renard.getPv())