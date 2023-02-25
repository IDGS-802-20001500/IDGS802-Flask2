from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField, PasswordField, validators

def mi_validacion(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError("El campo no tiene datos")


class UserForm(Form):

    matricula = StringField('Matricula',[validators.DataRequired(message="La matricula es requerida")])
    nombre=StringField('Nombre',[validators.DataRequired(message="El campo es requerido"),
                                 validators.length(min=5,max=15, message="Ingresa un valor maximo")])
    apaterno=StringField('Apellido paterno',[mi_validacion])
    amaterno=StringField('Apellido materno')
    email=EmailField('Correo')

class LoginForm(Form):
    username = StringField('usuario',[validators.DataRequired(message="La usuario es requerido")]) 
    password = PasswordField('contraseña',[validators.DataRequired(message="El nombre es requerido"), validators.length(min=5,max=15,message="Ingresa un valor maximo")])