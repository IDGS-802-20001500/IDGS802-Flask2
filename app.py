from flask import Flask, render_template
from flask import request

import forms
from Actividad1_forms import NumForms
from forms2 import ColorForm
from Rforms import ResistForm
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import make_response
from resistencias import ColoresResistencia

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

        cdicc = {cing.lower():cesp.lower()}
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
                colores[clave.lower()] = valor.lower()
                
           

        if request.form.get("idioma") == "ingles":
            for clave, valor in colores.items():
                if valor == color.lower():
                    print(clave)
                    encontrado = True
                    return render_template("Actividad2.html", form=speak_form, color=clave)
            if not encontrado:
                    return render_template("Actividad2.html", form=speak_form, color="No hay")
                
            return
        if request.form.get("idioma") == "espanol":
            for clave, valor in colores.items():
                if clave == color.lower():
                    print(valor)
                    encontrado = True
                    return render_template("Actividad2.html", form=speak_form, color=valor)
            if not encontrado:
                return render_template("Actividad2.html", form=speak_form, color="No hay")
            
@app.route("/resistencia", methods=["GET","POST"])
def resistencia():

    rforms = ResistForm()
    valor_cookie=request.cookies.get("datos_user")
    nombre = valor_cookie.split("@")
    b1 = 0
    b2 = 0
    b3 = 0
    tol = 0
    cb1 = " "
    cb2 = " "
    cb3 = " "
    ctol = " "
    valor = 0 
    max = 0 
    mini = 0
    backg1 = " "
    backg2 = " "
    backg3 = " "
    backg4 = " "

    textco1 = " "
    textco2 = " "
    textco3 = " "
    
    

    if request.method=="POST" and nombre != None:
       b1 = int(request.form["banda1"])
       b2 = int(request.form["banda2"])
       b3 = int(request.form["banda3"])
       tol = float(request.form.get("rbtnTol"))

       print("banda 1: {}, banda 2: {}, banda 3: {}, tol: {}".format(b1,b2,b3, tol))

       print("min: {}, ohms: {}, max: {}".format((((b1+b2)*b3)*(tol+1)),((b1+b2)*b3),(((b1+b2)*b3)-(((b1+b2)*b3)*tol))))

       valor = (b1+b2)*b3
       max = ((b1+b2)*b3)*(tol+1)
       mini = ((b1+b2)*b3)-(((b1+b2)*b3)*tol)
       

       colors = ColoresResistencia(b1, b2, b3, tol)    
       cb1 = colors.banda1()
       cb2 = colors.banda2()
       cb3 = colors.banda3()
       ctol = colors.tolerancia()

       backg1 = colors.color1()
       backg2 = colors.color2()
       backg3 = colors.color3()
       backg4 = colors.color4()

       #textco1 = colors.text1()
       #textco2 = colors.text2()
       #textco3 = colors.text3()

       print("{}, {}, {}, {}".format(cb1,cb2,cb3,ctol))

       

    return render_template("Resistencias.html", form=rforms, banda_1=cb1, banda_2=cb2, banda_3=cb3, tolerancia=ctol, valor=valor, mini=mini, max=max, nom=nombre[0], bgc1=backg1, bgc2=backg2, bgc3=backg3,
                           bgc4=backg4)
                
        

if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)