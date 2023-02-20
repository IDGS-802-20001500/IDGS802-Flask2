from flask import Flask, render_template
from flask import request

import forms
from Actividad1_forms import NumForms

app=Flask(__name__)

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET","POST"])
def Alumno():
    alum_form=forms.UserForm(request.form)
    if request.method=="POST":
        mat=alum_form.matricula.data
        nom=alum_form.nombre.data
        #alum_form.apaterno.data
        #alum_form.amaterno.data
        #alum_form.email.data

    return render_template("Alumnos.html", form=alum_form, mat=mat, nom=nom)

@app.route("/Numeros", methods=["GET","POST"])
def Numeros():

    

    if request.method =="GET":
        num_form= NumForms()
        return render_template("Actividad1.html", form=num_form)
    else:
        num_form= NumForms(request.form)
        return render_template("Actividad1.html", form=num_form)
    
    

@app.route("/Respuesta", methods=["POST"])
def Respuesta():
    nums_form = NumForms(request.form)
    listaN = []

    for numero in request.form.getlist("numbers"):
        listaN.append(int(numero))

    maxi = max(listaN)
    mini = min(listaN)
    prom = sum(listaN)/len(listaN)

    
    def repetir(lista):
        contador = {}
        for numer in lista:
            if numer in contador:
                contador[numer] += 1
            else:
                contador[numer] = 1
            repetidos = {}
        for index in contador:
            if contador[index] > 1:
                repetidos[index] = contador[index]
        return repetidos
        
    repit = repetir(listaN)
    
    return render_template("Respuesta.html", maximo=maxi, minimo=mini, promedio=prom,repetidos = repit)


if __name__ =="__main__":
    app.run(debug=True,port=3000)