from crypt import methods
from flask import Flask, render_template, request, redirect
from function import *

app = Flask(__name__)
app.config['TESTING'] = True

mensaje = {
    'value' : '',
    'type' : ''
}

partitura = {
    'type' : '',
    'name' : '',
    'listaVoces' : ''
}

def setNotficication(value,type):
    mensaje['value'] = value
    mensaje['type'] = type

@app.route('/')
def main():
    mensaje = {'value' : '','type' : ''}
    partitura = {'type' : '','name' : '','listaVoces' : ''}
    return render_template('main.html',mensaje=mensaje,partitura=partitura)

@app.route('/handle_data', methods =['POST'])
def handle_data():
    if request.method == 'POST':
        listaVoces = getVoicesOptions(request.form['tipoPartitura'],request.form['nombrePartitura'])
        if(listaVoces):
            setNotficication('Partitura encontrada con éxito. Seleccione la voz que desea añadir','success')
            partitura['type'] = request.form['tipoPartitura']
            partitura['name'] = request.form['nombrePartitura']
            partitura['listaVoces'] = listaVoces
        else:
            setNotficication('No se pudo encontrar esa partitura','danger')
    return render_template('main.html',mensaje=mensaje,partitura=partitura)
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