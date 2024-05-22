#Python allows you to store different data types in a list.

myMixedTypeList = ["Hello", 100, 23.2, True, "World"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))


#usamos {} como marcadores de posición que se rellenaran con los valores de la lista y lo pedido.

#con format(item, type(item)) dice qué valores deben ir en los espacios en blanco {}

#item es el valor de la lista 
#type(item) es el tipo de dato de la lista