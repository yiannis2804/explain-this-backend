from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # This allows your extension to access the API

# ✅ Replace this with your real API key
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Explain this simply:\n\n{text}"}
            ]
        )
        explanation = response['choices'][0]['message']['content']
        return jsonify({'explanation': explanation})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ This makes the server run when you run the file directly

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)

