#a Composite data type is any data type that comprises primitive data types.

#Comma-separated values (CSV) is a file format that's used to store tabular data, such as data from a spreadsheet. You will work with the CSV file from the following block.

#first define a dictionary that will serve as the composite type for reading tabular data

import csv
import copy

#import csv importa la libreria csv que nos permite trabajar con archivos csv "comma-separated values".
#import copy importa la libreria copy que nos permite hacer copias de diccionarios.

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

#with "with open" syntax statement keeps a file open while you read data. It will automatically close the CSV file when the code inside the "with" block is finished running. Instead of using double quotation marks and .format to pass in the variables, you can use a single quotation mark and write in the variables between the "{}" symbols.

# csv.reader() is a function that you are using from the csv library that you imported with the import csv statement.

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  

#"for row in csvReader:" iterates through each row in the csv file.
#"if lineCount == 0" checks if the first line is the header.
#it it si "print(f'Column names are: {", ".join(row)}')" prints the header. Otherwise, it prints the row. "lineCount += 1" increments the line count.

    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  

#"currentVehicle = copy.deepcopy(myVehicle)" createsa deep copy to storage all the data

        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
#"for myCarProperties in myInventoryList" iterates through each dictionary in the list.

#for key, value in myCarProperties.items()" iterates through each key and value in the dictionary.

    for myCarProperties in myInventoryList:
      for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")

#By default, Python does a shallow copy of complex data types. A shallow copy refers, or points, to the storage location of the myVehicle dictionary variable. Without this line, you would have only one storage box, and only the last item in the list would be copied into memory. This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read.