from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Hola mundo desde Flask'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Hola {nombre}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'