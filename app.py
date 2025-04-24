from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_DISPLAY_IMAGES'] = 4  # Show only 4 most recent images
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_sorted_images():
    """Get images sorted by modification time (newest first)"""
    try:
        images = []
        for f in os.listdir(app.config['UPLOAD_FOLDER']):
            path = os.path.join(app.config['UPLOAD_FOLDER'], f)
            if os.path.isfile(path):
                images.append({
                    'name': f,
                    'path': path,
                    'mtime': os.path.getmtime(path)
                })
        # Sort by modification time (newest first)
        return sorted(images, key=lambda x: x['mtime'], reverse=True)
    except FileNotFoundError:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'image' in request.files:
        file = request.files['image']
        if file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Get only the 4 most recent images
    images = get_sorted_images()[:app.config['MAX_DISPLAY_IMAGES']]
    gallery_urls = [url_for('static', filename=f'uploads/{img["name"]}') for img in images]
    
    return render_template('index.html', gallery_urls=gallery_urls)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)