#quiero hacer un input que pida nombre, telefono y edad y lo guarde en una lista y luego imprimir la lista

users_list =[
    {"nombre": "Pedro", "apellido": "Perez","edad":30, "telefono": "12345678"},
    {"nombre": "Juan", "apellido": "Lopez","edad":28, "telefono": "87654321"},
    {"nombre": "Maria", "apellido": "Gonzalez","edad":25, "telefono": "98765432"},
    {"nombre": "Luis", "apellido": "Ramirez","edad":32, "telefono": "54321678"}
 ]

nombre = input("cuál tu nombre: "),
apellido= input("cuál tu apellido: "),
telefono = input("dime tu telefono: "),
edad = input("que edad tienes: "),

users_list.append({"nombre": nombre,"apellido": apellido, "telefono": telefono, "edad": edad})

for user in users_list:
    print(user)

for user in users_list:
    print(f"{user['nombre']} {user['apellido']} | {user['edad']} | {user['telefono']}")