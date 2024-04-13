from ply import lex, yacc

tokens = (
    'ATOM',
    'AND',
    'THEN',
    'IFF',
    'NOT',
    'OR',
)

t_ATOM = r'\b(?!(?:not|and|or|if|iff|then)\b)[a-zA-Z]+\b'
t_AND = r'and'
t_THEN = r'then'
t_IFF = r'iff'
t_NOT = r'not'
t_OR = r'or'

# A rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'THEN'),
    ('left', 'AND'),
    ('left', 'IFF'),
    ('left', 'OR'),
    ('left', 'NOT'),
)

def p_expression_atom(p):
    'expression : ATOM'
    p[0] = p[1]

def p_expression_and(p):
    'expression : expression AND expression'
    p[0] = f"{p[1]} ∧ {p[3]}"

def p_expression_then(p):
    'expression : expression THEN expression'
    p[0] = f"{p[1]} -> {p[3]}"

def p_expression_iff(p):
    'expression : expression IFF expression'
    p[0] = f"{p[1]} <-> {p[3]}"

def p_expression_or(p):
    'expression : expression OR expression'
    p[0] = f"{p[1]} v {p[3]}"

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = f"¬ {p[2]}"

err_detected = False

def p_error(p):
    global err_detected
    # print(f"Syntax error at '{p}'")
    err_detected = True

parser = yacc.yacc()

def parse(input):
    global err_detected
    err_detected = False
    result = parser.parse(input)
    if not err_detected and result:
        print(f"Votre formule est correcte: {result}")
        return True
    else:
        print("La formule n'est pas correcte.")
        return False

# Test
if __name__ == '__main__':
    user_input = input("Entrez une formule propositionnelle : ")
    # code = "a and b then c"
    valid = parse(user_input)
    # print("valid : ", valid)
    if not valid:
        print("Votre Formule de merde : ", user_input)
