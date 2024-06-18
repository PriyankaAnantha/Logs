# Task 1: Django and FastAPI Integration
Create an UI using Django which render an UI table. 
For data fetch, create fast API that accept yahoo finance company ticker name, time frame and start date and end date

---
## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [License](#license)

## Overview
This project demonstrates the integration of Django with FastAPI to fetch financial data from Yahoo Finance. The Django application provides a web interface to input stock ticker information and retrieve historical data through a FastAPI backend.

## Features
- Fetch historical stock data from Yahoo Finance
- Display data in a tabular format on a web page
- Integration of Django for frontend and FastAPI for backend

## Prerequisites
- Python 3.8+
- pip (Python package installer)

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/PriyankaAnantha/Logs.git
    cd Logs/task1
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Django migrations**
    ```bash
    python manage.py migrate
    ```

## Running the Application

1. **Start the FastAPI server**
    ```bash
    uvicorn fastapi_app:app --host 127.0.0.1 --port 8001 --reload
    ```

2. **Start the Django server**
    ```bash
    python manage.py runserver 8000
    ```

3. **Access the application**
    Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. **Open the web application** at `http://127.0.0.1:8000/`
2. **Fill out the form** with the stock ticker, time frame, start date, and end date.
3. **Submit the form** to fetch and display the historical stock data.

## Project Structure
```
Logs/
├── task1/
│   ├── fastapi_app.py          # FastAPI application
│   ├── manage.py               # Django project management
│   ├── requirements.txt        # Project dependencies
│   ├── task1/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── ...
│   └── task1app/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       ├── views.py
│       └── templates/
│           └── task1app/
│               └── index.html  # Django HTML template
└── ...
```


## API Documentation

### FastAPI Endpoint
- **URL:** `/fetch-data/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "ticker": "AAPL",
        "timeframe": "1d",
        "start_date": "2022-01-01",
        "end_date": "2022-12-31"
    }
    ```
- **Response:**
    ```json
    {
        "data": "Date,Open,High,Low,Close,Adj Close,Volume\n2022-01-03,182.630005,182.940002,177.710007,182.009995,181.078888,104487900\n..."
    }
    ```

### Django Form Submission
- **URL:** `/`
- **Method:** `POST`
- **Form Data:**
    - `ticker` (e.g., `AAPL`)
    - `timeframe` (e.g., `1d`)
    - `start_date` (e.g., `2022-01-01`)
    - `end_date` (e.g., `2022-12-31`)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/PriyankaAnantha/Logs/blob/main/task1/LICENSE.txt) file for details.

## Acknowledgemets
Mentor: Mr. Shivendra Singh 

