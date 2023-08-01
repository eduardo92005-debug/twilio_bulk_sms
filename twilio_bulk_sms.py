from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route('/message', methods=['GET','POST'])
def message_controller():
    return render_template('index.html')


@app.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')

app.run()