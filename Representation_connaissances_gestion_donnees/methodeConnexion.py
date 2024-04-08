def build_connection_graph(KB, alpha):
    """
    Construit un graphe de connexions entre les formules de KB et alpha.
    Args:
        KB (list): Liste de formules de la base de connaissances.
        alpha (str): Formule à prouver.

    Returns:
        dict: Graphe de connexions (représenté sous forme de dictionnaire).
    """
    # Implémentation à compléter (construction du graphe)

def has_connection(graph, start, end):
    """
    Vérifie s'il existe un chemin de start à end dans le graphe.
    Args:
        graph (dict): Graphe de connexions.
        start (str): Formule de départ.
        end (str): Formule d'arrivée.

    Returns:
        bool: True si un chemin existe, False sinon.
    """
    # Implémentation à compléter (recherche de chemin)

# Exemple d'utilisation
KB = ['P or Q', 'R -> S', 'not T']
alpha = 'S'

graph = build_connection_graph(KB, alpha)
print(f"KB |= alpha : {has_connection(graph, 'P or Q', 'S')}")
