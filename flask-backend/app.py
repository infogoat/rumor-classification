import pickle
import tensorflow as tf
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load trained tokenizer
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load trained LSTM model
model = tf.keras.models.load_model('rumor_stance_model (1).keras')  
# Define sequence length 
MAX_SEQUENCE_LENGTH = 100  

# Preprocessing function
def preprocess_input(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)
    return padded_sequence

# API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        headline = data.get('headline', '')

        # Preprocess the input
        processed_input = preprocess_input(headline)

        # Make prediction
        prediction = model.predict(processed_input)

        # Convert prediction to human-readable output
        result = 'True' if prediction[0][0] > 0.5 else 'False'  
        return jsonify(result=result, probability=float(prediction[0][0]))
    
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
