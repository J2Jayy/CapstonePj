from flask import Flask, request, jsonify

import os
import openai

app = Flask(__name__)

# OPENAI API 키 설정 (환경 변수에서 가져오기)
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_fake_profile(survey_data):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Create a fake profile based on the following survey data: {survey_data}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

@app.route('/generate-profile', methods=['POST'])
def generate_profile():
    survey_data = request.json
    fake_profile = generate_fake_profile(survey_data)
    return jsonify({"profile": fake_profile})

if __name__ == '__main__':
    app.run(debug=True)
