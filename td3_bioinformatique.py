#Question 1 : 2bits 

#Question 2 : A : 00 , C:01 , G:10 , T:11
    
# Question 3 : fonction qui retourne true si M est prefixe fe S sinn false 
def prefixe(M,S):
    if (len(M)>len(S)):   #1
        return False          #1
    n=len(M)     #1
    for i in range(n):      #n
        
            if M[i] != S[i]:  #1
                return False   #1
    return True   #1
#Question 4 : on a effectué n comparaison elementaire , donc la complexité est n

print(prefixe("ghita", "ghitaaboumoussa"))

#Question 5 : 
    
def list_suffixes(S):
    T=tuple()
    n=len(S)
    for i in range(n):
        T = T + ((S[i:], i),)
    return list(T)
 
L=list_suffixes("ghitaaaaa")
print(L)

#question 6

def tri_liste(L):
    n=len(L)
    for i in range(n):
        for j in range(0,n-i-1):
            if (L[j]>L[j+1]):
                L[j],L[j+1]=L[j+1],L[j]
    return L

L=tri_liste(L)
print(L)

#question 7

def recherche_dichotomique(M,L):    #m et k tailles respectives de M et L
    debut=0      #1 
    fin=len(L)-1     #2
    while debut<fin:      #alpha fois
             milieu=(debut+fin)//2      #3
             if L[milieu][0][:len(M)]==M:    # ♥   #1
                 return L[milieu][1]     #1
             elif L[milieu][0] > M :     #1
                  fin=milieu -1    #2
             else:
                 debut=milieu +1   #2
    return None   #1

print(recherche_dichotomique("aaa", L))

""""question 8 : la complexité de cette algo est :
    C(n)=1+2+alpha(3+1+1+max(1,2,2)+1)=7alpha+4
    avec alpha = log(n)+1
    d'ou C(n)=log(n)"""

#question 9

def est_feuille(R):
    return len(R) == 2 and not R[1]

def feuilles(R):
    l = []
    if est_feuille(R):
        l.append(R[0])
    else:
        for child in R[1]:
            l.extend(feuilles(child))  #pour charger l par les elements obtenus de l'appel de feuille 
    return l

# Example usage
R = ['#', [['A', [[9, []], ['GCTA', [[5, []]]], ['TCTAGCTA', [[1, []]]]]], ['CTA', [[7, []], ['GCTA', [[3, []]]]]], ['GCTA', [[6, []]]], ['T', [['A', [[8, []], ['GCTA', [[4, []]]], ['TCTAGCTA', [[0, []]]]]], ['CTAGCTA', [[2, []]]]]]]]
print(feuilles(R))

#question 10 

def recherche_arbre(M,R):
    l=[]
    for fils in R[1]:
        if fils[1]:
            if prefixe(M,fils[0]):
                l=feuilles(fils)
            elif prefixe(fils[0],M):
                l=recherche_arbre(M[len(fils[1]):],fils)
    return l 

print(recherche_arbre('A', R))

#question 18 : 


def matrice(P, Q):
    p=len(P)
    q=len(Q)
    M = [[0] * q for _ in range(p)]
    for i in range(p):
        for j in range(q):
            if P[i] == Q[j]:
                if i==0 and j==0:
                    M[i][j]=1
                else :
                    M[i][j]=M[i-1][j-1]+1
            else:
                M[i][j]
    return M

M = matrice("GCTAGCATT", "CATTGTAGCT")

for ligne in M:
    print(ligne)
    
#Question 19 : 
def plus_long_mc(P, M):
    len_P = len(P)
    len_Q = len(M[0])

    maxlen = 0
    maxindice = []

    for i in range(len_P):
        for j in range(len_Q):
            if M[i][j] > maxlen:
                maxlen = M[i][j]
                maxindice = [(i, j)]
            elif M[i][j] == maxlen:
                maxindice.append((i, j))

    return maxindice
                   
print(plus_long_mc("GCTAGCATT", M))










