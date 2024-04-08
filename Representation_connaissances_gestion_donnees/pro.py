def eval_proposition(proposition, variables):
    """
    Évalue une proposition propositionnelle donnée en utilisant les valeurs des variables.
    Args:
        proposition (str): La proposition propositionnelle.
        variables (dict): Un dictionnaire associant les noms des variables à leurs valeurs (0 ou 1).

    Returns:
        bool: True si la proposition est vraie, False sinon.
    """
    stack = []
    for token in proposition.split():
        if token in variables:
            stack.append(variables[token])
        elif token == 'not':
            operand = stack.pop()
            stack.append(not operand)
        elif token == 'and':
            operand2, operand1 = stack.pop(), stack.pop()
            stack.append(operand1 and operand2)
        elif token == 'or':
            operand2, operand1 = stack.pop(), stack.pop()
            stack.append(operand1 or operand2)
        elif token == 'if':
            operand2, operand1 = stack.pop(), stack.pop()
            stack.append(not operand1 or operand2)
        elif token == 'then':
            operand2, operand1 = stack.pop(), stack.pop()
            stack.append(not operand1 or operand2)
        elif token == 'iff':
            operand2, operand1 = stack.pop(), stack.pop()
            stack.append(operand1 == operand2)
    return stack[0]

# Exemple d'utilisation
variables = {'a': 1, 'b': 0}
proposition1 = 'a b and'
proposition2 = 'a b or'
proposition3 = 'a not a'
proposition4 = 'a b if'
proposition5 = 'a b iff'

print(f"Résultat proposition 1: {eval_proposition(proposition1, variables)}")
print(f"Résultat proposition 2: {eval_proposition(proposition2, variables)}")
print(f"Résultat proposition 3: {eval_proposition(proposition3, variables)}")
print(f"Résultat proposition 4: {eval_proposition(proposition4, variables)}")
print(f"Résultat proposition 5: {eval_proposition(proposition5, variables)}")