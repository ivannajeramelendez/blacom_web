from flask_wtf import Form, validators
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email


class ContactForm(Form):
  nombre = StringField("Nombre Completo", validators=[InputRequired('Porfavor introduce tu nombre')])
  correo = StringField("Correo", validators=[InputRequired('Porfavor introduce tu correo')])
  asunto = StringField("Asunto", validators=[InputRequired('Porfavor introduce tu asunto')])
  mensaje = TextAreaField("Mensaje", validators=[InputRequired('Porfavor introduce tu mensaje')])
  enviar = SubmitField("Enviar")
