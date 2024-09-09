
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
        x = str(input("ingrese el nombre del usuario: "))
        y= input("ingrese el número del usuario: ")
    elif opcion == 3:
        print(people.get(input()))
        people.update(input())
        print(people)
    elif opcion == 4:
        people.pop(input())
    else:
        break

        



