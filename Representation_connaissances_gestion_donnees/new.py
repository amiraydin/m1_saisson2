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
)

# Définition des tokens
t_NOT = r'¬'
t_AND = r'∧'
t_OR = r'∨'
t_IMPLIES = r'→'
t_IFF = r'↔'

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

def t_ATOM(t):
    r'[a-zA-Z]+\s*'
    return t

def t_error(t):
    print("Caractère non valide : '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_formula(p):
    '''formula : atom
                | NOT formula
                | formula AND formula
                | formula OR formula
                | formula IMPLIES formula
                | formula IFF formula'''
    if len(p) == 2:  # Single atom
        p[0] = p[1]
    elif len(p) == 3:  # NOT formula
        p[0] = (p[1], p[2])
    else:  # Binary operation
        p[0] = (p[1], p[2], p[3])


def p_atom(p):
    '''atom : ATOM'''
    pass

def p_error(p):
    if p:
        print("Erreur de syntaxe près de '%s'" % p.value)
    else:
        print("Erreur de syntaxe à la fin de l'entrée")

parser = yacc.yacc()

def verify_formula(input_formula):
    lexer.input(input_formula)
    try:
        parsed = parser.parse(input_formula, lexer=lexer)
        corrected_formula = parsed_to_string(parsed)
        return True, corrected_formula
    except:
        return False, ""

def parsed_to_string(parsed):
    if len(parsed) == 1:
        return parsed[0]
    elif len(parsed) == 2:
        if parsed[0] == 'NOT':
            return "¬" + parsed_to_string(parsed[1])
        else:
            return "(" + parsed_to_string(parsed[1]) + ")"
    else:
        operator = parsed[1]
        if operator == 'AND':
            operator = ' ^ '
        elif operator == 'OR':
            operator = ' v '
        elif operator == 'IMPLIES':
            operator = ' -> '
        elif operator == 'IFF':
            operator = ' <-> '
        return "(" + parsed_to_string(parsed[0]) + operator + parsed_to_string(parsed[2]) + ")"

if __name__ == '__main__':
    user_input = input("Entrez une formule propositionnelle : ")
    valid, corrected_formula = verify_formula(user_input)
    if valid:
        print("Formule correcte :", corrected_formula)
    else:
        print("Formule incorrecte")
