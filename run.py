from flask import Flask, render_template, request, redirect, url_for
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = '1BJY2TgB0rknJNYvfARpaa4zgEytH6Sju'  # Replace with your Google Drive folder ID

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

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
            # Save the uploaded file to a temporary location
            temp_filename = secure_filename(file.filename)
            temp_filepath = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
            
            # Write the file to the temporary location
            file.save(temp_filepath)
            
            # Prepare file metadata
            file_metadata = {
                'name': file.filename,
                'parents': [PARENT_FOLDER_ID],
                'mimeType': 'image/jpeg'
            }
            
            # Create a MediaFileUpload object with the file content
            media = MediaFileUpload(temp_filepath, mimetype='image/jpeg', resumable=True)
            
            # Upload file to Google Drive
            file_drive = service.files().create(body=file_metadata, media_body=media).execute()
            
            print("File uploaded successfully:", file_drive)
            # Close the file handle explicitly
            file.close()
            
            # Clean up: remove temporary file
            os.remove(temp_filepath)
            print("Temporary file removed:", temp_filepath)
            
            return redirect(url_for('index'))
        
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
