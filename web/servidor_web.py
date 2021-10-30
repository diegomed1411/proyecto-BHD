from flask import Flask, request, redirect, url_for, render_template
from web.servicios import autenticacion, serv_unidades, serv_reclamos
from flask import session


app= Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods= ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['email'], request.form['clave']):
            error = 'Credenciales inválidas'
        else:
            email = request.form['email']
            session['email']= email
            return redirect(url_for('inicio' , email = email))
    return render_template('login.html', error=error)

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['nombre'], request.form['apellido'], request.form['email'], request.form['Tipo_de_documento'], request.form['numeroDoc'], request.form['telefono'],request.form['clave'],  request.form['idUnidad'], request.form['idInmueble'] ):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)

@app.route('/inicio')
def inicio():
    error = None
    email = request.args['email']
    usuarios = autenticacion.obtener_usuarios()
    unidades = serv_unidades.obtener_unidades()
    reclamos = serv_reclamos.obtener_reclamos()
    if request.method == 'POST':
        serv_reclamos.crear_reclamo()
        return redirect(url_for('inicio'))
    return render_template('inicio.html', usuarios=usuarios, email=email, unidades= unidades, reclamos= reclamos)

app.secret_key='hola'
if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)