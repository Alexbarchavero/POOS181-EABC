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

if __name__ == "__main__":
    app.run(port=5000, debug=True)