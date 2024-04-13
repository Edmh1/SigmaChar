from flask import Flask, request, jsonify
import lexer
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def analyze_code():
    if request.method == 'POST':
        code = request.json
        result, err = lexer.run(code)
        if err:
            return jsonify(error=err), 400
        else:
            return jsonify(result=result), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
