import ply.lex as lex
import ply.yacc as yacc

# Liste des tokens
tokens = (
    'ATOM',
    'NOT',
    'AND',
)

# Définition des tokens
t_NOT = r'¬ | not'
t_AND = r'∧ | and'

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Règle pour les atomes
def t_ATOM(t):
    r'[a-zA-Z]+'
    return t

# Gérer les erreurs de token
def t_error(t):
    print(f"Caractère non valide : '{t.value[0]}'")
    t.lexer.skip(1)

# Créer l'analyseur lexical
lexer = lex.lex()

# Définition des règles de syntaxe
def p_formula(p):
    '''formula : NOT atom
                | atom AND atom'''
    pass

def p_atom(p):
    '''atom : ATOM'''
    pass

# Gérer les erreurs de syntaxe
def p_error(p):
    if p:
        print(f"Erreur de syntaxe près de '{p.value}'")
    else:
        print("Erreur de syntaxe à la fin de l'entrée")
    return False


# Créer l'analyseur syntaxique
parser = yacc.yacc()

# Fonction de vérification de la formule
def verify_formula(input_formula):
    lexer.input(input_formula)
    try:
        parsed = parser.parse(input_formula, lexer=lexer)
        corrected_formula = parsed_to_string(parsed)
        return True, corrected_formula
    except:
        return False, ""

# Convertir l'arbre syntaxique parsé en une chaîne de caractères
def parsed_to_string(parsed):
    if len(parsed) == 2:
        if parsed[0] == 'NOT':
            return "¬" + parsed_to_string(parsed[1])
        elif parsed[0] == 'AND':
            return "(" + parsed_to_string(parsed[1]) + " ^ " + parsed_to_string(parsed[2]) + ")"
    else:
        return parsed[1]

# Exemple d'utilisation
if __name__ == '__main__':
    user_input = input("Entrez une formule propositionnelle : ")
    valid, corrected_formula = verify_formula(user_input)
    if valid:
        print("Formule correcte :", corrected_formula)
    else:
        print("Formule incorrecte")
