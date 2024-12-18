from flask import Flask,redirect,url_for,render_template,request,jsonify 
from PIL import Image,UnidentifiedImageError 
import io 
import numpy as np 
# import pickle 
 
app=Flask(__name__) 
 
@app.route('/') 
def welcome(): 
    return render_template('index.html') 
 
@app.route("/upload", methods=["POST"]) 
def upload(): 
    uploaded_file = request.files.get('image') 
 
    if not uploaded_file or uploaded_file.filename == '': 
        return render_template("error.html", message="No file uploaded!") 
 
    try: 
        # Check if the uploaded file is a valid image using its MIME type 
        if not uploaded_file.mimetype.startswith("image/"): 
            return render_template("error.html", message="The uploaded file is not an image!") 
 
        # Process the uploaded image 
        image = Image.open(uploaded_file) 
        image_format = image.format 
        image_size = image.size 
 
        # Pass data to the result page 
        return render_template( 
            "result.html", 
            message="Image uploaded successfully!", 
            format=image_format, 
            size=image_size, 
        ) 
    except Exception as e: 
        return render_template("error.html", message="Invalid image file!") 
 
if __name__=='__main__': 
    app.run(debug=True)