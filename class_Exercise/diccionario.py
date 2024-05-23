#crear una lista de usuarios con nombre telefono y edad

users_list =[
    {"nombre": "Pedro", "apellido": "Perez","edad":30, "telefono": "12345678"},
    {"nombre": "Juan", "apellido": "Lopez","edad":28, "telefono": "87654321"},
    {"nombre": "Maria", "apellido": "Gonzalez","edad":25, "telefono": "98765432"},
    {"nombre": "Luis", "apellido": "Ramirez","edad":32, "telefono": "54321678"}
 ]

print(users_list)

print(type(users_list))

print(users_list[1])


users_list.append({"nombre": "Jose", "apellido": "Ramirez","edad":32, "telefono": "54321678"})

print(users_list)

#hacer un programa que muestre por consola los nombres de las listas

for user in users_list:
    print(user["nombre"])

#hacer un programa que muestre por consola la información con un pipeline


for user in users_list:
    print(user["nombre"] , " " , user["apellido"] , " | " , user["edad"] , " | " , user["telefono"])

for user in users_list:
    print(f"{user['nombre']} {user['apellido']} | {user['edad']} | {user['telefono']}")

for user in users_list:
    print (user["edad"])