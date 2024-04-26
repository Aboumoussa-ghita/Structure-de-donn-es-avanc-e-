# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:49:20 2023

@author: msssg
"""
import numpy as np

#exercice 1 :
#question 2
def MatAdj(S,A):
    M=[ [0] * len(S) for _ in range(len(S))]
    for x,y in A:
        M[x][y]=1
        M[y][x]=1
    return M

S=[0,1,2,3,4,5,6]
A=[(0,1),(0,2),(1,2),(1,5),(2,3),(3,6),(4,6),(5,6)]

G=MatAdj(S, A)

for ligne in G:
    print(ligne)
    
#question 3
def degree(s,M):
    count=0
    for elmnt in M[s]:
        if elmnt !=0:
            count+=1
    return count

print(degree(1, G))
    
#question 4 : le graphe est eulerien
def estEulerien(G):
    for i in range(len(G)):
        d=degree(i, G)
        if d==0 or d%2==1:
            return False
        return True

print(estEulerien(A))

#exercice 3
#quesrion 1 : parcours en largeur 
def SuccesseurNonVisite(G,s,visite):
    voisin=[]
    for x in range(len(G[s])):
        if G[s][x]!=0 and x not in visite:
            voisin+=[x]
    return voisin

def ParcLargeur(G,depart):
    f=[depart]
    R=[]
    while len(f)!=0:
        s=f.pop(0)
        R.append(s)
        succ=SuccesseurNonVisite(G, s, R+f)
        f.extend(succ)
    return R

print(ParcLargeur(G, 0))

#question 2: parcours en profondeur 
def ParcProfondeur(G,depart):
    P=[depart]
    r=[]
    while len(P)!=0:
        s=P[-1]
        suc=SuccesseurNonVisite(G, s, P+r)
        if len(suc)!=0:
            P.append(suc[0])
        else :
            r=[P.pop(-1)]+r    #on a ajouter l'element de p avant r pour ne pas renverser la liste r 
    return r

print(ParcProfondeur(G, 0))

#exo 4
#algo de dijkstra
def IndiceMinDistance(D,NnMarque):
    pmin=NnMarque[0]
    for i in NnMarque[1:]:
        if D[i]<D[pmin]:
            pmin=i
    return pmin

def SuccesseurNonMarques(G,s,NnMarque):  # g est la matrice 
    voisin=[]
    for x in NnMarque:
        if G[s][x]!=np.inf: # on cherche a partir des colonnes 
            voisin.append(x)
    return voisin

def dijkstra(G,dep,arr):
    n=len(G) #nbre de sommets
    D=[np.inf]*n
    D[dep]=0
    pred=[dep]*n
    NnMarque=list(range(n))  #[0,1,2,3,4,5,6]
    while arr in NnMarque  :
        m=IndiceMinDistance(D, NnMarque)
        NnMarque.remove(m)  #marquer le sommet m
        sv=SuccesseurNonMarques(G,m,NnMarque)
        for k in sv: 
            if D[k]>D[m]+G[m][k]:
                D[k]=D[m]+G[m][k]
                pred[k]=m
        if arr not in NnMarque :
            break 
    return D , pred
# le prob de ce code est que le cas ou on atteint pas l'arrive , on reste dans une boucle infini

def PredecesseursG(G,s):
    pred=[]
    for i in range(len(G)):
        if G[i][s]!=np.inf :  # on cherche a partir des lignes 
            pred.append(i)
    return pred 

def bellman_ford(G,dep):
    n=len(G) #nbre de sommets
    D=np.zeros(n,n)+np.inf
    #D[:,0]=0 toute les lignes de la colonne zero recoit zero
    D[:,dep]=0
    P=[dep]*n
    for lg in range (1,n):
        for s in range(n):   # sommet à traiter
            Pr=PredecesseursG(G, s)  #liste des predecesseurs de s
            for p in Pr :#p est in predecesseur de s
                if D[lg-1,P]!=np.inf:
                    if D[lg-1,p]+G[p,s]<D[lg-1,s]:
                        D[lg,s]=D[lg-1,p]+G[p,s]
                        P[s]=p
                    
    #iteration de verif 
    for s in range(n): 
        pr=PredecesseursG(G,s)
        for p in pr : 
            if D[n-1,p]!=np.inf:
                if D[n-1,p]+G[p,s]<D[n-1,s]:
                    return "pas de solution , il existe un circuit absorbant !"
    return D[n-1],P
        

G=[[np.inf , 1 , 7],
   [1 , np.inf , 9],
   [7 ,9 ,np.inf]]

def floydWarshall(G):
    g=G.copy()
    n=len(g)
    for i in range(n):
        g[i][i]=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                g[i][j]=min(g[i][j],g[i][k]+g[k][j])
    return g 

print(floydWarshall(G))



























