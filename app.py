from flask import Flask, render_template
from flask import request

import forms
import Actividad1_forms

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
    num_form=Actividad1_forms.NumForms(request.form)
    if request.method=="POST":
        num_form.nums.data
    return render_template("Actividad1.html", form=num_form)

app.route("/Respuesta", methods=["GET","POST"])
def Respuesta():
    
    datos = []
    N = request.form.get("N")
    for numbers in N:
        datos.append(numbers)
    
    maximo = max(datos)
    minimo = min(datos)
    promedio = sum(datos)/len(datos)

    print("max = {}, min {}, prom {}".format(maximo,minimo,promedio))



    return render_template("Respuesta.html", maximo=maximo, minimo=minimo, promedio=promedio)


if __name__ =="__main__":
    app.run(debug=True,port=3000)