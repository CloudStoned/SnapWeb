from flask import Flask, render_template, request, redirect, url_for
from image_utils import ImageProcessor
import os
import cv2
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from werkzeug.utils import secure_filename
from creds import UPLOAD_FOLDER, PARENT_FOLDER_ID, authenticate

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def remove_temp_file(filepath):
    try:
        os.remove(filepath)
        print(f"Temporary file removed: {filepath}")
    except Exception as e:
        print(f"Error removing temporary file: {e}")

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
            image_processor = ImageProcessor()
            processed_img = image_processor.process_image(file)

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

                # Remove the temporary file after successful upload
                remove_temp_file(temp_filepath)

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

if __name__ == '__main__':
    app.run(debug=True)
