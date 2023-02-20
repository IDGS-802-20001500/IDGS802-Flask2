from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField, PasswordField, validators, DecimalField, IntegerField

class NumForms(Form):
    nums = IntegerField('Numero: ')
    numbers = FieldList(StringField('numero'))