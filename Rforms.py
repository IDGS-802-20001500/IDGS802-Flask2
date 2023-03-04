from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField, PasswordField, validators

class ResistForm(Form):

    banda1 = SelectField("Banda 1", 
    choices=[(0, "Negro"),
             (10, "Cafe"),
             (20, "Rojo"),
             (30, "Naranja"),
             (40, "Amarillo"),
             (50, "Verde"),
             (60, "Azul"),
             (70, "Violeta"),
             (80, "Gris"),
             (90, "Blanco")])

    banda2 = SelectField("Banda 2", 
    choices=[(0, "Negro"),
             (1, "Cafe"),
             (2, "Rojo"),
             (3, "Naranja"),
             (4, "Amarillo"),
             (5, "Verde"),
             (6, "Azul"),
             (7, "Violeta"),
             (8, "Gris"),
             (9, "Blanco")])

    banda3 = SelectField("Banda 3", 
    choices=[(1,"Negro"),
             (10,"Cafe"),
             (100,"Rojo"),
             (1000,"Naranja"),
             (10000, "Amarillo"),
             (100000, "Verde"),
             (1000000, "Azul"),
             (10000000, "Violeta"),
             (100000000, "Gris"),
             (1000000000, "Blanco")])
