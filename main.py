import os
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
    

if __name__ == "__main__" :
    main()
