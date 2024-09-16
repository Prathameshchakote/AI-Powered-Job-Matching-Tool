
# AI-Powered Job Matching Tool
================================


## Table of Contents
-----------------

1. [Overview](#overview)
2. [Running the Application Locally](#running-locally)
3. [Running the Application on Cloud using Docker Image in GCP](#running-on-cloud)
4. [Requirements](#requirements)


## Overview
------------

This AI-powered job-matching tool fetches the latest Job using RapidAPI and provides a description and Job application URL. Then users can upload resumes, check how much their resume matches the job requirements, and give the top 5 skills they must have to apply for the job.

## Running Locally
-----------------

To run the application on your local machine, follow these steps:


### Step 1: Clone the Repository

```bash
git clone https://github.com/Prathameshchakote/AI-Powered-Job-Matching-Tool
```

Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Step 3: Configure API Keys
Add your Rapid API key in fetch_jobs.py
Add your OpenAI key in job_analysis.py

Step 4: Run the Application
```bash
python app.py
```

Running on Cloud
------------------
To deploy the application on Google Cloud Platform using Docker, follow these steps:

Step 1: Open google Cloud Shell

Step 2: Clone the Repository
```bash
git clone https://github.com/Prathameshchakote/AI-Powered-Job-Matching-Tool
```

Step 3: Create Docker Image
```bash
gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/gethire
```

Step 4: Deploy to Google Cloud Run using gcloud shell
```bash
gcloud run deploy gethire \
  --image gcr.io/${GOOGLE_CLOUD_PROJECT}/gethire \
  --service-account guestbook@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
  --port 5000 \
  --set-env-vars "RAPIDAPI_KEY=YOUR_RAPIDAPI_KEY,OPENAPI_KEY=YOUR_OPENAPI_KEY"
```

Step 5: Access Your Hosted Application
You will receive a hosted URL for your application.

Requirements
--------------

1. Python
2. pip
3. Rapid API key
4. OpenAI key
5. Google Cloud Platform account (for cloud deployment)

Note: Similarly you can host this this application using docker file on any cloud platform like AWS, Azure
