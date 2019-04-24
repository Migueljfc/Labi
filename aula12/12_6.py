l = ['ECT']
l1 = []
l2 = []

l1.append('ET')  #Adiciona ET à lista l1
l2.append('LEI') #Adiciona LEI à lista l2
l1.append('MEI') #Adiciona MEI à lista l1
l2.append('MSI') #Adiciona MSI à lista l2
print(l)         #Imprime a lista l
print(l1)
print(l1[0])     #Imprime a primeira posição da lista l1 -> ET
print(l2)        #Imprime l2
print(len(l))    #Imprime a dimensão de l -> 1
l.extend(l1)     #Adiciona a lista l1 à lista l
l.extend(l2)     #Adiciona a lista l2 à lista l
print(len(l))    #Imprime a dimensão de l -> 5
print(l)         #Imprime a nova lista l
print(l[0:2])    #Imprime o 1º 2º elemento da lista l
print(sorted(l)) #Vai sortear as posições dos elementos de l