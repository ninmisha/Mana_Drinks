from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client.mana_drinks

# Sample products data
products = [
    {
        "name": "Melon & Mint",
        "description": "A refreshing blend of sweet melon and cool mint, our signature yerba mate is naturally energizing and deliciously crafted.",
        "price": 3.99,
        "image": "/static/images/melon-mint.png",
        "category": "drinks",
        "ingredients": ["organic yerba mate", "melon", "mint", "natural flavors"],
        "in_stock": True,
        "nutrition": {
            "serving_size": "355ml",
            "calories": 60,
            "caffeine": "80mg"
        }
    },
    {
        "name": "Grapefruit",
        "description": "Zesty and energizing grapefruit flavor combined with our signature yerba mate for a refreshing boost.",
        "price": 3.99,
        "image": "/static/images/grapefruit.png",
        "category": "drinks",
        "ingredients": ["organic yerba mate", "grapefruit", "natural flavors"],
        "in_stock": True,
        "nutrition": {
            "serving_size": "355ml",
            "calories": 60,
            "caffeine": "80mg"
        }
    },
    {
        "name": "Blackberry & Hibiscus",
        "description": "Sweet blackberries paired with floral hibiscus create a perfectly balanced yerba mate blend.",
        "price": 3.99,
        "image": "/static/images/blackberry-hibiscus.png",
        "category": "drinks",
        "ingredients": ["organic yerba mate", "blackberry", "hibiscus", "natural flavors"],
        "in_stock": True,
        "nutrition": {
            "serving_size": "355ml",
            "calories": 60,
            "caffeine": "80mg"
        }
    },
    {
        "name": "Tropical",
        "description": "An exotic blend of tropical fruits combined with our signature yerba mate for a taste of paradise.",
        "price": 3.99,
        "image": "/static/images/tropical.png",
        "category": "drinks",
        "ingredients": ["organic yerba mate", "pineapple", "mango", "passion fruit", "natural flavors"],
        "in_stock": True,
        "nutrition": {
            "serving_size": "355ml",
            "calories": 60,
            "caffeine": "80mg"
        }
    }
]

# Clear existing products
db.products.delete_many({})

# Insert new products
db.products.insert_many(products)

print("Database initialized with sample products!") 