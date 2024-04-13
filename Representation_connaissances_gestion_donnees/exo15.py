

def and_verite(f1, f2):
    verite = []
    if len(f1) == len(f2):
        for verite1, verite2 in zip(f1, f2):
            if verite1 and verite2:
                verite.append(1)
            else:
                verite.append(0)
    return verite

def or_verite(f1, f2):
    verite = []
    if len(f1) == len(f2):
        for verite1, verite2 in zip(f1, f2):
            if verite1 or verite2:
                verite.append(1)
            else:
                verite.append(0)
    return verite

def implies_verite(f1, f2):
    verite = []
    if len(f1) == len(f2):
        for verite1, verite2 in zip(f1, f2):
            if verite1 == 1 and verite2 == 1:
                verite.append(1)
            elif verite1 == 0 and verite2 == 0:
                verite.append(1)
            else:
                verite.append(0)
    return verite

def test(f1, f2):
    for v1, v2 in zip(f1, f2):
        print(v1, v2)

# test([0, 1, 1, 1], [1, 0, 0, 0])


def ensemble_verite(formulaire):
    form = []
    form_verite = []
    print(formulaire)
    for val in formulaire:
        if val[0] == 'AND':
            form_verite = [0, 0, 0, 1]
        if val[0] == 'OR':
            form_verite = [0, 1, 1, 1]
        if val[0] == 'IMPLIES':
            form_verite = [1, 0, 1, 1]
        if val[0] == 'IFF':
            form_verite = [1, 0, 0, 1]
    return form_verite

p = [['ATOM', 'a'], ['AND', 'and'], ['ATOM', 'b'], ['IMPLIES', '→'] , ['ATOM', 'b'], ['OR', 'or'], ['ATOM', 'a']]

formule_and = [['ATOM', 'a'], ['AND', 'and'], ['ATOM', 'b']]

ensemble_test = ensemble_verite(p)

print('ENSEMBLE TEST', ensemble_test)

print(implies_verite([0, 0, 1, 1], [0, 1, 0, 1]))