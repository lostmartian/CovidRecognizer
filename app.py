from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import numpy as np
import glob as glob


UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = set(['nii'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
   return render_template('index.html')

@app.route('/index.html')
def index():
   return render_template('index.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'ctscan.nii'))

	lungmodel = load_model('models/lung_model.hdf5')

	



if __name__ == '__main__':
	app.run(debug = True)
