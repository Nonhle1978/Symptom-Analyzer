from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def classify_symptoms(symptoms):
    text = symptoms.lower()
    if any(word in text for word in ["chest", "breath", "unconscious"]):
        return {"level": "High", "message": "Seek emergency medical care immediately.", "color": "red"}
    elif any(word in text for word in ["fever", "pain", "vomit"]):
        return {"level": "Medium", "message": "Visit a clinic or consult a healthcare professional.", "color": "orange"}
    else:
        return {"level": "Low", "message": "Monitor symptoms and consider home care.", "color": "green"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    symptoms = data.get('symptoms', '')
    result = classify_symptoms(symptoms)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
