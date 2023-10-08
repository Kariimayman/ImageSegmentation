from flask import Flask, render_template
from flask import send_file
from flask import request
from flask_cors import CORS
from main import predictUsingModel

app = Flask(__name__)
CORS(app)
from flask import Response


@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()


app.config['UPLOAD_FOLDER'] = "/"
img = ""


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        name = f.filename
        f.save(name)
        return "Success "


@app.route('/photo/<name>')
def get_current_time(name):
    predictUsingModel(name)
    return send_file(name)


if __name__ == '__main__':
    app.run(debug=True)
