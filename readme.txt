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
     |  Incert(terme=0, tolerance=-1)
     |  
     |  Classe permettant d'associer son incertitude � une grandeur physique.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, terme2)
     |      Additionne deux termes Incert.
     |  
     |  __eq__(self, terme2)
     |      V�rifie l'�galit� de deux objets Incert
     |  
     |  __init__(self, terme=0, tolerance=-1)
     |      Initialise un �l�ment de class Incert.
     |  
     |  __mul__(self, terme2)
     |      Multiplie deux termes Incert.
     |  
     |  __neg__(self)
     |      Calcule l'oppos� d'un terme Incert.
     |  
     |  __pow__(self, terme2)
     |      El�ve � la puissance un terme Incert.
     |  
     |  __radd__(self, terme2)
     |      Addition � gauche d'un Incert.
     |  
     |  __repr__(self)
     |      Affichage d'un terme Incert.
     |  
     |  __rmul__(self, terme2)
     |      Multiplication � gauche d'un Incert.
     |  
     |  __rsub__(self, terme2)
     |      Soustraction � gauche d'un Incert.
     |  
     |  __rtruediv__(self, terme2)
     |      Division � gauche.
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
    
    atan2(y, x)
        Calcule l'arc tangente de y/x en tenant compte des signes de y et de x
    
    cos(terme)
        Calcule le cosinus du terme avec son incertitude.
    
    decomp(chaine_nombre)
        D�compose un nombre sous forme de chaine en une liste contenant :
        [0] la partie enti�re
        [1] la partie d�cimale
        [2] la puissance de dix
    
    exp(terme)
        Calcule l'exponentielle du terme avec son incertitude type.
    
    i(terme='')
        Saisie rapide d'un Incert (sans tol�rance).
    
    iabs(terme)
        Calcule la valeur absolue du terme avec son incertitude.
    
    it(terme='', tolerance=-1)
        saisie rapide d'un Incert avec tol�rance.
    
    ln(terme)
        Calcule le logarithme n�p�rien du terme avec son incertitude type.
    
    resol(liste_nombre)
        D�termine la r�solution d'un nombre exprim� sous forme de liste
        contenant :
        [0] la partie enti�re
        [1] la partie d�cimale
        [2] la puissance de dix
    
    sin(terme)
        Calcule le sinus du terme avec son incertitude.
    
    sqrt(terme)
        Calcule la racine carr�e du terme avec son incertitude.
    
    tan(terme)
        Calcule la tangente du terme avec son incertitude.
    
    todec(terme)
        Transforme un terme au format sexag�simal vers d�cimal.
    
    tosexag(terme)
        Transforme un terme au format sexag�simal.

DATA
    pi = +3.141593E+00(0 op�ration) 2.887E-16(u type) 9...type %) 4.8E-...
    un = +1.000000E+00(0 op�ration) 0.000E+00(u type) 0...type %) 0.0E+...
    zero = +0.000000E+00(0 op�ration) 0.000E+00(u type) (...ssible) 0.0...

FILE
    c:\users\mc\documents\python\mes_modules\incertitudes\incert.py


