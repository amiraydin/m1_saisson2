import ply.lex as lex
import ply.yacc as yacc

# Liste des tokens
tokens = (
    'ATOM',
    'NOT',
    'AND',
    'OR',
    'IMPLIES',
    'IFF',
    'LPAREN',
    'RPAREN',
)

# Définition des tokens
t_ATOM = r'[a-zA-Z]+'
t_NOT = r'¬ | not'
t_AND = r'∧|and'
t_OR = r'∨|or'
t_IMPLIES = r'→|if.+then'
t_IFF = r'↔|iff'

t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Gérer les sauts de ligne
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Gérer les erreurs de token
def t_error(t):
    print("Caractère non valide : '%s'" % t.value[0])
    t.lexer.skip(1)

# Créer l'analyseur lexical
lexer = lex.lex()

# Définition des règles de syntaxe
def p_formula(p):
    '''formula : atom
                | NOT formula
                | formula AND formula
                | formula OR formula
                | formula IMPLIES formula
                | formula IFF formula
                | LPAREN formula RPAREN'''
    pass

def p_atom(p):
    '''atom : ATOM'''
    pass

# Gérer les erreurs de syntaxe
def p_error(p):
    if p:
        print("Erreur de syntaxe près de '%s'" % p.value)
    else:
        print("Erreur de syntaxe à la fin de l'entrée")

# Créer l'analyseur syntaxique
parser = yacc.yacc()

# Fonction de vérification de la formule
def verify_formula(input_formula):
    lexer.input(input_formula)
    try:
        parsed = parser.parse(input_formula)
        corrected_formula = parsed_to_string(parsed)
        return True, corrected_formula
    except:
        return False, ""

# Convertir l'arbre syntaxique parsé en une chaîne de caractères
def parsed_to_string(parsed):
    if len(parsed) == 1:
        return parsed[0]
    elif len(parsed) == 2:
        if parsed[0] == 'NOT':
            return "¬" + parsed_to_string(parsed[1])
        else:
            return "(" + parsed_to_string(parsed[1]) + ")"
    else:
        return "(" + parsed_to_string(parsed[1]) + " " + parsed[0] + " " + parsed_to_string(parsed[2]) + ")"

# Remplacer les connecteurs logiques par leurs équivalents
def replace_connectors(formula):
    formula = formula.replace("and", " ∧ ")
    formula = formula.replace("or", " ∨ ")
    formula = formula.replace("then", " -> ")
    formula = formula.replace("iff", " <-> ")
    return formula

# Exemple d'utilisation
if __name__ == '__main__':
    user_input = input("Entrez une formule propositionnelle : ")
    valid, corrected_formula = verify_formula(user_input)
    if valid:
        corrected_formula = replace_connectors(corrected_formula)
        print("Formule correcte :", corrected_formula)
    else:
        print("Formule incorrecte")
