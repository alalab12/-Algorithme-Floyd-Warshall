import os
from absorb import absorb
from path import get_path
from graph import load_graph, print_matrix, get_matrix_print
from floyd import floyd_warshall


def main():
    run = True
    while run:
        dir = "graphs"
        found = False
        while not found:
            try:
                filename = input("Nom du fichier : ")
                file = os.path.join(dir,filename)
                load = load_graph(file)
                found = True
            except FileNotFoundError:
                print(f"Le fichier '{filename}' n'a pas été trouvé dans le dossier '{dir}'. Veuillez réessayer.")
                continue
        num_vertices = load[0]
        distance_matrix = load[1]

        trace_execution = ""
        
        trace_execution += get_matrix_print(distance_matrix, label="Matrice des poids initiale (L)")
        #print_matrix(distance_matrix, label="Matrice des poids initiale (L)")

        #Appel de Floyd-Warshall
        fw = floyd_warshall(distance_matrix)
        L = fw[0]   # matrice des distances minimales
        P = fw[1]   # matrice des successeurs
        trace_execution += fw[2] # trace de l'exécution de l'algorithme

        trace_execution += get_matrix_print(L, label="Matrice L finale (distances minimales)")
        trace_execution += get_matrix_print(P, label="Matrice P finale (successeurs)")
        #print_matrix(L, label="Matrice L finale (distances minimales)")
        #print_matrix(P, label="Matrice P finale (successeurs)")
        
        if absorb(L):
            trace_execution += "Le graphe est absorbant.\n"
        else:
            # Choix 1 On affiche tout
            trace_execution += "Le graphe n'est pas absorbant.\n"
            print(trace_execution)
            choix_large = input("Que voulez-vous faire ? \n\n1. Afficher tous les chemins\n2. Afficher un ou plusieurs chemins spécifiques\n3. Ne pas afficher de chemins\n : ").lower()
            if choix_large == "1":    
                # on affihe les chemins entre tt les sommets et tt les autres
                num_vertices = len(P)
                for i in range(num_vertices):
                    for j in range(num_vertices):
                        if i != j: # on affiche pas le chemin de i à lui même parce que soit c'est direct lui même soit si c'est moins que ça alors c'est absorbant or là le graphe est pas absorbant 
                            path = get_path(P, i, j)
                            if path is not None:
                                print(f"Le chemin de {i} vers {j} : {' -> '.join(map(str, path))}\n")
                                trace_execution += f"Le chemin de {i} vers {j} : {' -> '.join(map(str, path))}\n"
                            else:
                                print(f"Pas de chemin de {i} vers {j}\n")
                                trace_execution += f"Pas de chemin de {i} vers {j}\n"


            # Choix 2 On affiche que les chemins demandé
            if choix_large == "2":
                choix = "oui"
                while choix != "non":
                    choix = input("\nVoulez-vous observez un chemin ? (oui/non) : ").lower()
                    if choix.lower() == "non":
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

            
        #print(trace_execution)

        print("\n\nFin de l'exécution du programme.\n")
        print("Voulez-vous analyser un autre graphe ? (oui/non) : ", end="")
        if input().lower() != "non":
            run = True
        else:
            run = False


    """dir = "traces_execution"
    file = os.path.join(dir,filename)
    with open(file, "w", encoding="utf-8") as f:
        f.write(trace_execution)"""

if __name__ == "__main__" :
    main()
