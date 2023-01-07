from flask import Flask, render_template, request, session, jsonify
import requests
import logging
import bcrypt
import sys
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("src/log/all.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

app = Flask(__name__)
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def homepage():
    logging.info("A user went up: Homepage")
    return render_template('html/index.html')
    #imageList = os.listdir('static/images')
    #imageList = ['images/' + image for image in imageList]
    #return render_template('go.html', imageList=imageList)

@app.route('/orario')
def orario():
    logging.info("A user went up: Orario")
    if 'username' in session:
        return "You are logged in as " + session['username']
    #return render_template('html/orario.html')

@app.route('/calendario')
def calendario():
    logging.info("A user went up: Calendario")
    return render_template('html/calendario.html')

# Da sistemare
@app.route('/api', methods = ['GET', 'POST'])
def api():
    logging.info("A user went up: API")
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})
        
if __name__ == '__main__':
   logging.info("Web server started!") 
   app.run()