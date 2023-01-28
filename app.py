from urllib.request import Request, urlopen
from flask import Flask, render_template
import logging
import json
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
    url = "http://127.0.0.1:5000"
    response = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(response).read()
    dict = list(json.loads(webpage))
    number = str(range(0,7))
    day = str(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    return render_template('orario/orario.html', data=dict, number=number, day=day)

@app.route('/calendario')
def calendario():
    logging.info("A user went up: Calendario")
    return render_template('html/calendario.html')
        
if __name__ == '__main__':
   logging.info("Web server started!") 
   app.run(port=4999, debug=True)