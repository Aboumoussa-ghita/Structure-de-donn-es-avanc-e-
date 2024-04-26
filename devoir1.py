#question 1 : creer une tuple a partir d'une liste 
def frequences(L):
    T = tuple()
    for i in range(len(L)):
        cpt = 0
        for j in range(len(L)):
            if L[i] == L[j]:
                cpt = cpt + 1
        if (L[i], cpt) not in T:
            T = T + ((L[i], cpt),)

    return T

L=[12,29,46,29,31,8,12,55,29,8,12,29,31,29,8,29,8,8]
f=frequences(L)
#print(f)

#question 2 : trier la tuple dans l'ordre croissant des occurrences 
"""def tri(F):
    F_list = list(F)  
    for i in range(len(F_list)-1):
        for j in range(0, len(F_list)-i-1):
            if F_list[j][1] > F_list[j+1][1]:
                F_list[j], F_list[j+1] = F_list[j+1], F_list[j]  
    return tuple(F_list)  
"""
#question 2 en utilisant le tri par fusion pour avoir une complexité de nlogn
def tri(F):
    if len(F) > 1:
        middle = len(F) // 2
        leftList = F[:middle]
        rightList = F[middle:]

        tri(leftList)
        tri(rightList)

        leftIndex = rightIndex = mergedIndex = 0

        while leftIndex < len(leftList) and rightIndex < len(rightList):
            if leftList[leftIndex][1] <= rightList[rightIndex][1]:  
                F[mergedIndex] = leftList[leftIndex]
                leftIndex += 1
            else:
                F[mergedIndex] = rightList[rightIndex]
                rightIndex += 1
            mergedIndex += 1

        while leftIndex < len(leftList):
            F[mergedIndex] = leftList[leftIndex]
            leftIndex += 1
            mergedIndex += 1

        while rightIndex < len(rightList):
            F[mergedIndex] = rightList[rightIndex]
            rightIndex += 1
            mergedIndex += 1

    return F
result = tri([(31, 2), (12, 3), (8, 5), (55, 1), (29, 6), (46, 1)])
#print(result)

#Question 3 : inserer un tuple T dans une liste F
def insere(F, T):
    T_list = list(T)
    for i in range(len(F)):
        if F[i][1] > T_list[1]:
            F.insert(i, T_list)
            return F
    F.append(T)
    return F

T=(17,5)
r=insere(result,T)
#print(r)

#Question 4 : creer un arbre de huffman 
def arbre_Huffman(F):
    while( len(F)>1):
        
        tupG=F.pop(0)
        tupD=F.pop(0)
        racine=tupG[1]+tupD[1]
        A=[racine,[tupG[0],[],[]],[tupD[0],[],[]]]
        new_tuple=(A,racine)
        insere(F, new_tuple)
        
    return F   

#print(arbre_Huffman([(31, 2), (12, 3), (8, 5), (55, 1), (29, 6), (46, 1)]))          
       
#Question 5 : ecrire la fonction codes_hiffman pour avoir un dictionnaire 
def codes_huffman(A, code, codesH):
    if A[1] == [] and A[2] == []:
        codesH[A[0]] = code
    else:
        if A[1] != []:
            codes_huffman(A[1], code + "0", codesH)
        if A[2] != []:
            codes_huffman(A[2], code + "1", codesH)
    return codesH

arbre = [18, [7, [46, [], []], []], [11, [5, [31, [], []], []], [29, [], []]]]  

codesHuffman = {}
codesHuffman = codes_huffman(arbre, "", codesHuffman)
print("gg",codesHuffman)

#Question 6 : compresser le dictionnaire en une chaine de caracteres 
def compresse(L,codesH):
    B=""
    for i in range(len(L)):
        for cle, valeur in codesH.items():
            if L[i]==cle:
                B+=valeur 
    return B           
                
dict={55:'1011',8:'01',12:'00',29:'11',46:'1010',31:'100'}
L=[12,29,29,31,8,55,12,46,8,29,12]
#print(compresse(L, dict))
    
#Question 7 : decompresser le string en une liste 
def decompresse(codesH, b):
    result = []
    code = ""
    for i in b:
        code += i
        for cle, valeur in codesH.items():
            if code == valeur:
                result.append(cle)
                code = ""
    return result

dict={55:'1011',8:'01',12:'00',29:'11',46:'1010',31:'100'}
B="0000111110001101100101001110010011"      
        
#print(decompresse(dict, B))        












     