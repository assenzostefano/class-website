from flask import Flask, render_template, request, session, jsonify
import requests
import bcrypt
import os

app = Flask(__name__)
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def homepage():
    return render_template('html/index.html')
    #imageList = os.listdir('static/images')
    #imageList = ['images/' + image for image in imageList]
    #return render_template('go.html', imageList=imageList)

@app.route('/orario')
def orario():
    if 'username' in session:
        return "You are logged in as " + session['username']
    #return render_template('html/orario.html')

@app.route('/calendario')
def calendario():
    return render_template('html/calendario.html')

# Da sistemare
@app.route('/api', methods = ['GET', 'POST'])
def api():
    if(request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})
        
if __name__ == '__main__':
   app.run()