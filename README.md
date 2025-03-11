# Mana Yerba Mate Website Clone

A modern web application clone of the Mana Yerba Mate website built with Flask and MongoDB.

## Features

- Responsive design using Tailwind CSS
- Dynamic product catalog
- MongoDB integration
- RESTful API endpoints
- Modern UI/UX

## Prerequisites

- Python 3.8 or higher
- MongoDB
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mana-yerba-mate-clone
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```
MONGO_URI=mongodb://localhost:27017/mana_drinks
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

5. Initialize the database with sample data:
```bash
python init_db.py
```

## Running the Application

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
mana-yerba-mate-clone/
├── app.py              # Main Flask application
├── init_db.py         # Database initialization script
├── requirements.txt   # Python dependencies
├── static/           # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css
│   └── images/
├── templates/        # HTML templates
│   ├── base.html
│   └── index.html
└── .env             # Environment variables
```

## API Endpoints

- `GET /api/products` - Get all products
- `GET /api/products/<product_id>` - Get a specific product
- `POST /api/products` - Add a new product

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 