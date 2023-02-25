
#f=open("alumnos.txt","r")
#nombres = f.read()
#print(nombres)


"""nombres2=f.readlines()
print(nombres2)
f.close()

for items in nombres2:
    print(items, end='')"""

alumno={"Matricula": 20001500,
        "Nombre": "Mauricio Israel",
        "Apellidos": "Ferández Ramos",
        "Correo":"20001500@alumnos.utleon.edu.mx"}

#f=open("colores.txt", "a")

"""f.write("\n")
for clave, valor in alumno.items():
    
    f.write("{}: {}\n".format(clave,valor))
    print("{}: {}".format(clave,valor))"""

colores = {}
buscar = "rosa"
encontrado = False

f=open("colores.txt", "r")
for linea in f:
    clave, valor = linea.strip().split(":")
    colores[clave] = valor

for clave, valor in colores.items():
    if valor == buscar:
        print(clave)
        encontrado = True
        break
    if clave == buscar:
        print(valor)
        encontrado = True
        break


if not encontrado:
    print("No se encontró la clave o valor buscado")

f.close()


