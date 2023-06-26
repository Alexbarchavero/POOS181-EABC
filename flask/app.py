#Importacion del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbflask'
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    return render_template("index.html")

#ruta http://localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        # pasamos a variables el contenido de los input
        vtitulo = request.form['txtTitulo']
        vartista = request.form['txtArtista']
        vanio = request.form['txtAnio']
        
        #print(titulo,artista,anio)
        
        #Conectar y ejecutar el insert
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO tbAlbums(titulo,artista,anio) VALUES(%s,%s,%s)',(vtitulo,vartista,vanio))
        mysql.connection.commit()
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino la BD"

#Ejecucion del servidor en puerto 5000
if __name__ == "__main__":
    app.run(port=5000, debug = True)