import numpy as np

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def reconstruire_chemin(pred, dep, arr): # pred dict
    actuel = arr   
    chemin = [actuel]
    while actuel != dep:  # tq on est pas arrivé au dep
        actuel = pred[actuel]   #on recup le noeud precedent de actuel
        chemin = [actuel] + chemin  #le preced est ajouté au debut de chemin
    return chemin

def AEtoile(Graphe, dep, arr):
    #Affectation des coûts inf à tous les sommets à l'exception de "dep"
    G, pred = {}, {}
    for noeud in Graphe:
        G[noeud] = np.inf #dictionnaire de stockage des coûts d'accès aux nœuds(distance déjà parcourue)
        pred[noeud] = -1  #dictionnaire de stockage des prédécesseurs de chaque noeud , -1 indique pas encore été visités ou  pas de prédécesseur connu

    G[dep] = 0 # coup pour noeud de dep 0
    file_priorite = [(0, dep)]

    while file_priorite: #file non vide
        # Trouver le nœud avec le coût le plus faible dans la liste non triée
        cout_actuel, noeud_actuel = min(file_priorite)
        file_priorite.remove((cout_actuel, noeud_actuel))

        if noeud_actuel == arr:
            break

        for voisin in Graphe[noeud_actuel]:
            cout_voisin = G[noeud_actuel] + distance(noeud_actuel, voisin)

            if cout_voisin < G[voisin]:
                pred[voisin] = noeud_actuel
                G[voisin] = cout_voisin
                cout_heuristique = cout_voisin + heuristic(voisin, arr)
                file_priorite.append((cout_heuristique, voisin))

    return G[arr], reconstruire_chemin(pred, dep, arr)


Graphe={
(0,0):[(0,1),(1,0)], (0,1):[(0,0),(0,2),(1,1)],
(0,2):[(0,1),(0,3),(1,2)], (0,3):[(0,2)], (1,0):[(0,0),(2,0),(1,1)],
(1,1):[(1,0),(0,1),(1,2)], (1,2):[(0,2),(1,1),(2,2)], (2,0):[(1,0),(3,0)],
(2,2):[(1,2),(3,2)], (3,0):[(2,0),(4,0),(3,1)], (3,1):[(3,0),(3,2)],
(3,2): [(3,1),(3,3),(2,2),(4,2)], (3,3):[(3,2),(4,3)], (4,0):[(3,0)],
(4,2): [(3,2),(4,3)], (4,3):[(4,2),(3,3)]
}
dep = (0, 0)
arr = (3, 1)

print(AEtoile(Graphe, dep, arr))

dep = (0, 0)
arr = (4,3)

print(AEtoile(Graphe, dep, arr))