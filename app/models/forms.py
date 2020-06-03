from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class ExtrairForm(FlaskForm):
    link = SelectField("link", choices=[('Escolha o site para ter seus dados extraidos'),('Tecmundo'),('MegaCurioso')],)
