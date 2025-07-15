from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Securely load your Gemini API key from environment variable
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Use Gemini 1.5 Flash for faster, cheaper responses
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/generate-cover-letter", methods=["POST"])
def generate_cover_letter():
    data = request.get_json()

    job_title = data.get("job_title", "")
    company = data.get("company", "")
    skills = data.get("skills", "")
    experience = data.get("experience", "")
    tone = data.get("tone", "professional")

    prompt = f"""
    Write a {tone} cover letter for a position titled '{job_title}' at '{company}'.
    The applicant has the following skills: {skills}, and the following experience: {experience}.
    The letter should be concise, engaging, and suitable for copy-pasting into a job application.
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({"cover_letter": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
