from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField, PasswordField, validators


class UserForm(Form):

    matricula = StringField('Matricula',[validators.DataRequired(message="La matricula es requerida")])
    nombre=StringField('Nombre',[validators.DataRequired(message="El campo es requerido"),
                                 validators.length(min=5,max=15, message="Ingresa un valor maximo")])
    apaterno=StringField('Apellido paterno')
    amaterno=StringField('Apellido materno')
    email=EmailField('Correo')
