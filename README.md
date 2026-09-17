# CodeAlpha URL Shortener

A backend URL Shortener API developed as part of the CodeAlpha Backend
Development Internship.

## Features

- Convert long URLs into short unique codes
- Store URL mappings in database
- Redirect short URLs to original URLs
- RESTful API
- Database integration
- Error handling

## Technologies

- Python
- Flask
- SQLAlchemy
- SQLite
- REST API

## Installation

### 1. Clone the repository

git clone <repository-url>

### 2. Create virtual environment

python -m venv venv

### 3. Activate environment

Windows:

venv\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure environment variables

Create a `.env` file based on `.env.example`.

### 6. Run the application

python run.py

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /shorten | Create short URL |
| GET | /<short_code> | Redirect to original URL |

## Internship

This project was developed as part of the
CodeAlpha Backend Development Internship.
