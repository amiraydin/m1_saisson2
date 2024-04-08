def transform_to_cnf(formula):
    """
    Transforme une formule en forme normale conjonctive (CNF).
    Args:
        formula (str): La formule propositionnelle.

    Returns:
        list: Liste de clauses (chaque clause est une liste de littéraux).
    """
    # Implémentation à compléter (conversion en CNF)

def resolution(KB, alpha):
    """
    Vérifie si KB |= alpha en utilisant la méthode de résolution.
    Args:
        KB (list): Liste de clauses (formules de la base de connaissances).
        alpha (list): Liste de littéraux (formule à prouver).

    Returns:
        bool: True si KB |= alpha, False sinon.
    """
    # Implémentation à compléter (application de la résolution)

# Exemple d'utilisation
KB = [
    ['not', 'P', 'Q'],
    ['R', 'S'],
    ['not', 'R', 'T']
]
alpha = ['T']

print(f"KB |= alpha : {resolution(KB, alpha)}")

## Méthode de résolution :

##    Supposons que nous ayons la base de connaissances (KB) suivante :
##        KB = {¬P ∨ Q, R → S, ¬R ∨ T}
##    Et nous voulons prouver la formule α = T.
##    Nous transformons KB en forme normale conjonctive (CNF) :
##        KB = {(¬P ∨ Q), (¬R ∨ T), (¬R ∨ S)}
##    Ensuite, nous appliquons la résolution pour dériver une clause vide :
##        (¬R ∨ T) et (¬R ∨ S) => (¬R ∨ T ∨ S)
##        (¬P ∨ Q) et (¬R ∨ T ∨ S) => (¬P ∨ Q ∨ T ∨ S)
##        KB |= T (car nous avons obtenu une clause vide)
##    Donc, KB peut prouver α = T.