import xmlrpc.client as xmlrpclib

from flask import Flask, render_template, request, flash, redirect
from flask_mail import Message, Mail
from contacto import ContactForm
from residencial import ServiceForm

user = 'i.najera@blacom.com.mx'
pwd = 'blacom123..'
dbname = 'develop_blacom'
url = 'http://erp.blacom.com.mx:8089/xmlrpc'

mail = Mail()

app = Flask(__name__)

app.secret_key = 'lolo1639'

app.config['MAIL_SERVER'] = 'smtp.blacom.com.mx'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'no.contestar@blacom.com.mx'
app.config['MAIL_PASSWORD'] = 'K2DLGVcMQhzk'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/cobertura')
def cobertura():
    return render_template('cobertura.html')

@app.route('/comunicaciones')
def comunicaciones():
    return render_template('comunicaciones-unificadas.html')

@app.route('/diseño-de-red')
def diseno():
    return render_template('diseño-de-red.html')

@app.route('/isp')
def isp():
    return render_template('isp.html')

@app.route('/vigilancia-ip')
def vigilancia():
    return render_template('vigilancia-ip.html')

@app.route('/servidores-de-telefonia')
def telefonia():
    return render_template('servidores-de-telefonia.html')

@app.route('/factibilidad')
def factibilidad():
    return render_template('factibilidad.html')

@app.route('/soporte-tecnico')
def soporte():
    return render_template('soporte-tecnico.html')

@app.route('/residencial')
def residencial():
    return render_template('residencial.html')

@app.route('/empresarial')
def empresarial():
    return render_template('empresarial.html')

@app.route('/dedicado')
def dedicado():
    return render_template('dedicado.html')

@app.route('/servicio-residencial', methods=['GET', 'POST'])
def servicioresidencial():
    form = ServiceForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # Si el formulario es válido......
            # Enviar un correo electrónico
            msg = Message('Internet Residencial', sender='no.contestar@blacom.com.mx', recipients=['ivannaje15@icloud.com'])
            msg.html = """
                <h2>
                El Cliente: %s </br>
                Direccion: %s </br>
                Celular: %s </br>
                Ciudad: %s </br>
                Municipio: %s </br>
                Codigo Postal: %s </br>
                Correo: %s </br>
                Mensaje: %s </br>
                Tipo de Plan: %s </br>
                Ancho de banda: %s </br>
                Fecha de Instalación: %s </br>
                </h2>
                """ % (form.nombre.data, form.direccion.data, form.celular.data, form.ciudad.data,
                       form.municipio.data, form.codigo.data, form.correo.data, form.mensaje.data,
                       form.plan.data, form.banda.data, form.fecha.data)
            mail.send(msg)
            # Aquí empieza el guardado de los datos en odoo
            sock = xmlrpclib.ServerProxy(url + '/common')
            uid = sock.login(dbname, user, pwd)
            sock = xmlrpclib.ServerProxy(url + '/object')
            # Aquí tomo los datos del formulario para enviarlos a odoo
            partner_data = {
                'name': form.nombre.data,
                'email': form.correo.data,
                'mobile': form.celular.data,
                'function': "Desde Pagina Web",
                'website': "www.blacom.com.mx",
                'phone': form.celular.data,
                'street_name': form.direccion.data,
                'street_name2': form.ciudad.data,
                'home_reference': form.mensaje.data,
                'comment': "Servicio de internet via web",
                'neightborhood_id': form.codigo.data,
                'ref': form.banda.data
            }
            partner_id = sock.execute(
                dbname, uid, pwd, 'res.partner', 'create', partner_data
            )
            if partner_id:
                # Redirigir a una pagina que muestre un mensaje de éxito
                return render_template('gracias.html')
            else:
                # En caso de error al guardar los datos en odoo
                flash("Hubo un error al guardar los datos. Contacte su administrador")

        else:
            flash('Todos son requeridos.')

        # Finalmente, si no se redirigió al usuario a ningún otro lugar
        # se renderiza el formulario de contacto
    return render_template('servicio-residencial.html', form=form)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()

    if request.method == 'POST':
      if form.validate() == False:
        flash('Todos son requeridos.')
        return render_template('contacto.html', form=form)
      else:
        msg = Message(form.asunto.data, sender='no.contestar@blacom.com.mx', recipients=['ivannaje15@icloud.com'])
        msg.html = """
              <h2>
              El Cliente: %s </br>
              Con el Correo: %s </br>
              Nos manda el Mensaje: %s </br>
              </h2>
              """ % (form.nombre.data, form.correo.data, form.mensaje.data)
        mail.send(msg)

        return render_template('contacto.html', success=True)

    elif request.method == 'GET':
      return render_template('contacto.html', form=form)


app.logger.debug('Mensaje de debug')
app.logger.warning('Una advertencia (%d advertencias)', 55)
app.logger.error('Un error ha ocurrido!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
