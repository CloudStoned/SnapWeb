from flask import Flask, render_template, request, redirect, url_for
import os
from image_preprocess import pre_process_image
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.root_path, 'static/uploads', filename)
            
            # Preprocess the image (assuming pre_process_image is defined)
            try:
                pre_process_image(file, save_path)
            except Exception as e:
                return f"Error processing image: {str(e)}"

            return redirect(url_for('uploaded_image'))
    
    return 'Upload failed'

@app.route('/uploaded_image')
def uploaded_image():
    # Define the path to the uploads directory
    uploads_dir = os.path.join(app.root_path, 'static', 'uploads')
    
    # Get a list of filenames in the uploads directory
    filenames = os.listdir(uploads_dir)
    
    # Filter out non-image files (optional)
    image_filenames = [filename for filename in filenames if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Pass the list of image filenames to the template for rendering
    return render_template('uploaded_image.html', image_filenames=image_filenames)

if __name__ == '__main__':
    app.run(debug=True)
