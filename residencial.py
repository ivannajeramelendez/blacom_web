from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateTimeField
from wtforms.validators import InputRequired


class ServiceForm(Form):
  nombre = StringField("Nombre Completo", validators=[InputRequired('Porfavor introduce tu nombre')])
  correo = StringField("Correo Electronico", validators=[InputRequired('Porfavor introduce tu correo')])
  direccion = StringField("Direccion", validators=[InputRequired('Porfavor introduce tu Direccion')])
  celular = StringField("Celular", validators=[InputRequired('Porfavor introduce tu celular')])
  ciudad = SelectField("Ciudad", choices=[('puebla', 'Puebla'), ('tlaxcala', 'Tlaxcala')])
  municipio = StringField("Municipio", validators=[InputRequired('Porfavor introduce tu municipio')])
  codigo = StringField("Codigo Postal", validators=[InputRequired('Porfavor introduce tu C.P')])
  plan = SelectField("Tipo de Plan", choices=[('mensual', 'Mensual'), ('semestral', 'Semestral'), ('anual', 'Anual')])
  banda = SelectField("Ancho de Banda", choices=[('hasta 2 Mbps', 'Hasta 2 Mbps'), ('hasta 3 Mbps', 'Hasta 3 Mbps'), ('hasta 5 Mbps', 'Hasta 5 Mbps'), ('hasta 10 Mbps', 'Hasta 10 Mbps')])
  fecha = DateTimeField('¿Cuando es la instalación? Mes/Dia/Año', format='%m/%d/%y', validators=[InputRequired('Porfavor introduce una fecha')])
  mensaje = TextAreaField("Algun Mensaje:", validators=[InputRequired('Porfavor introduce tu mensaje')])
  enviar = SubmitField("Enviar")