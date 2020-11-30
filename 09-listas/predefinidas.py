animales = ["Perro", "Gato", "Lobo", "Conejo"]

numeros = [1, 3, 5, 4, 10, 38, 2]

#Ordenar lista
print("Lista sin ordenar")
print(numeros)
print("\nLista Ordenada")
numeros.sort()
print(numeros)

#Añadir elementos
print("\nAñadir elementos a la lista animales")
animales.append("Tiburon")

animales.insert(1, "Coyote")
print(animales)

#Eliminar elementos de una lista

#Elimina el ultimo elemento
#Se eliminara tiburon
animales.pop()

#Eliminar elemento de una lita pasando el indice como parametro
#Eliminaremos Coyote de la lista
animales.pop(1)
print(animales)

#Podemos eliminar elementos de la lista pasando el elemento como parametro
animales.remove("Gato")
print(animales)
print("_____________________")
#Imprimir una lista de forma inversa
print("Imprimir una lista inversa")
print(numeros)
numeros.reverse()
print(numeros)
print("_____________________")

#Buscar elementos dentro de una lista
print("Verificar si aparece un elemento en una lista")
print('Lobo' in animales)
print("_____________________")

#Contar elementos de una lista
print("Contar elementos de la lista animales")
print(len(animales))
print("_____________________")

#Contar cuantas veces aparece un elemento en una lista
#Agregamos otro elemento a la lista numeros
print("Contar elementos que se repiten en una lista")
numeros.append(5)
print(numeros.count(5))
print("_____________________")

#Conseguir el indice de un elemento en una lista
print("Conseguir indice de elemento Lobo en la lista")
print(animales)
print(animales.index("Lobo"))
print("_____________________")

#Unir listas
#Unir la lista de animales y numeros
print("Unir las listas animales y numeros")
animales.extend(numeros)
print(animales)




