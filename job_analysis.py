import os
from flask import redirect, render_template, request
import PyPDF2
from openai import OpenAI
import openai
from fetch_jobs import allowed_file

def upload_file():
    if 'resume' not in request.files:
        return "No file part"

    resume_file = request.files['resume']
    job_description = request.form['job_description']
    job_title = request.form['job_title']
    job_state = request.form['job_state']
    job_city = request.form['job_city']
    employer_name = request.form['employer_name']
    job_apply_link = request.form['job_apply_link']
    if resume_file.filename == '':
        return "No selected file"

    if resume_file.filename == '' or not allowed_file(resume_file.filename):
        return redirect(request.url)

    try:
        resume_text = extract_text_from_pdf(resume_file)
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

    match_percentage = calculate_match(job_description, resume_text)
    
    return render_template('resume_analysis.html', match_percentage=match_percentage, job_description=job_description, job_state=job_state, job_title=job_title, job_city=job_city, employer_name=employer_name, job_apply_link=job_apply_link)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

def calculate_match(job_description, resume_text):
    prompt = f"Job Description: {job_description}\n\nResume: {resume_text}\n\nWhat are top 5 techical Skills required to apply givn job description and What percentage does this resume match the job description?"
    # prompt = f"Job Description: {job_description}\n\n  What are top 5 techical Skills required to apply givn job description? In the output only give list of top 5 Skills"

    #     from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAPI_KEY"))
    example_of_response = """
        {"top 5 skills for this job": ["Algorithem","Back-End Web Development","Machine Leraning","Java","SwiftUI"]},
        {"Resume Match Percentage" : 40%}
        """
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo-16k",
      messages=[
            {"role": "system", "content": f"""You are an assistant that helps 
            calculate resume match percentage. and give me top 5 techical Skills
             that should have to apply this job. The output shoud be a JSON similer to  {example_of_response}
             Do not return anything else than the JSON."""},
            {"role": "assistant", "content": example_of_response},
            {"role": "user", "content": prompt}
        ]
    )

    print(completion.choices[0].message)
    # Correctly access the content attribute
    completion_message = completion.choices[0].message.content
    print(f"completion_message = {completion_message}")
    Resume_Match_Percentage = completion_message.replace("[", "").replace("]", "").replace("{", "").replace("}", "\n")
    return Resume_Match_Percentage