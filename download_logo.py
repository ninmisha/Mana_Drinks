import requests
import os

# Create static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Logo URL
logo_url = 'https://i.pinimg.com/736x/b7/cc/3d/b7cc3dfc810c12bd36976eebb7a10535.jpg'

def download_logo():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(logo_url, headers=headers)
        response.raise_for_status()
        
        filepath = os.path.join('static/images', 'logo.png')
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print("Successfully downloaded logo.png")
        return True
    except Exception as e:
        print(f"Error downloading logo: {str(e)}")
        return False

if __name__ == '__main__':
    download_logo() 