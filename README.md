# SDE1 - MLE-Assignment

This project demonstrates the deployment of an image classification model as a web application using Flask, a Python web framework. The application allows users to upload an image, which is then classified into one of six categories: Building, Forest, Mountains, Glacier, Sea, or Streets. The classification is performed using a trained Support Vector Machine (SVM) model, which was trained on a dataset of images belonging to these categories. The application provides a simple and intuitive interface for users to interact with the model and receive predictions in real-time.

# # Structure: 

1. SDE Assignment.ipynb: This is the main Python script containing the Flask application code. It loads the trained model, defines routes for rendering the home page and handling image uploads, preprocesses the uploaded images, makes predictions using the model, and renders the prediction results on the web page.

2. model.p: This file contains the trained SVM model serialized using pickle. It is loaded by the Flask application to perform image classification.

3. templates/index.html: This HTML file defines the structure and layout of the web page. It contains a form for uploading images and displays the prediction results returned by the Flask application.

4. uploads/: This directory is used to store the images uploaded by users through the web application.

5. Clone the repository to your local machine using the following command:

   git clone https://github.com/your_username/image-classification-flask.git

7. Navigate to the project directory:

   cd image-classification-flask

9. Run the Flask application:

    python app.py

11. Open a web browser and navigate to http://localhost:5000 to access the web application.
