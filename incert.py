#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: incert.py
# Auteur: Marc COATANHAY

"""
    Module python pour effectuer les calculs d'incertitudes
    de grandeurs physiques
"""

# Import des modules
import math


# Définitions fonctions et classes
def acos(terme):
    """Calcule l'arc cosinus du terme avec son incertitude"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.acos(terme.valeur)
        if((1 - terme.valeur**2) != 0):
            resultat.incert = (1 / math.sqrt(1 - terme.valeur**2))*terme.incert
        else:
            resultat.incert = 1E99*terme.incert
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return acos(Incert(terme))

def asin(terme):
    """Calcule l'arc sinus du terme avec son incertitude"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.asin(terme.valeur)
        if((1 - terme.valeur**2) != 0):
            resultat.incert = (1 / math.sqrt(1 - terme.valeur**2))*terme.incert
        else:
            resultat.incert = 1E99*terme.incert
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return asin(Incert(terme))

def atan(terme):
    """Calcule l'arc tangente du terme avec son incertitude"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.atan(terme.valeur)
        resultat.incert = (1 / (1 + terme.valeur**2))*terme.incert
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return asin(Incert(terme))

def cos(terme):
    """Calcule le cosinus du terme avec son incertitude"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.cos(terme.valeur)
        resultat.incert = abs(math.sin(terme.valeur)*terme.incert)
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return cos(Incert(terme))

def decomp(chaine_nombre):
    """Décompose un nombre sous forme de chaine en une liste contenant :
    [0] la partie entière
    [1] la partie décimale
    [2] la puissance de dix"""
    # Séparation de la partie décimale autour du symbole "."
    liste_1 = chaine_nombre.upper().split(".")
    len_liste_1 = len(liste_1)
    if(len_liste_1 == 2):
        # Une partie décimale est précisée
        liste_nombre = [liste_1[0]]
        # Séparation de la puissance de dix autour de la lettre "E"
        liste_2 = liste_1[1].split("E")
        liste_nombre.append(liste_2[0])
        if(len(liste_2) == 2):
            # Une puissance de dix est précisée
            liste_nombre.append(liste_2[1])
        else:
            # Pas de puissance de dix précisée
            # Donc on prend zéro
            liste_nombre.append('0')
    elif(len_liste_1 == 1):
        # Pas de partie décimale précisée
        # Séparation de la puissance de dix autour de la lettre "E"
        liste_2 = liste_1[0].split("E")
        liste_nombre = [liste_2[0], '']
        if(len(liste_2) == 2):
            # Une puissance de dix est précisée
            liste_nombre.append(liste_2[1])
        else:
            # Pas de puissance de dix précisée
            # donc on prend zéro
            liste_nombre.append('0')
    return liste_nombre

def exp(terme):
    """Calcule l'exponentielle du terme avec son incertitude type"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.exp(terme.valeur)
        resultat.incert = math.exp(terme.valeur)*terme.incert
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return exp(Incert(terme))

def i(terme=""):
    """Saisie rapide d'un Incert (sans tolérance)"""
    if(terme==""):
        return Incert(input("Entrer la valeur : "), -1)
    else:
        return Incert(terme, -1)

def it(terme="", tolerance=-1):
    """saisie rapide d'un Incert avec tolérance"""
    if(terme==""):
        terme = input("Entrer la valeur : ")
    if(tolerance==-1):
        tolerance = input("Entrer la tolérance : ")
    if(tolerance == ""):
        tolerance = 0
    print(tolerance)
    return Incert(terme, float(tolerance))

def ln(terme):
    """Calcule le logarithme népérien du terme avec son incertitude type"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.log(terme.valeur)
        resultat.incert = terme.incert/terme.valeur
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return ln(Incert(terme))

def resol(liste_nombre):
    """Détermine la résolution d'un nombre exprimé sous forme de liste contenant :
    [0] la partie entière
    [1] la partie décimale
    [2] la puissance de dix"""
    nb_decimales = len(liste_nombre[1])
    resolution = 10**(int(liste_nombre[2]) - nb_decimales)
    return resolution

def sin(terme):
    """Calcule le sinus du terme avec son incertitude"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.sin(terme.valeur)
        resultat.incert = abs(math.cos(terme.valeur)*terme.incert)
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return sin(Incert(terme))

def tan(terme):
    """Calcule la tangente du terme avec son incertitude"""
    if(type(terme) == Incert):
        resultat = Incert()
        resultat.valeur = math.tan(terme.valeur)
        resultat.incert = abs((1 + math.tan(terme.valeur)**2)*terme.incert)
        resultat.elargissements = [("95%", 2), ("99%", 3)]
        resultat.operations = terme.operations + 1
        resultat.effectif = 0
        return resultat
    else:
        return tan(Incert(terme))

class Incert():
    """Classe permettant d'associer les incertitudes à différents calculs"""
    def __add__(self, terme2):
        """Additionne deux termes Incert"""
        if(type(terme2) == Incert):
            resultat = Incert()
            resultat.valeur = self.valeur + terme2.valeur
            resultat.incert = math.sqrt(self.incert**2 + terme2.incert**2)
            resultat.elargissements = [("95%", 2), ("99%", 3)]
            resultat.operations = self.operations + terme2.operations + 1
            resultat.effectif = 0
            return resultat
        else:
            return self + Incert(terme2)

    def __init__(self, terme=0, tolerance=-1):
        """Initialise un élément de class Incert"""
        if(type(terme) == str):
            if(terme != ""):
                self.valeur = float(terme)
                chaine_nombre = terme
            else:
                self.valeur = 0
                tolerance = 0
        elif(type(terme) == int):
            self.valeur = terme
            tolerance = 0
        elif(type(terme) == float):
            self.valeur = terme
            chaine_nombre = str(terme)
        else:
            self.valeur = 0
            tolerance = 0
        if(tolerance == -1):
            self.incert = resol(decomp(chaine_nombre))/math.sqrt(12)
            self.elargissements = [("95%", 1.65), ("99%", 1.72)]
        else:
            self.incert = tolerance / math.sqrt(3)
            self.elargissements = [("95%", 1.96), ("99%", 2.58)]
        self.operations = 0
        self.effectif = 0

    def __mul__(self, terme2):
        """Multiplie deux termes Incert"""
        if(type(terme2) == Incert):
            resultat = Incert()
            resultat.valeur = self.valeur * terme2.valeur
            resultat.incert = math.sqrt(
                (self.incert*terme2.valeur)**2
                + (terme2.incert*self.valeur)**2)
            resultat.elargissements = [("95%", 2), ("99%", 3)]
            resultat.operations = self.operations + terme2.operations + 1
            resultat.effectif = 0
            return resultat
        else:
            return self*Incert(terme2)

    def __neg__(self):
        """Calcule l'opposé d'un terme Incert"""
        self.valeur = - self.valeur
        return self

    def __pow__(self, terme2):
        """Elève à la puissance un terme Incert"""
        if(type(terme2) == Incert):
            resultat = Incert()
            resultat.valeur = math.exp(terme2.valeur*math.log(self.valeur))
            resultat.incert = resultat.valeur*math.sqrt(
                (terme2.valeur*self.incert/self.valeur)**2 +
                (math.log(self.valeur)*terme2.incert)**2)
            resultat.elargissements = [("95%", 2), ("99%", 3)]
            resultat.operations = self.operations + terme2.operations + 1
            resultat.effectif = 0
            return resultat
        elif(type(terme2) == int):
            resultat = Incert()
            resultat.valeur = self.valeur ** terme2
            resultat.incert = self.incert*terme2*self.valeur**(terme2 - 1)
            resultat.elargissements = [("95%", 2), ("99%", 3)]
            resultat.operations = self.operations + 1
            resultat.effectif = 0
            return resultat
        else:
            return self**Incert(terme2)

    def __radd__(self, terme2):
        """Addition à gauche d'un Incert"""
        return self + terme2

    def __rmul__(self, terme2):
        """Multiplication à gauche d'un Incert"""
        return self * terme2

    def __rsub__(self, terme2):
        """Soustraction à gauche d'un Incert"""
        return -self + terme2

    def __rtruediv__(self, terme2):
        """Division à gauche"""
        return Incert(terme2) / self

    def __repr__(self):
        """Affichage d'un terme Incert"""
        # -------------------------------------------------------------
        # Valeur
        # -------------------------------------------------------------
        if(self.valeur < 0):
            signe = "-"
            valeur = - self.valeur
        else:
            signe = "+"
            valeur = self.valeur
        chaine = signe + format(valeur, 'E')
        if(self.operations > 1):
            pluriel = "s"
        else:
            pluriel = ""
        chaine += "(" + str(self.operations) + " opération" + pluriel + ")"
        # -------------------------------------------------------------
        # Incertitude type
        # -------------------------------------------------------------
        chaine += "\r " + format(self.incert, '0.3E')
        chaine += "(u type)"
        # -------------------------------------------------------------
        # Incertitudes élargies
        # -------------------------------------------------------------
        for (niveau, k) in self.elargissements:
            elargissement = self.incert*k
            chaine += "\r " + format(elargissement, '0.1E')
            chaine += "(" + niveau + ",k=" + str(k)
            if(self.effectif != 0):
                chaine += ",n=" + str(self.effectif) + ")"
            else:
                chaine += ")"
        return chaine

    def __sub__(self, terme2):
        """Soustraction de deux termes Incert"""
        if(type(terme2) == Incert):
            resultat = Incert()
            resultat.valeur = self.valeur - terme2.valeur
            resultat.incert = math.sqrt(self.incert**2 + terme2.incert**2)
            resultat.elargissements = [("95%", 2), ("99%", 3)]
            resultat.operations = self.operations + terme2.operations + 1
            resultat.effectif = 0
            return resultat
        else:
            return self - Incert(terme2)

    def __truediv__(self, terme2):
        """Division de deux termes Incert"""
        if(type(terme2) == Incert):
            resultat = Incert()
            resultat.valeur = self.valeur / terme2.valeur
            resultat.incert = (1/terme2.valeur**2)*math.sqrt(
                (self.incert*terme2.valeur)**2
                + (terme2.incert*self.valeur)**2)
            resultat.elargissements = [("95%", 2), ("99%", 3)]
            resultat.operations = self.operations + terme2.operations + 1
            resultat.effectif = 0
            return resultat
        else:
            return self/Incert(terme2)

pi = Incert(math.pi)
zero = Incert(0)
un = Incert(1)
