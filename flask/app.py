#Importar el framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app = Flask(__name__)

#Configuracion de la conexion a la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='dbflask'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#Declaracion de rutas http://localhost:5000/
@app.route("/")
def index():
    cc = mysql.connection.cursor()
    cc.execute('select * from tbAlbums')
    consultaAlbums = cc.fetchall()
    #print (consultaAlbums)
    return render_template('index.html', lsAlbums = consultaAlbums)

#Declaracion de rutas http://localhost:5000/guardar tipo post
@app.route("/guardar", methods=['POST'])
def guardar():
    if request.method == 'POST':
        #Pasamos a las variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        
        #Conectar nuestra BD y ejecutar el insert

        cs = mysql.connection.cursor()
        cs.execute('insert into tbAlbums (titulo, artista, anio) values (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()

    flash('Los datos se guardaron correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('select * from tbAlbums where id=%s',(id,))
    consultaId = cursorId.fetchall()
    return render_template('editarAlbum.html', album = consultaId)

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varTitulo = request.form['txtTitulo']
        varArtista = request.form['txtArtista']
        varAnio = request.form['txtAnio']
        cursAct = mysql.connection.cursor()
        cursAct.execute('update tbAlbums set titulo=%s,artista=%s,anio=%s where id=%s',(varTitulo,varArtista,varAnio,id))
        mysql.connection.commit()
    flash('Se actualizo el Album: '+varTitulo)
    return redirect(url_for('index'))

#Declaracion de rutas http://localhost:5000/

@app.route('/eliminar/<id>')
def eliminar(id):
    return render_template('eliminar.html', album = id)

@app.route('/borrar/<id>', methods=['POST'])
def borrar(id):
    cursorDel = mysql.connection.cursor()
    cursorDel.execute('DELETE FROM tbAlbums WHERE id=%s', (id,))
    mysql.connection.commit()
    flash('Se eliminó el Álbum con ID: ' + id)
    return redirect(url_for('index'))


#Ejecucion del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)