# ClimateHub 🌤️

![Screenshot 2024-10-18 154440](https://github.com/user-attachments/assets/441ee2cd-d047-4121-9e59-d23a957e573f)


**ClimateHub** is a Django-based weather application that fetches real-time weather information using the OpenWeatherMap API. The application allows users to search for the current weather in any city, view weather details like temperature, humidity, wind speed, and more. The search history is stored in a database and can be viewed at any time.

## Features

- 🌍 Real-time weather data for any city using OpenWeatherMap API.
- 💧 Displays temperature, wind speed, humidity, and weather conditions.
- 🕓 Tracks and stores search history.
- 🎨 Dynamic background and animations based on the weather conditions (sunny, cloudy, rainy, etc.).
- 🌐 User-friendly interface built with Bootstrap for responsive design.

## Videos
Default Interface:

https://github.com/user-attachments/assets/5926ad5f-5719-4d71-b0b4-8e1cadea548a

Weather History

https://github.com/user-attachments/assets/286b64d5-c2b3-444f-9bbf-ee5d80fc96fd


## Screenshots

![image](https://github.com/user-attachments/assets/0dd28d6d-fe8e-4cbf-bf4d-e0cf07cd192f)
![image](https://github.com/user-attachments/assets/bf12cb4f-a49e-4d33-b33d-2a00bdd53788)
![image](https://github.com/user-attachments/assets/a08eff76-f7bc-4ebe-b520-52f87ddfe0bb)

## Tech Stack

- **Backend**: Django 3.2+ (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **API**: [OpenWeatherMap](https://openweathermap.org/)
- **Database**: SQLite (default, can be changed)
- **Version Control**: Git/GitHub

## Installation and Setup

### Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.x**: Download from [here](https://www.python.org/downloads/).
- **Django**: Install by running `pip install django`.
- **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get an API key.

### Clone the repository

To get a local copy of the project, run:

```bash
git clone https://github.com/yourusername/ClimateHub.git
cd ClimateHub
```

### Install the dependencies

It is recommended to use a virtual environment. Run the following commands to set up:

```bash
# Create and activate virtual environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Set up environment variables

Create a `.env` file or use Django's `settings.py` to configure your OpenWeatherMap API key:

```plaintext
WEATHER_API_KEY=your_openweathermap_api_key_here
```

Alternatively, add this to `settings.py`:

```python
import os
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'your_default_api_key')
```

### Migrate the database

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000` to view the app.

## Usage

1. **Search for Weather**: Enter the name of a city in the search bar and get real-time weather details.
2. **View Weather History**: Click on "View Weather History" to see a list of previous searches.

## Project Structure

```
ClimateHub/
│
├── ClimateHub/           # Django project files
├── skywatcher/           # Django app for weather features
│   ├── migrations/       # Django migrations for database
│   ├── templates/        # HTML templates (index.html, history.html)
│   ├── models.py         # Weather model for storing data
│   ├── views.py          # Handles requests and weather API integration
│   ├── urls.py           # URL routing for the app
│
├── static/               # Static files like CSS/JS (if any)
├── db.sqlite3            # Default SQLite database (auto-generated)
├── manage.py             # Django management script
├── .env                  # Environment variables (not included in repo)
├── README.md             # This README file
└── requirements.txt      # Dependencies
```

## API Integration

The application uses the **OpenWeatherMap API** to fetch weather data. The main API URL structure:

```
https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric
```

Replace `{city}` with the name of the city and `{api_key}` with your API key. The weather details are fetched in **metric units** (Celsius).

## Customization

- You can modify the API request units to get weather data in **Imperial** units (Fahrenheit) by setting `units=imperial` in the API URL.
- Background animations and colors are dynamically updated based on weather conditions (e.g., sunny, cloudy, rainy).

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Contributions are always welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/) for providing weather data.
- [Bootstrap](https://getbootstrap.com/) for styling and layout.

---
**Powered by ClimateHub — All Rights Reserved © 2024**

```
