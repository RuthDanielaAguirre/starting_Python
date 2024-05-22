#a Composite data type is any data type that comprises primitive data types.

#firs define a dictionary that will serve as the composite type for reading tabular data

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#use a "for" loop to iterate through the keys and values of the dictionary.

#for key, value in expresa que sea para cada clave y valor de la expresión.

#myVehicle.items() obtiene todos los pares de clave y valor del diccionario creado.

#print y el uso de corchetes son para crear espacios en blanco que serán rellenados con lo que pides {}

#format(key, value) dice qué valores deben ir en los espacios en blanco {}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))


myInventoryList = []