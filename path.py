def get_path(P, i, j):
    """
    Retourne le chemin le plus court entre les sommets i et j en utilisant la matrice des successeurs P
    """
    if P[i][j] is None:
        return None  # pas de chemin entre i et j
    
    path = [i] # le chemin commence par i

    while i != j: # tant que le chemin est pas fini
        i = P[i][j] # i devient le successeur de i sur le chemin vers j
        path.append(i) # et on l'ajoute au chemin
    return path