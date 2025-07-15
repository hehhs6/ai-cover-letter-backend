from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ⚠️ Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyA8qqRU2jMOKU9eSC2O4N3wXUbfVxEhRxE")

@app.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter():
    data = request.json
    name = data.get("name", "John Doe")
    job_title = data.get("job_title", "Software Engineer")
    company = data.get("company", "ABC Corp")
    skills = data.get("skills", "Python, AI, Communication")
    style = data.get("style", "formal")

    prompt = f"""
    Write a {style} cover letter for the position of {job_title} at {company}.
    The candidate's name is {name}, and they have the following skills: {skills}.
    Make it professional and well-structured.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return jsonify({"cover_letter": response.text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
