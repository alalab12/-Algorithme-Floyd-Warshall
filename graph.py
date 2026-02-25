INF = float('inf')

def load_graph(filename):
    """
    n : nombre de sommets (num_vertices)
    m: nombre d'arcs  (num_edges)
    Lignes suivantes  : u v w
          - u : sommet de départ
          - v : sommet d'arrivée
          - w : poids de l'arc de u vers v
    """

    # 1) On ouvre le fichier en lecture
    with open(filename, "r", encoding="utf-8") as f: 
        lines = [] 
        for line in f :
            stripped = line.strip()  # enlève les espaces + \n
            if stripped : # on garde que les lignes non vides
                lines.append(stripped)


    # 2) On lit le nombre de sommets (n) et le nombre d'arcs (m)
    num_vertices = int(lines[0]) # On récupère le nombre de sommets
    num_edges = int(lines[1]) # On récupère le nombre d'arcs

    # 3) On crée la matrice des distances de taille n x n remplie avec INF
    #Créer une fonction juste avec l'initialisation de la matrice ?
    distances_matrix = []

    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            """
            Pour l'instant on considère qu'il n'existe aucun chemin de i vers j,
            donc on met la distance à INF (infini)
            """
            row.append(INF) 
            
        distances_matrix.append(row)

    # 4) On met la distance de chaque sommet vers lui-même à 0

    for i in range(num_vertices):
        # Distance de chaque sommet à lui-même = 0
        distances_matrix[i][i] = 0

    # 5) On lit maintenant les arcs un par un dans les lignes suivantes
    for line in lines[2:2 + num_edges]:

        parts = line.split()
        u = int(parts[0])
        v = int(parts[1])
        w = int(parts[2])

        # la distance de u vers v = w
        distances_matrix[u][v] = w

    return num_vertices, distances_matrix



    

    





def print_matrix(matrix, label=""):
    """
    Afficher une matrice avec les indices de sommets et indique le nom de la matrice
    """
    n = len(matrix)

    if label:
        print(label)

    # En-tête colonnes
    print("     ", end="")

    for j in range(n):
        print(f"{j:>6}", end="")
    print()

    # Lignes
    for i in range(n):
        print(f"{i:>3} |", end="")

        for j in range(n):
            val = matrix[i][j]

            if val == float('inf'):
                s = "INF"
            else:
                s = str(val)

            print(f"{s:>6}", end="")

        print()

    print()
    


