# TortueMobile

Ceci est un module pour les tortues dans les cahiers Jupyter. C'est une traduction française de [mobilechelonian](https://github.com/takluyver/mobilechelonian) de [Thomas Kluyver](https://github.com/takluyver).

## Installation

`pip install tortuemobile`

## Utilisation

```python
import tortuemobile
t = tortuemobile.Tortue()
```

|Commande|Description|Exemple|
|-|-|-|
|`t.vitesse(entier)`|la vitesse de votre tortue, de 1 à 10|`t.vitesse(10)`|
|`t.droite(degrés)`|tourner votre tortue vers la droite d'un certain nombre de degrés|`t.droite(90)`|
|`t.gauche(degrés)`|tourner la tortue vers la gauche d'un certain nombre de degrés|`t.gauche(45)`|
|`t.avant(pixels)`|faire avancer la tortue d'un certain nombre de pixels|`t.avant(100)`|
|`t.recule(pixels)`|faire reculer la tortue d'un certain nombre de pixels|`t.retraite(20)`|
|`t.cercle(rayon, degrés)`|faire dessiner à la tortue un morceau de cercle de rayon égal à un certain nombre de degrés|`t.cercle(40, 360)`|
|`t.styloenhaut()`|ta tortue peut maintenant se déplacer sans tracer des lignes|`t.styloenhaut()`|
|`t.styloenbas()`|ta tortue trace à nouveau des lignes|`t.styloenbas()`|
|`t.couleurstylo('color')`|couleur de la ligne de votre tortue en utilisant un [nom de couleur](https://www.w3schools.com/colors/colors_names.asp)|`t.couleurstylo('blue')`|
|`t.couleurstylo('rgb(R, V, B)')`|couleur de la ligne de votre tortue en utilisant valeurs de rouge, vert, et bleu de 0 à 255|`t.pencolor('rgb(0, 255, 100)')`|
|`t.origine()`|remettre la tortue au centre de l'écran|`t.origine()`|
|`t.position(x, y)`|déplacer la tortue à une position spécifique, (0,0) est en haut à gauche et (400, 400) est en bas à droite|`t.position(100, 250)`|
|`t.fixecap(degrés)`|fixer le cap de la tortue à un certain nombre de degrés|`t.cap(90)`|
