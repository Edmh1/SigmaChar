from flask import Flask, request
import lexer
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/analyzeCode', methods=['POST'])
def analyze_code():
    if request.method == 'POST':
        code = request.json['codeInput']
        result, err = lexer.run(code)
        if err:
            errJSON = {}
            errJSON[0]= {
                'error' : err.error_name, 'details' : err.details
            }
            return json.dumps(errJSON)
        else:
            return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
