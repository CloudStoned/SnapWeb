from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.root_path, 'static/uploads', filename))
            return redirect(url_for('index')) 
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
