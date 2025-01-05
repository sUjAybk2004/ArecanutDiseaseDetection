
Arecanut Disease Detection System

This project is a web-based machine learning application designed to detect diseases in arecanut crops. It allows users to upload images of arecanut leaves and receive predictions about the presence of diseases.
Features

- **Disease Detection:** Upload images to detect arecanut diseases using a trained TensorFlow model.
- **User-Friendly Interface:** A simple and intuitive web application interface built with Flask.
- **Efficient Model:** The TensorFlow model is optimized for high accuracy and performance.
  
Project Structure
.idea/                   # IDE configuration files
.ipynb_checkpoints/      # Jupyter Notebook checkpoints
Dataset/                 # Dataset used for training the model
__pycache__/             # Python cache files
instance/uploads/        # Temporary storage for uploaded files
models/                  # Machine learning models
static/                  # Static assets (CSS, JS, images)
templates/               # HTML templates
uploads/                 # Uploaded files
.gitignore               # Files to ignore in version control
Arecanut.ipynb           # Jupyter Notebook for training the model
app.py                   # Flask application entry point
dummy.py                 # Placeholder/test script
main.py                  # Main backend logic
mainBG.py                # Additional backend logic
requirements.txt         # Python dependencies
test.py                  # Test script
test_main.http           # HTTP request testing
```

Setup and Installation

Prerequisites

- Python 3.8 or above
- pip (Python package installer)

Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/arecanut-disease-detection.git
   cd arecanut-disease-detection


2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. Open the application in your web browser.
2. Upload an image of an arecanut leaf.
3. Click on "Submit" to get the prediction result.
4. View the predicted disease or confirmation of a healthy leaf.

## Dataset

The `Dataset` folder contains images of arecanut leaves used to train the TensorFlow model. The data is pre-processed and split into training and validation sets.

## Model

The machine learning model is implemented using TensorFlow and is stored in the `models/` directory. Refer to `Arecanut.ipynb` for the training process and model evaluation.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

- Thanks to the farming community for their feedback and support.
- TensorFlow documentation for guiding model implementation.

Feel free to customize this based on any additional details or specific requirements for your project!
