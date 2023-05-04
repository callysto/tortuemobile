import os.path
import math

from ipywidgets import widgets
from notebook import nbextensions
from traitlets import Unicode, List
from IPython.display import display

__version__ = '0.5.2'

def install_js():
    pkgdir = os.path.dirname(__file__)
    nbextensions.install_nbextension(os.path.join(pkgdir, 'tortuemobilejs'), user=True)

class Tortue(widgets.DOMWidget):
    _view_module = Unicode("nbextensions/tortuemobilejs/turtlewidget").tag(sync=True)
    _view_name = Unicode('TurtleView').tag(sync=True)
    points = List(sync=True)

    SIZE = 400
    OFFSET = 20
    def __init__(self):
        '''Créer une tortue

        exemple::

            t = Tortue()
        '''
        super(Tortue, self).__init__()
        install_js()
        display(self)
        self.stylo = 1
        self.vitesseVar = 1
        self.couleur = "black"
        self.cap = 90
        self.points = []
        self.origine()

    def styloenbas(self):
        '''La tortue trace des lignes. Les tortues commencent avec leur stylo en bas.

        exemple::

            t.styloenbas()
        '''
        self.stylo = 1

    def styloenhaut(self):
        '''Lever le stylo.

        exemple::

            t.styloenhaut()
        '''
        self.stylo = 0

    def vitesse(self, vitesse):
        '''Régler la vitesse de la tortue (1 à 10).

        exemple::

            t.vitesse(10) # vitesse maximum
        '''
        self.vitesseVar = min(max(1, vitesse), 10)

    def droite(self, num):
        '''Tourner lar tortue vers la droite d'un certain nombre de degrés.

        exemple::

            t.droite(90)
        '''
        self.cap += num
        self.cap = self.cap%360
        self.b_change = num
        self._ajoute_point()

    def gauche(self, num):
        '''Tourner lar tortue vers la gauche d'un certain nombre de degrés.

        exemple::

            t.gauche(90)
        '''
        self.cap -= num
        self.cap = self.cap%360
        self.b_change = -num
        self._ajoute_point()

    def avant(self, num):
        '''Faire avancer la tortue d'un certain nombre de pixels.

        exemple:

            t.avant(100)
        '''
        self.posX += round(num * math.sin(math.radians(self.cap)), 1)
        self.posY -= round(num * math.cos(math.radians(self.cap)), 1)

        if self.posX < Tortue.OFFSET:
            self.posX = Tortue.OFFSET
        if self.posY < Tortue.OFFSET:
            self.posY = Tortue.OFFSET

        if self.posX > Tortue.SIZE - Tortue.OFFSET:
            self.posX = Tortue.SIZE - Tortue.OFFSET
        if self.posY > Tortue.SIZE - Tortue.OFFSET:
            self.posY = Tortue.SIZE - Tortue.OFFSET

        self.b_change = 0
        self._ajoute_point()

    def recule(self, num):
        '''Faire reculer la tortue d'un certain nombre de pixels.

        exemple::

            t.recule(100)
        '''
        self.posX -= round(num * math.sin(math.radians(self.cap)), 1)
        self.posY += round(num * math.cos(math.radians(self.cap)), 1)

        if self.posX < Tortue.OFFSET:
            self.posX = Tortue.OFFSET
        if self.posY < Tortue.OFFSET:
            self.posY = Tortue.OFFSET

        if self.posX > Tortue.SIZE - Tortue.OFFSET:
            self.posX = Tortue.SIZE - Tortue.OFFSET
        if self.posY > Tortue.SIZE - Tortue.OFFSET:
            self.posY = Tortue.SIZE - Tortue.OFFSET

        self.b_change = 0
        self._ajoute_point()

    def couleurstylo(self, couleur):
        '''Modifier la couleur du stylo. Les noms des couleurs sont en anglais.

        exemple::

            t.couleurstylo("red")
        '''
        self.couleur = couleur

    def position(self, x, y, capVar=None):
        """Déplacer la tortue à une position spécifique, (0,0) est en haut à gauche et (400, 400) est en bas à droite.

        exemple::

            t.position(100, 100)
        """
        self.posX = x
        self.posY = y
        if capVar is None:
            self._ajoute_point()
        elif isinstance(capVar, int):
            self.fixecap(capVar)
        else:
            raise ValueError("Le cap doit être un nombre entier")

    def fixecap(self, capVar):
        """Fixer le cap de la tortue à un certain nombre de degrés.

        exemple::

            t.fixecap(180)
        """
        diff = self.cap - capVar
        self.b_change = diff
        self.cap = capVar
        self._ajoute_point()
        self.b_change = 0

    def _ajoute_point(self):
        p = dict(p=self.stylo, lc=self.couleur, x=self.posX, y=self.posY,
                 b=self.b_change, s=self.vitesseVar)
        self.points = self.points + [p]

    def cercle(self, radius, extent=360):
        """Faire dessiner à la tortue un morceau de cercle de rayon égal à un certain nombre de degrés.
        
        Un rayon positif fait tourner la tortue vers la gauche, un rayon négatif la fait tourner vers la droite.

        exemple::

            t.cercle(50, 180)
        """
        temp = self.cap
        self.b_change = 0;
        vitesseTemp = self.vitesseVar
        self.vitesseVar = 1

        for i in range(0, int(extent//2)):
            n = math.fabs(math.radians(self.b_change) * radius)
            if(radius >= 0):
                self.avant(n)
                self.gauche(2)
            else:
                self.avant(n)
                self.droite(2)
        if(radius >= 0):
            self.cap = (temp + extent)
        else:
            self.cap = (temp - extent)
        self.vitesseVar = vitesseTemp

    def origine(self):
        '''Remettre la tortue au centre de l'écran.

        exemple::

            t.origine()
        '''
        self.posX = 200
        self.posY = 200
        if 90 < self.cap <=270:
            self.b_change = - (self.cap - 90)
        else:
            self.b_change = 90 - self.cap
        self.cap = 90
        self._ajoute_point()
