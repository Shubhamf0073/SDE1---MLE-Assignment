import os
import pickle
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from skimage.io import imread
from skimage.transform import resize
import numpy as np

app = Flask(__name__)
run_with_ngrok(app)

# Load the trained model
model_path = "model.p"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Define the categories
categories = ["Building", "Forest", "Mountains", "Glacier", "Sea", "Streets"]

# Define the upload folder for images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def preprocess_image(image):
    # Resize the image
    resized_image = resize(image, (15, 15))
    # Flatten the image array
    flattened_image = resized_image.flatten()
    return flattened_image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction_text='No file uploaded')

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction_text='No file selected')

    if file:
        # Save the uploaded image
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Load and preprocess the uploaded image
        image = imread(filename)
        preprocessed_image = preprocess_image(image)

        # Make prediction using the model
        prediction = model.predict([preprocessed_image])[0]
        predicted_category = categories[prediction]

        return render_template('index.html', predicted_text=f'The image belongs to category: {predicted_category}')

if __name__ == "__main__":
    app.run()
