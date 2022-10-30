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
    'voice' : ''
}

def setNotficication(value,type):
    mensaje['value'] = value
    mensaje['type'] = type

@app.route('/')
def main():
    # mensaje['value'] = 'Este mensaje es de prueba'
    # mensaje['type'] = 'danger'
    return render_template('main.html',mensaje=mensaje,partitura=partitura)

@app.route('/handle_data', methods =['POST'])
def handle_data():
    if request.method == 'POST':
        setNotficication('Submit enviado','success')
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