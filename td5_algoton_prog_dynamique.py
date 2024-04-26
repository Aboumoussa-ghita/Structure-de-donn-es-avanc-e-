 #td5 : algo gloutons et prog dynamique 
objet= {
         "A":(13,700),
         "B":(12,400),
         "C":(8,300), 
         "D":(10,300)
    }
 
def ValeurMassique(objet):
     l=[]
     for ob in objet:
         masse=objet[ob][0]
         prix=objet[ob][1]
         vm=round(prix/masse)
         l.append((vm,masse,prix,ob))
     l.sort(reverse=True)
     return l
     
#print(ValeurMassique(objet))  
    
def SacADos(objet,capacite):
    L=ValeurMassique(objet)
    rslt=[]
    pd=0
    ob=[]
    prix=0
    for i in range(len(L)):
        if pd +L[i][1]<= capacite :
            ob+=L[i][3]
            prix+=L[i][2]
            pd+=L[i][1]

        if pd==capacite : 
            break     #pour optimiser le code        
    rslt.append((ob,'avec un cout de',prix,'euros'))
    return rslt
    
#print(SacADos(objet, 30))

def Rendu(L,N):  #L supposée triée 
    S=[]
    for i in range(len(L)):
        while L[i]<= N:
            S.append(L[i])
            N=N-L[i] 
    if N !=0 : 
        return ("il n'existe pas de solution exacte , la solution proposée est la suivante :", S)
    return S
  
L=[25,10,5,1]
N=87 

L=[31,22,10,2]
N=100 
print(Rendu(L, N))   
    
d={}
def fib2(n):   # la complexité pour cet algo est de n 
    if n==0 or n==1:
        d[n]=n
    elif n not in d :
        d[n]=fib2(n-1)+fib2(n-2)
    return d[n]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            