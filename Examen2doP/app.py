from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='db_floreria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/consultayedicion')
def cons_edit():
    return render_template('cons_edit.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'post':
        g_nombre = request.form['g_nombre']
        g_cantidad = request.form['g_cantidad']
        g_precio = request.form['g_precio']
        
        cursor1 = mysql.connection.cursor()
        cursor1.execute('insert into tbFlores(nombre,cantidad,precio) values(%s,%s,%s)',(g_nombre,g_cantidad,g_precio))
        mysql.connection.commit()
    return render_template('mensaje.html')

@app.route('/consultar/<id>',methods=['POST'])
def consultar(id):
    if request.method == 'post':
        cursor2 = mysql.connection.cursor()
        cursor2.execute('select * from tbFlores where nombre = %s',(id,))
        consulta = cursor2.fetchone()
        return render_template('cons_edit.html', flor = consulta)

@app.route('/editar')
def editar(nombre):
    cursor4 = mysql.connection.cursor()
    cursor4.execute('select * from tbFlores where nombre=%s',(nombre,))
    connombre = cursor4.fetchone()
    return render_template('editarAlbum.html', flor = connombre)

@app.route('/actualizar<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        e_nombre = request.form['e_nombre']
        e_cantidad = request.form['e_cantidad']
        e_precio = request.form['e_precio']
        cursor3 = mysql.connection.cursor()
        cursor3.execute('update tbFlores set nombre=%s,cantidad=%s,precio=%s where id=%s',(e_nombre, e_cantidad, e_precio, id))
        mysql.connection.commit()
    flash('Se actualizo la flor: '+e_nombre)
    return redirect(url_for('consultayedicion'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)