#%%

idades = [28,42,43 ,35,39, 28,38]
print(idades)
# %%

# %%
# aqui vamos ver um pouco de tamanhos e posições das listas

tamanho = len(teo)
posição = tamanho - 1

exs = teo[posição]

teo[pos][len(exs) -1]

teo[-1] # é o ultimo elemento da lista


#fatiamento de lista 

teo[0:4] # do 0 ao 3 
teo[0:4:2] # do 0 ao 3 de 2 em 2
teo[4][3:5] # da lista 4 os dois ultimos elementos
ou teo[4][-2:] # da lista 4 os dois ultimos elementos

salarios = teo[5]
salarios[::-1] # inverte a lista (do menor para o maior)

#teo[start: stop : step] 
# start = onde começa a lista
# stop = onde termina a lista
# step = de quantos em quantos elementos

idades = [17,32,56,87]
idades.append(18) # adiciona o elemento 18 na lista
print(idades)

media = sum(idades) / len(idades) # soma todos os elementos da lista e divide pelo tamanho da lista
print(media)

minimo = min(idades) # menor elemento da lista
print(minimo)

maximo = max(idades) # maior elemento da lista
print(maximo)

qtde = len(idades) # quantidade de elementos da lista
print(qtde)
