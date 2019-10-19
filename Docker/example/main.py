from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """<p style='display: flex;
                 flex-direction: column;
                 align-items: center;
                 justify-content: center;
                 height: 100vh;
                 font-size: 70px;
                 font-weight: 900;'>¡Hola Mundo!</p>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)