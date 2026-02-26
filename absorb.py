def absorb(L):
    """
    Retourne True ou False selon que le graphe représenté par la matrice L est absorbant ou non.
    """
    num_vertices = len(L)

    for i in range(num_vertices):
        if L[i][i] < 0: # si il existe un chemin de i à lui même de poids négatif, alors le graphe est absorbant
            return True
    return False