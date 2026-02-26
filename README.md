# -Algorithme-Floyd-Warshall

## Fonctionnement fichier graph

### Afin de stocker les graphes dans des fichiers textes nous utiliserons la logique suivante:
```txt
A = Nombre de sommets
B = Nombres d'arête
Pour chaque arête:
    Sommet_de_départ Sommet_d'arrivé Poids_de_l'arete 
```

### Voici un exemple avec graph1 :
```py
4 #Nombre de sommet = 4 soit les sommets {0, 1, 2, 3}
5 #Nombre d'arête = 5
3 1 25 # Arête n°1 de 3 vers 1 avec un poids de 25
1 0 12 # Arête n°2 de 1 vers 0 avec un poids de 12
2 0 -25 # Arête n°3 de 2 vers 0 avec un poids de -25
0 1 0 # Arête n°4 de 0 vers 0 avec un poids de 0
2 1 7 # Arête n°5 de 2 vers 1 avec un poids de 7
```

