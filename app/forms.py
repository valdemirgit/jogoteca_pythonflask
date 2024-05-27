from wtforms.fields import (BooleanField, PasswordField, StringField,SubmitField)
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm,validators
from wtforms.fields import EmailField

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
    ])
    submit = SubmitField("Cadastrar")