import os
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import torch
from flask_cors import CORS

# Configure paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates', 'tailwind')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')

app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)
CORS(app)

# Initialize classifier
try:
    classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
        device=0 if torch.cuda.is_available() else -1
    )
    print("Model loaded successfully")
except Exception as e:
    print(f"Model loading failed: {str(e)}")
    classifier = None

# Preprocessing function
def preprocess_input(text):
    return text.strip()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-page')  # New route for prediction interface
def predict_page():
    return render_template('prediction.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if not classifier:
        return jsonify(error="Model not loaded"), 500

    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify(error="No text provided"), 400

        # Define candidate labels clearly
        candidate_labels = ["support", "deny", "question", "neutral"]
        result = classifier(text, candidate_labels, multi_label=False)
        
        # Get raw scores
        scores = result["scores"]
        labels = result["labels"]
        
        # Find the label with the highest score
        best_label = labels[0]
        best_score = scores[0]

        # Force neutral if confidence is low
        if best_score < 0.4:
            best_label = "neutral"
        
        return jsonify({
            "prediction": best_label,
            "confidence": round(best_score, 3)
        })

    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)

