from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from werkzeug.utils import secure_filename
from creds import UPLOAD_FOLDER, PARENT_FOLDER_ID, authenticate
from image_processor import ImagePreProcessor 
from ml_model import SvmModel

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        
        if file.filename == '':
            return "No file selected for upload."
        
        creds = authenticate()
        service = build('drive', 'v3', credentials=creds)
    
        try:
            # Process the uploaded image using ImageProcessor
            IMGPR = ImagePreProcessor()
            processed_img = IMGPR.for_saving(file)

            if processed_img is not None:
                # Save the processed image to a temporary file
                temp_filename = secure_filename(file.filename)
                temp_filepath = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
                cv2.imwrite(temp_filepath, processed_img)  # Save processed image

                # Prepare file metadata for Google Drive
                file_metadata = {
                    'name': file.filename,
                    'parents': [PARENT_FOLDER_ID],
                    'mimeType': 'image/jpeg'
                }

                # Create a MediaFileUpload object with the processed image content
                media = MediaFileUpload(temp_filepath, mimetype='image/jpeg', resumable=True)
                
                # Upload file to Google Drive
                file_drive = service.files().create(body=file_metadata, media_body=media).execute()
                print("File uploaded successfully:", file_drive)

                return redirect(url_for('index'))  # Redirect to a success page
            else:
                return "Error processing image."
        
        except Exception as e:
            print("Error uploading file:", e)
            return f"Error uploading file: {str(e)}"
    
    return 'Upload failed. No file provided or invalid request.'

@app.route('/uploaded_image')
def uploaded_image():
    # Placeholder route for displaying uploaded images
    return render_template('uploaded_image.html')

@app.route('/predict')
def predict():
    return render_template('predict_image.html')

@app.route('/predict_image', methods=['POST'])
def predict_image():
    if 'file' not in request.files:
        return "No file provided for prediction."

    file = request.files['file']
    if file.filename == '':
        return "No file selected for prediction."

    try:
        IMGPR = ImagePreProcessor()
        input_features = IMGPR.for_predicting(file_stream=file)

        if input_features is not None:
            # Reshape features for prediction
            input_features = input_features.reshape(1, -1)

            svm_model = SvmModel()
            prediction = svm_model.predict(input_features)
            return f"Prediction: {prediction[0]}"
        else:
            return "Error processing image."

    except Exception as e:
        print("Error predicting:", e)
        return f"Error predicting: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)