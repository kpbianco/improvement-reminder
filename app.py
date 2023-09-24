import os
from flask import Flask, render_template, url_for

#image_folder = os.path.('static')

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/improvement-image")
def message_handler():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'out.png')
    return render_template("index.html", user_image = full_filename)