import os
import json
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import torch
from flask_cors import CORS

# Configure paths
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates', 'tailwind')
# STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates', 'tailwind')  
STATIC_DIR = os.path.join(BASE_DIR, 'static')
USER_DATA_FILE = os.path.join(BASE_DIR, 'user_data.json')

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

# Helper function to load user data from JSON
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w') as f:
            json.dump({}, f)
    with open(USER_DATA_FILE, 'r') as f:
        return json.load(f)

# Helper function to save user data to JSON
def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f)

# Registration route
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user_data = load_user_data()

    if username in user_data:
        return jsonify({"error": "Username already exists"}), 400

    user_data[username] = password
    save_user_data(user_data)
    return jsonify({"message": "Registration successful"}), 200

# Login route
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user_data = load_user_data()

    if username in user_data and user_data[username] == password:
        return jsonify({"message": "Login successful"}), 200
    elif username not in user_data:
        return jsonify({"error": "Username not found"}), 404
    else:
        return jsonify({"error": "Invalid password"}), 401
ic
# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

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
        print(data)
        text = data.get('headline', '')
        
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
        
        # return jsonify({
        #     "prediction": best_label,
        #     "confidence": round(best_score, 3)
        # })

        return jsonify({
    "result": {
        "label": best_label,
        "score": round(best_score, 3)
    }
})

    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/opinion')
def opinion():
    return render_template('opinion.html')

if __name__ == '__main__':
    app.run(debug=True)

