# Back-End Python básico #

from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)    # allow Front-End JavaScript get to API

@app.route('/')
def home():
    return jsonify({"status": "API do Condomínio rodando com sucesso!"})

# Inicial route of garden's calendar
@app.route('/api/jardinagem', methods=['GET'])
def get_jardinagem():
    eventos = [
        {"id": 1, "atividade": "Poda das árvores e arbustos", "data", "2026-08-20", "status": "Agendado"};
        {"id": 2, "Adubação do jardim frontal": "data", "2026-08-20", "status": "Agendado"}
    ]
    return jsonify(eventos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)