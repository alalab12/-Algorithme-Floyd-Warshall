import os
from absorb import absorb
from path import get_path
from graph import load_graph, print_matrix
from floyd import floyd_warshall


def main():

    dir = "graphs"
    filename = input("Nom du fichier : ")

    file = os.path.join(dir,filename)

    load = load_graph(file)
    num_vertices = load[0]
    distance_matrix = load[1]


    print_matrix(distance_matrix, label="Matrice des poids initiale (L)")

    #Appel de Floyd-Warshall
    fw = floyd_warshall(distance_matrix)
    L = fw[0]   # matrice des distances minimales
    P = fw[1]   # matrice des successeurs


    print_matrix(L, label="Matrice L finale (distances minimales)")
    print_matrix(P, label="Matrice P finale (successeurs)")
    
    if absorb(L):
        print("Le graphe est absorbant.")
    else:
        # Choix 1 On affiche tout
        print("Le graphe n'est pas absorbant.")
        # on affihe les chemins entre tt les sommets et tt les autres
        num_vertices = len(P)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if i != j: # on affiche pas le chemin de i à lui même parce que soit c'est direct lui même soit si c'est moins que ça alors c'est absorbant or là le graphe est pas absorbant 
                    path = get_path(P, i, j)
                    if path is not None:
                        print(f"Le chemin de {i} vers {j} : {' -> '.join(map(str, path))}")
                    else:
                        print(f"Pas de chemin de {i} vers {j}")
        
        # Choix 2 On affiche que les chemins demandé
        """
        choix = "oui"
        while choix == "oui":
            choix = input("\nVoulez-vous observez un chemin ? (oui/non) : ").lower()
            if choix != "oui":
                print("Arrêt du programme.")
                break
                
            else:
                start = int(input(f"Sommet de départ (0 à {len(L)-1}) : "))
                end = int(input(f"Sommet d'arrivée (0 à {len(L)-1}) : "))

                
                if P[start][end] is None:
                    print(f"Il n'y a aucun chemin entre {start} et {end}.")
                else:
                    chemin = get_path(P, start, end)
                    print(f"-> Valeur minimale : {L[start][end]}")
                    print(f"-> Chemin : {' -> '.join(map(str, chemin))}")

        """

if __name__ == "__main__" :
    main()
