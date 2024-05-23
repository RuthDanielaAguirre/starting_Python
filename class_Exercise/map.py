#la funcion map permite aplicar una funcion a cada elemento de una lista

numeros = [1,2,3,4,5,6,7,8,9,10]
def cubico(num):
    return num**3

result = map(cubico, numeros)
resultLambda = map(lambda x: x**3, numeros)

print(list(result))
print(list(resultLambda))



#la funcion filter permite aplicar una condicion a cada elemento de una lista

numeros = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x: x>5, numeros)

print(list(result))


#la funcion reduce permite aplicar una condicion a cada elemento de una lista

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]
result = reduce(lambda x,y: x+y, numeros)

print(result)