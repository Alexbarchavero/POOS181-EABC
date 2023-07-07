from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='DB_Fruteria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/guardar", methods=['POST'])
def guardar():
    if request.method == 'POST':
        vfruta = request.form['txtfruta']
        vseason = request.form['txtseason']
        vprecio = request.form['txtprecio']
        vstock = request.form['txtstock']
        
        cs = mysql.connection.cursor()
        cs.execute('insert into tbFrutas (fruta,temporada,precio,stock) values (%s, %s, %s, %s)', (vfruta,vseason,vprecio,vstock))
        mysql.connection.commit()
    flash('Los datos se guardaron correctamente')
    return render_template("ingresar.html")

@app.route('/editar/<id>')
def editar(id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('select * from tbFrutas where id=%s',(id,))
    consultaId = cursorId.fetchone()
    return render_template('editarAll.html', fruta = consultaId)

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varfruta = request.form['txtfruta']
        varseason = request.form['txttemporada']
        varprecio = request.form['txtprecio']
        varstock = request.form['txtstock']
        
        cursAct = mysql.connection.cursor()
        cursAct.execute('update tbFrutas set fruta=%s,temporada=%s,precio=%s,stock=%s where id=%s',(varfruta,varseason,varprecio,varprecio,id))
        
        mysql.connection.commit()
        
    flash('Se actualizo la fruta: '+varfruta)
    return render_template('consultarAll.html')


