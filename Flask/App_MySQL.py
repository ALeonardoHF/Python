from flask import Flask, render_template, request, redirect, url_for, flash
#Conexion con XAMPP
#from flask_mysqldb import MySQL

#MySQL XAMPP Connection
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'flaskcontacts'
#mysql = MySQL(app)

app = Flask(__name__)

import pymysql
con = pymysql.connect(host='localhost', user='root', passwd='toor', db='flaskcontacts')
cursor = con.cursor()
# settings, evita errores de flask
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        con.commit()
        flash('Contact Added Successfully')
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_contact(id):
    cursor.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cursor.fetchall()
    return  render_template('edit_contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    cursor.execute("""
    UPDATE contacts
    SET fullname = %s,
        phone = %s,
        email = %s
    WHERE id = %s
    """, (fullname, phone, email, id))
    con.commit()
    flash('Contact Update Successfully')
    return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cursor.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    con.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))

if __name__  == '__main__':
    app.run(port = 3000, debug = True)
