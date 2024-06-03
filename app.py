import os
import flask
from flask import render_template, request
from flask import jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = flask.Flask(__name__, template_folder='Templates')

"""#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = ''#password
#in my case password is null so i am keeping empty
app.config['MYSQL_DB'] = 'sentiment_analyzer'#database name

mysql = MySQL(app)"""
@app.route('/')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    if flask.request.method == 'GET':
        return(flask.render_template('diagnosis.html'))
    
    
if __name__ == '__main__':
    app.run(debug=True)