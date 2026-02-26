from graph import print_matrix


INF = float('inf')

def floyd_warshall(distance_matrix):
    """
    Implémentation de l'algorithme de Floyd-Warshall pour trouver les plus courts chemins 
    entre tous les couples de sommets dans un graphe pondéré.
    """
    
    num_vertices = len(distance_matrix)

    #1) On copie de la matrice de poids initiale dans L
    L = []
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            row.append(distance_matrix[i][j])
        L.append(row)

    #2) On initialise la matrice des successeurs P
    P = []
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            if distance_matrix[i][j] != INF and i != j: #il existe une arête de i à j
                row.append(j)
            else:
                row.append(None) #pas de successeur direct
        P.append(row)


    #3) On itère sur tous les sommets intermédiaires k
    for k in range(num_vertices):
        print(f"Étape k={k} :")

        for i in range(num_vertices):

            for j in range(num_vertices):

                if L[i][k] != INF and L[k][j] != INF: #on connait  un chemin de i à k et de k à j
                    new_distance = L[i][k] + L[k][j]

                    if L[i][j] > new_distance: #si le chemin passant par k est plus court que le chemin de i à j
                        L[i][j] = new_distance
                        P[i][j] = P[i][k] #le premier sommet après i pour aller vers j est celui de i->k

        print_matrix(L, label=f"Matrice des poids après l'étape k={k} (L)")
        print_matrix(P, label=f"Matrice des successeurs après l'étape k={k} (P)")

    return L, P