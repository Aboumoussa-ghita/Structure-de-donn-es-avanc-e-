def vide(a):
    if len(a) == 0:
        return True
    return False


def val(a):
    if not vide(a):
        return a[0]
    return None


def filsgauche(a):
    if not vide(a) and not vide(a[1]):
        return a[1][0]
    return None


def filsdroit(a):
    if not vide(a) and not vide(a[2]):
        return a[2][0]
    return None


def hauteur(a):
    d = 0
    c = 0
    if vide(a) or (vide(a[1]) and vide(a[2])):
        return 0
    else:
        d = 1 + d
        c = 1 + c
    d = d + hauteur(a[1])
    c = c + hauteur(a[2])
    if c > d:
        d = c
    return d


def isfeuille(a):
    if not vide(a) and vide(a[1]) and vide(a[2]):
        return True
    return False


def nbrnoeuds(a):
    if vide(a):
        return 0
    return 1 + nbrnoeuds(a[2]) + nbrnoeuds(a[1])


def prefix(a):
    if not vide(a):
        print(val(a), end=' ')
        prefix(a[1])
        prefix(a[2])


def infix(a):
    if not vide(a):
        infix(a[1])
        print(val(a), end=' ')
        infix(a[2])


def postfix(a):
    if not vide(a):
        postfix(a[1])
        postfix(a[2])
        print(val(a), end=' ')


def isinterne(a):
    if vide(a):
        return False
    return not isfeuille(a)


def nbr_intern(a):
    n = 0
    if vide(a):
        return 0
    if isinterne(a):
        n = n + 1
    return n + nbr_intern(a[1]) + nbr_intern(a[2])


def existe(x, a):
    if vide(a):
        return False
    if x == val(a):
        return True
    else:
        return existe(x, a[1]) or existe(x, a[2])


def max_ar(a):
    if vide(a):
        return None
    elif isfeuille(a):
        return val(a)
    else:
        if vide(a[2]):
            return max(max_ar(a[1]), val(a))
        elif vide(a[1]):
            return max(max_ar(a[2]), val(a))
        else:
            return max(max_ar(a[1]), max_ar(a[2]), val(a))


def min_ar(a):  
    if vide(a):
        return None
    elif isfeuille(a):
        return val(a)
    else:
        if vide(a[2]):
            return min(min_ar(a[1]), val(a))
        elif vide(a[1]):
            return min(min_ar(a[2]), val(a))
        else:
            return min(min_ar(a[1]), min_ar(a[2]), val(a))


def abr(a):
    if vide(a):
        return True
    if isfeuille(a):
        return True
    else:
        if vide(a[1]):
            return val(a) < min_ar(a[2]) and abr(a[2])
        if vide(a[2]):
            return val(a) > max_ar(a[1]) and abr(a[1])
        else:
            return max_ar(a[1]) <= val(a) < min_ar(a[2]) and abr(a[1]) and abr(a[2])


def existeabr(x, a):
    if vide(a):
        return False
    if x == val(a):
        return True
    elif x < val(a):
        return existeabr(x, a[1])
    else:
        return existeabr(x, a[2])


def max_abr(a):
    if vide(a):
        return None
    elif vide(a[2]):
        return val(a)
    else:
        return max_abr(a[2])


def min_abr(a):
    if vide(a):
        return None
    elif vide(a[1]):
        return val(a)
    else:
        return min_abr(a[1])


def inser_val(x, a):
    if not vide(a) and x < val(a):
        if not vide(a[1]):
            inser_val(x, a[1])
        else:
            a[1] = [x, [], []]
            print(x, " est inséré avec succès!")
    elif not vide(a):
        if not vide(a[2]):
            inser_val(x, a[2])
        else:
            a[2] = [x, [], []]
            print(x, " est inséré avec succès!")
    else:
        a.extend([x, [], []])


def supprimer(x, a):
    if not vide(a):
        if x == val(a):
            if isfeuille(a):
                a = []
            elif vide(a[1]):
                a = a[2]
            elif vide(a[2]):
                a = a[1]
            else:
                a[0] = min_abr(a[2])
                a[2] = supprimer(val(a), a[2])
        elif x < val(a):
            a[1] = supprimer(x, a[1])
        else:
            a[2] = supprimer(x, a[2])
    return a


tree = [3, [15, [0, [], []], [2, [], []]], [4, [], [8, [], []]]]
arb = [15, [5, [3, [], []], [12, [10, [6, [], [7, [], []]], []], [13, [], []]]], [16, [], [20, [18, [], []], [23, [], []]]]]
print("hauteur : ", hauteur(tree))
print("racine : ", val(tree))
print("fils gauche : ", filsgauche(tree))
print("fils droit : ", filsdroit(tree))
print("nobre de noeuds : ", nbrnoeuds(tree))
print("prefixe : ", end='')
prefix(tree)
print("\npostfixe : ", end='')
postfix(tree)
print("\ninfixe : ", end='')
infix(tree)
print("\nis interne ? : ", isinterne(tree))
print("nombre des noeuds internes : ", nbr_intern(tree))
print("1 existe dans tree : ", existe(1, tree))
print("max tree: ", max_ar(tree))
print(tree, "est une abr ? : ", abr(tree))
print(arb, "est une abr ? : ", abr(arb))
print("3 existe dans abr : ", existeabr(9, arb))
print("le max de arb : ", max_abr(arb))
print("le min de arb : ", min_abr(arb))
supprimer(5, arb)
print(arb)
