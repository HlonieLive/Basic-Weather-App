# Weather-App

A simple GUI-based weather application built using Python's Pygame library. This app fetches real-time weather data from the OpenWeatherMap API and displays it in a user-friendly interface. 

## Features 

    Displays current weather information (temperature, wind speed, humidity).
    Interactive buttons to toggle between different weather parameters.
    Fetches data from the OpenWeatherMap API.
    Simple and intuitive graphical user interface (GUI).
     

## Prerequisites 

Before running the app, ensure you have the following installed: 

    Python : Version 3.6 or higher.
        Download from: https://www.python.org/downloads/ 
         
    Pygame : A Python library for creating games and GUIs.
    Requests : A Python library for making HTTP requests.
     

## Installation 

1. Clone the repository or download the source code: 
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
     
 
2. Install the required dependencies: 
    pip install pygame requests
     
     

3. Obtain an API key from OpenWeatherMap: 
    Sign up at: https://openweathermap.org/appid 
    Replace <YOUR_API_KEY> in the weather_app.py file with your actual API key.
         

## Usage

Clone the repository or download the source code:
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
        
 

Install the required dependencies using the requirements.txt file: 
    pip install -r requirements.txt
 
 

Obtain an API key from OpenWeatherMap: 
    Sign up at: https://openweathermap.org/appid 
    Replace <YOUR_API_KEY> in the weather_app.py file with your actual API key.


Run the script:
    python3 weather_app.py
     
     
A Pygame window will open, displaying four buttons: 
    **Days** : Shows the current weather data (temperature, wind speed, humidity).
    **Wind** : Placeholder for wind-related details.
    **Humidity** : Placeholder for humidity-related details.
    **Hours** : Placeholder for hourly weather forecasts.
         

Click on any button to toggle its visibility and display the corresponding weather information. 
     

## Configuration

**API Key**

To use the app, you need to configure the OpenWeatherMap API key. Follow these steps: 

    Open the weather_app.py file in a text editor.
    Locate the line where API_KEY is defined:

        API_KEY = "<YOUR_API_KEY>"
     
     
Replace <YOUR_API_KEY> with your actual API key obtained from OpenWeatherMap.
 
 
## Contributing 

Contributions are welcome! If you'd like to improve this project, follow these steps: 

    Fork the repository.
    Create a new branch: git checkout -b feature/new-feature.
    Make your changes and commit them: git commit -m "Add new feature".
    Push to the branch: git push origin feature/new-feature.
    Submit a pull request.
     

## License 

This project is licensed under the MIT License. See the LICENSE  file for more details.


## Acknowledgments 

    OpenWeatherMap  for providing the weather data API.
    Pygame  for enabling the creation of the GUI. 