import os
from graph import load_graph, print_matrix


def main():

    dir = "graphs"
    filename = input("Nom du fichier : ")

    file = os.path.join(dir,filename)

    result = load_graph(file)
    num_vertices = result[0]
    distance_matrix = result[1]


    print_matrix(distance_matrix, label="Matrice des poids initiale (L)")
    

if __name__ == "__main__" :
    main()