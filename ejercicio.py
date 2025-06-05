lista_de_notas = []
while True:
    try:
        user =int(input(" Ingrese 1 para agregar notas: \n Presione cualquier tecla para salir: "))
        if user == 1:
            while True:
                try:
                    nota = int(input("Ingrese la nota o ingrese 0 para salir: "))
                    if nota == 0:
                        break
                    else:
                        lista_de_notas.append(nota)
                        print(f"Las notas cargadas al sistema son: {lista_de_notas}")
                        print(f"La cantidad de notas es: {len(lista_de_notas)}")
                        print(f"El promedio de las notas es {sum(lista_de_notas)/len(lista_de_notas)}")
                except ValueError:
                    print("Solo ingrese numeros")
                    continue
    except ValueError:
        print("¡Adios!")
        break
