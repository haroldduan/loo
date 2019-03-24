# -*- coding: utf-8 -*-
# Copyright 2019, AVATech
#
# Author Harold.Duan
# This module is REST API service implements.

import sys
print(sys.path)
from flask import Flask,render_template
import face_recognition,face_recognition_models

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/FR')
def face_recognition_test():
    
    pass