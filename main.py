

from data import people
while True:
    print("oprime 1 para listar todos los usuarios")
    print("oprime 2 para agregar un nuevo usuario")
    print("oprime 3 para modificar un usuario")
    print("oprime 4 para eliminar un usuario")
    print("oprime 5 para salir")

    opcion = int(input("ingrese la opcion que desea realizar: "))
    if opcion==1:
        print(people)
    elif opcion ==2:
        nom = str(input("ingrese el nombre del usuario: "))
        num = input("ingrese el número del usuario: ")
        people[nom] = num
    elif opcion == 3:
        nombre = input("ingrese el nombre del usuario que desea modificar: ")
        if people.get(nombre)== "none":
            print("usuario no encontrado")
        else:
            nuevo = int(input("ingrese el nùmero: "))
            people.update({nombre: nuevo})
        print(people)
    elif opcion == 4:
        people.pop(input())
    else:
        break

        



