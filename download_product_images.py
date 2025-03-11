import os
import shutil
from PIL import Image

# Create static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

def save_hero_image():
    try:
        # Source image path (your WhatsApp image)
        source_image = "WhatsApp Image 2025-03-10 at 11.44.01_19d96c48.jpg"
        
        # Destination path in static/images
        destination = os.path.join('static', 'images', 'hero-background.jpg')
        
        # Simple file copy if image manipulation fails
        shutil.copy2(source_image, destination)
        print(f"Successfully saved hero image to {destination}")
    except Exception as e:
        print(f"Error saving hero image: {str(e)}")

if __name__ == '__main__':
    save_hero_image() 