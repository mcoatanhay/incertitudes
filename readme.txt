Help on module incert:

NAME
    incert

DESCRIPTION
    Module python pour effectuer les calculs d'incertitudes
    de grandeurs physiques.

CLASSES
    builtins.object
        Incert
    
    class Incert(builtins.object)
     |  Classe permettant d'associer son incertitude à une grandeur physique.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, terme2)
     |      Additionne deux termes Incert.
     |  
     |  __eq__(self, terme2)
     |      Vérifie l'égalité de deux objets Incert
     |  
     |  __init__(self, terme=0, tolerance=-1)
     |      Initialise un élément de class Incert.
     |  
     |  __mul__(self, terme2)
     |      Multiplie deux termes Incert.
     |  
     |  __neg__(self)
     |      Calcule l'opposé d'un terme Incert.
     |  
     |  __pow__(self, terme2)
     |      Elève à la puissance un terme Incert.
     |  
     |  __radd__(self, terme2)
     |      Addition à gauche d'un Incert.
     |  
     |  __repr__(self)
     |      Affichage d'un terme Incert.
     |  
     |  __rmul__(self, terme2)
     |      Multiplication à gauche d'un Incert.
     |  
     |  __rsub__(self, terme2)
     |      Soustraction à gauche d'un Incert.
     |  
     |  __rtruediv__(self, terme2)
     |      Division à gauche.
     |  
     |  __sub__(self, terme2)
     |      Soustraction de deux termes Incert.
     |  
     |  __truediv__(self, terme2)
     |      Division de deux termes Incert.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None

FUNCTIONS
    acos(terme)
        Calcule l'arc cosinus du terme avec son incertitude.
    
    asin(terme)
        Calcule l'arc sinus du terme avec son incertitude.
    
    atan(terme)
        Calcule l'arc tangente du terme avec son incertitude.
    
    cos(terme)
        Calcule le cosinus du terme avec son incertitude.
    
    decomp(chaine_nombre)
        Décompose un nombre sous forme de chaine en une liste contenant :
        [0] la partie entière
        [1] la partie décimale
        [2] la puissance de dix
    
    exp(terme)
        Calcule l'exponentielle du terme avec son incertitude type.
    
    i(terme='')
        Saisie rapide d'un Incert (sans tolérance).
    
    it(terme='', tolerance=-1)
        saisie rapide d'un Incert avec tolérance.
    
    ln(terme)
        Calcule le logarithme népérien du terme avec son incertitude type.
    
    resol(liste_nombre)
        Détermine la résolution d'un nombre exprimé sous forme de liste
        contenant :
        [0] la partie entière
        [1] la partie décimale
        [2] la puissance de dix
    
    sin(terme)
        Calcule le sinus du terme avec son incertitude.
    
    tan(terme)
        Calcule la tangente du terme avec son incertitude.
    
    todec(terme)
        Transforme un terme au format sexagésimal vers décimal.
    
    tosexag(terme)
        Transforme un terme au format sexagésimal.

DATA
    pi = +3.141593E+00(0 opération) 2.887E-16(u type) 4.8E-16(95%,k=1.65...
    un = +1.000000E+00(0 opération) 0.000E+00(u type) 0.0E+00(95%,k=1.96...
    zero = +0.000000E+00(0 opération) 0.000E+00(u type) 0.0E+00(95%,k=1....

FILE
    c:\users\mc\mu_code\_mes_modules\incertitudes\incert.py


