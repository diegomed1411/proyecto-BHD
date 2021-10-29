from flask import Flask, request, redirect, url_for, render_template
from web.servicios import autenticacion
from flask import session
from datos.modelos.usuarioResidente import obtener_usuarios_por_email_clave


app= Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

usuario = []
def obtenerDatosUsuario(email, clave):
    return usuario.append(obtener_usuarios_por_email_clave(email, clave))


@app.route('/login', methods= ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['email'], request.form['clave']):
            error = 'Credenciales inválidas'
        else:
            session['email']= request.form['email']
            session['clave']= request.form['clave']
            #return redirect(url_for('inicio' , encabezado = session['email']))
            datos = obtenerDatosUsuario(session['email'], session['clave'])
            return render_template('inicio.html', encabezado = datos)
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
    usuarios = autenticacion.obtener_usuarios()
    return render_template('inicio.html', usuarios=usuarios)

app.secret_key='hola'
if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)