from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)             # Active CORS pour permettre les requêtes du front-end

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)