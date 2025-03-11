import os
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
from io import BytesIO

# Create static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Mana Yerba Mate product images
product_images = {
    'melon-mint.png': 'https://manayerbamate.com/cdn/shop/files/slider-melon-01_710x840_crop_center.jpg?v=1717777981',
    'grapefruit.png': 'https://manayerbamate.com/cdn/shop/products/pamplemousse-01_0e1b45ec-4258-4ee9-ab96-644486715cbf_710x840_crop_center.jpg?v=1672091392',
    'blackberry-hibiscus.png': 'https://manayerbamate.com/cdn/shop/files/mures-02_827x980.jpg?v=1658150775',
    'tropical.png': 'https://manayerbamate.com/cdn/shop/files/tropical-02_827x980.jpg?v=1658150775'
}

# Store location information and images
stores = {
    'downtown.png': {
        'name': 'Downtown Store',
        'address': '123 Main St, City Center',
        'phone': '(555) 123-4567',
        'hours': '''Opening Hours
Monday - Friday: 9:00 AM - 8:00 PM
Saturday: 10:00 AM - 6:00 PM
Sunday: Closed''',
        'image_url': 'https://c8.alamy.com/comp/R821CM/portland-oregonusa-october-8-2016-a-bike-shop-store-front-with-multiple-bikes-lined-up-on-the-sidewalk-in-downtown-portland-oregon-R821CM.jpg'
    },
    'westside.png': {
        'name': 'Westside Location',
        'address': '456 West Ave, Shopping District',
        'phone': '(555) 234-5678',
        'hours': '''Opening Hours
Monday - Friday: 9:00 AM - 8:00 PM
Saturday: 10:00 AM - 6:00 PM
Sunday: Closed''',
        'image_url': 'https://www.speedpro.com/saint-petersburg/wp-content/uploads/sites/108/2022/11/IMG_9324.jpg'
    },
    'mall-kiosk.png': {
        'name': 'Mall Kiosk',
        'address': '789 Mall Road, Food Court',
        'phone': '(555) 345-6789',
        'hours': '''Opening Hours
Monday - Friday: 9:00 AM - 8:00 PM
Saturday: 10:00 AM - 6:00 PM
Sunday: Closed''',
        'image_url': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/af/40/0b/photo0jpg.jpg?w=900&h=500&s=1'
    }
}

def download_image(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        filepath = os.path.join('static/images', filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def create_store_image(filename, store_info):
    try:
        # Create a new image with a white background
        width = 800
        height = 600
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
        
        # Try to use Arial font, fallback to default if not available
        try:
            title_font = ImageFont.truetype('arial.ttf', 48)
            regular_font = ImageFont.truetype('arial.ttf', 24)
        except:
            title_font = ImageFont.load_default()
            regular_font = ImageFont.load_default()

        # If store has an image URL, try to download and use it
        if 'image_url' in store_info:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(store_info['image_url'], headers=headers)
                response.raise_for_status()
                
                # Save temporary image
                temp_image = Image.open(BytesIO(response.content))
                # Resize to fit the top half of our image
                temp_image = temp_image.resize((800, 300), Image.Resampling.LANCZOS)
                image.paste(temp_image, (0, 0))
                
                # Start text below the image
                y_position = 320
            except:
                y_position = 50
        else:
            y_position = 50

        # Store name
        draw.text((width/2, y_position), store_info['name'], font=title_font, fill='black', anchor='mm')
        y_position += 80

        # Address
        draw.text((width/2, y_position), store_info['address'], font=regular_font, fill='black', anchor='mm')
        y_position += 40

        # Phone
        draw.text((width/2, y_position), store_info['phone'], font=regular_font, fill='black', anchor='mm')
        y_position += 60

        # Hours
        for line in store_info['hours'].split('\n'):
            draw.text((width/2, y_position), line, font=regular_font, fill='black', anchor='mm')
            y_position += 30

        # Save the image
        filepath = os.path.join('static/images', filename)
        image.save(filepath)
        print(f"Successfully created {filename}")
    except Exception as e:
        print(f"Error creating {filename}: {str(e)}")

# Download product images
for filename, url in product_images.items():
    download_image(url, filename)

# Create store location images
for filename, store_info in stores.items():
    create_store_image(filename, store_info) 