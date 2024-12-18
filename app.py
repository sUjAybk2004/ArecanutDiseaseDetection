import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)

# Load the saved model
MODEL_PATH = "models/7.keras"
model = load_model(MODEL_PATH)

# Class names (from your dataset)
class_names = [
    'ChukkiRoga_Pat-1_High', 'ChukkiRoga_Pat-1_Low', 'ChukkiRoga_Pat-1_Medium',
    'ChukkiRoga_Pat-2_High', 'ChukkiRoga_Pat-2_Low', 'ChukkiRoga_Pat-2_Medium',
    'ChukkiRoga_Pat-3_High', 'ChukkiRoga_Pat-3_Low', 'ChukkiRoga_Pat-3_Medium',
    'Kole_roga', 'healthy'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    uploaded_file = request.files['image']

    if not uploaded_file or uploaded_file.filename == '':
        return render_template("error.html", message="No file uploaded!")

    if not uploaded_file.mimetype.startswith("image/"):
        return render_template("error.html", message="The uploaded file is not an image!")

    try:
        # Open the image with Pillow
        img = Image.open(uploaded_file)

        # Preprocess the image
        # img = img.resize((256, 256))  # Resize to model input size
        img_array = img_to_array(np.array(img))  # / 255.0  # Normalize the image...
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension...

        # Make prediction
        predictions = model.predict(img_array)

        res = np.argmax(predictions[0])
        print("predictions", predictions)
        # print("\nConfidence: ", confidence)

        print("Predicted class index :", res)
        print("Predicted class name :", class_names[res])

        # unwanted image identifier
        if predictions[0][res] <0.3:
            return render_template("error.html",
                                   message=f"Recheck the image and upload again. We are not sure about the image.")

        predicted_class = class_names[res]

        # Default values
        prediction = ""
        pathogen = ""
        intensity = ""

        # Check for patterns in the predictions
        if 'ChukkiRoga' in predicted_class:
            prediction = "Chukki Roga"

            if 'Pat-1' in predicted_class:
                pathogen = "Colletotrichum gloeosporioides"
            elif 'Pat-2' in predicted_class:
                pathogen = "Pestolotica areca"
            elif 'Pat-3' in predicted_class:
                pathogen = "Phyllosticta arecae"

            if 'High' in predicted_class:
                intensity = "High"
            elif 'Medium' in predicted_class:
                intensity = "Medium"
            elif 'Low' in predicted_class:
                intensity = "Low"

        elif 'Kole_roga' in predicted_class:
            prediction = "Kole Roga"
            pathogen = "N/A"
            intensity = "N/A"

        elif 'healthy' in predicted_class:
            prediction = "Healthy"
            pathogen = "N/A"
            intensity = "N/A"

        else:
            prediction = "Unknown"
            pathogen = "N/A"
            intensity = "N/A"

        # os.remove(filepath)
        # Render the result page
        return render_template(
            "result.html",
            predicted_class=prediction,
            pathogen=pathogen,
            intensity=intensity,
        )
    except Exception as e:
        return render_template("error.html", message=f"Error processing image: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
