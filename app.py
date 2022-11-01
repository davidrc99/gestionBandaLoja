from flask import Flask, render_template, request, redirect
from function import *

app = Flask(__name__)
app.config['TESTING'] = True

_mensaje = {
    'value' : '',
    'type' : ''
}

_partitura = {
    'type' : '',
    'name' : '',
    'listaVoces' : ''
}

_cola = []

def setNotficication(value,type):
    _mensaje['value'] = value
    _mensaje['type'] = type

@app.route('/')
def main():
    _mensaje = {'value' : '','type' : ''}
    _partitura = {'type' : '','name' : '','listaVoces' : ''}
    return render_template('main.html',mensaje=_mensaje,partitura=_partitura,cola=_cola)

@app.route('/searchSheet', methods =['POST'])
def searchSheet():
    if request.method == 'POST':
        listaVoces = getVoicesOptions(request.form['tipoPartitura'],request.form['nombrePartitura'])
        _partitura = {'type' : '','name' : '','listaVoces' : ''}
        if(listaVoces):
            setNotficication('Partitura encontrada con éxito. Seleccione la voz que desea añadir','success')
            _partitura['type'] = request.form['tipoPartitura']
            _partitura['name'] = request.form['nombrePartitura']
            _partitura['listaVoces'] = listaVoces
        else:
            setNotficication('No se pudo encontrar esa partitura','danger')
    return render_template('main.html',mensaje=_mensaje,partitura=_partitura,cola=_cola)

@app.route('/addVoice', methods =['POST'])
def addVoice():
    if request.method == 'POST':
        voz = getVoice( request.form['tipoPartitura'], request.form['nombrePartitura'],request.form['vozPartitura'])
        _cola.append(voz)
    return render_template('main.html',mensaje=_mensaje,partitura=_partitura,cola=_cola)

# @app.route('/')
# def main():
#     mensaje = ''
#     part = {
#         'name':'',
#         'type':''
#         }
#     return render_template('form.html',part=part,mensaje=mensaje)
# @app.route('/searchData' , methods =['POST'])
# def searchData():
#     mensaje = ''
#     part = {
#             'name':'',
#             'type':''
#             }
#     if request.method == 'POST':
#         part['type'] = request.form['tipoPartitura']
#         part['name'] = request.form['nombrePartitura']
#         listaVoces = getVoicesOptions(part['type'],part['name'])
#         if(listaVoces):
#             mensaje = 'OK'
#         else:
#             mensaje = 'ERROR'
#     return render_template('form.html', part=part,mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug = True)  