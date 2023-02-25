from flask import Flask, render_template
from flask import request

import forms
from Actividad1_forms import NumForms
from forms2 import ColorForm
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import make_response

app=Flask(__name__)
app.config['SECRET_KEY'] = "Esta es una clave encriptada"
csrf = CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template("404.html"),404

@app.before_request
def before_request():
    print("numero1")

@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    reg_user=forms.LoginForm(request.form)
    datos =""
    
    if request.method == "POST" and reg_user.validate():
        user=reg_user.username.data
        passw=reg_user.password.data
        datos=user+'@'+passw
        succes_message="Bienvenido {}".format(user)
        flash(succes_message)

    response=make_response(render_template("cookies.html",form=reg_user))
    response.set_cookie("datos_user",datos)
    return response

@app.after_request
def after_request(response):
    print("numero3")
    return response

@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get("datos_user")
    nombre = valor_cookie.split("@")
    return render_template("saludo.html", nom = nombre[0])
        

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET","POST"])
def Alumno():
    alum_form=forms.UserForm(request.form)
    mat = ""
    nom = ""
    if request.method=="POST" and alum_form.validate():
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

@app.route("/colores", methods = ["GET", "POST"])
def colores():
    speak_form = ColorForm(request.form)
    cing = ""
    cesp = ""
    cdicc = {}

    if request.method=="POST":

        cing = speak_form.ingles.data
        cesp = speak_form.espanol.data
        print(cesp)
        print(cing)

        cdicc = {cing:cesp}
        print(cdicc)

        with open("colores.txt", "a") as f:
            for clave, valor in cdicc.items():
                f.write("{}:{}\n".format(clave,valor))
        
        
    return render_template("Actividad2.html", form=speak_form)


@app.route("/colores2", methods = ["GET", "POST"])
def traduccion():
    speak_form = ColorForm(request.form)

    color = ""
    colores = {}
    encontrado = False

    if request.method=="POST":
        color = speak_form.color.data

        with open("colores.txt", "r") as f:
            for linea in f:
                clave, valor = linea.strip().split(":")
                colores[clave] = valor
                
           

        if request.form.get("idioma") == "ingles":
            for clave, valor in colores.items():
                if valor == color:
                    print(clave)
                    encontrado = True
                    return render_template("Actividad2.html", form=speak_form, color=clave)
                
            return
        if request.form.get("idioma") == "espanol":
            for clave, valor in colores.items():
                if clave == color:
                    print(valor)
                    encontrado = True
                    return render_template("Actividad2.html", form=speak_form, color=valor)
                
        if not encontrado:
                    return render_template("Actividad2.html", form=speak_form, color="No hay")




if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)