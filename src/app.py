from flask import Flask, request
import lexer
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Cambia esta URL por la URL de tu aplicación desplegada
API_URL = 'https://sigmachar.vercel.app/'  

@app.route('/analyzeCode', methods=['POST'])
def analyze_code():
    if request.method == 'POST':
        code = request.json['codeInput']
        response = requests.post(API_URL + '/analyzeCode', json={'codeInput': code})
        if response.status_code == 200:
            return response.json()
        else:
            return json.dumps({'error': 'Error en la solicitud'})

if __name__ == '__main__':
    # Utiliza la URL de tu aplicación si se ejecuta localmente
    app.run(debug=True, host='0.0.0.0', port=5000)
