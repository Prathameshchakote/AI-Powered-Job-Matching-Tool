from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import os
from fetch_jobs import get_jobs, allowed_file
from job_analysis import upload_file

# Configuration for file upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
jobs_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'job_title' in request.form:
            job_title = request.form['job_title']
            jobs = get_jobs(job_title)
            jobs_list = jobs
            return render_template('index.html', jobs=jobs)
    return render_template('index.html', jobs=[])

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    return upload_file()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
