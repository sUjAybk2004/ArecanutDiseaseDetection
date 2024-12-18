from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the model once at the beginning of the app
model = load_model('your_model.keras')


# Prediction function
def predict_class(img_path):
    # Preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust size to your input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize as done during training

    # Make a prediction
    predictions = model.predict(img_array)

    # Get the predicted class (highest probability)
    predicted_class = np.argmax(predictions, axis=1)
    return predicted_class[0]


@app.route('/predict', methods=['POST'])
def predict():
    # Get the file from the request
    file = request.files['image']

    # Save the file temporarily
    img_path = "temp_image.jpg"
    file.save(img_path)

    # Get the prediction
    predicted_class = predict_class(img_path)

    # Return the result as a JSON response
    return jsonify({"predicted_class": int(predicted_class)})


if __name__ == "__main__":
    app.run(debug=True)
