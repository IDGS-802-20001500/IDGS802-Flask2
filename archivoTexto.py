
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

f=open("alumnos.txt", "a")
#f.write("\n {}".format(alumno))

for index in alumno.items():
    f.write("\n" + str(index).replace("(",""))
    print(index)

f.close()

