# HNG-Stage-One-Task---Backend-Track

# Django Web Server - API Endpoint Example

This project sets up a basic Django web server that exposes an API endpoint to greet a visitor with their name, IP address, and current weather information based on their location.

## Setup Instructions

### Prerequisites

- Python (version 3.8 or higher)
- Django
- Requests library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/daniel-caleb/HNG-Stage-One-Task---Backend-Track.git
   cd my_web_server

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Set up environment variables:

- Obtain an API key from OpenWeatherMap (https://home.openweathermap.org/users/sign_up)
- Set your API key in the environment variable OPENWEATHER_API_KEY (e.g., export OPENWEATHER_API_KEY='your_openweather_api_key')

5. Start the development server:

    ```bash
    python manage.py runserver

## Usage

```
GET /api/hello/
```
![weather](https://github.com/daniel-caleb/HNG-Stage-One-Task---Backend-Track/assets/95380895/50a86d60-0b36-4d1c-aadd-de59e513a971)
