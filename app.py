from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# ✅ Configure OpenAI client using the new SDK format
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/explain', methods=['POST'])
def explain():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Explain this simply:\n\n{text}"}]
        )
        explanation = response.choices[0].message.content
        return jsonify({'explanation': explanation})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
