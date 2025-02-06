# Imports:
import pygame
import requests

# Initialise Pygame
pygame.init()

# Create a window/screen:
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Weather App")

# Create buttons:
days = pygame.Rect(100, 100, 100, 50)
wind = pygame.Rect(300, 100, 100, 50)
humidity = pygame.Rect(500, 100, 100, 50)
hours = pygame.Rect(700, 100, 100, 50)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (211, 211, 211)
clicked_color = (105, 105, 105)

def draw_button(button, color, text):
    """This function draws a button"""
    pygame.draw.rect(screen, color, button)
    font = pygame.font.SysFont("Arial", 15)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (button.x + 20, button.y + 20))


def get_weather(city, api_key):
    """This Function gets the weather from OpenWeatherMap API"""

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=parameters)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data: {e}")
        return

# A Loop that keeps the screen ON
running = True
button1_clicked = False
button2_clicked = False
button3_clicked = False
button4_clicked = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if days.collidepoint(mouse_pos):
                button1_clicked = not button1_clicked
            if wind.collidepoint(mouse_pos):
                button2_clicked = not button2_clicked
            if humidity.collidepoint(mouse_pos):
                button3_clicked = not button3_clicked
            if hours.collidepoint(mouse_pos):
                button4_clicked = not button4_clicked

    # Fill the screen with a background color (optional)
    screen.fill((255, 255, 255))

    # Draw the buttons with different colors based on their state
    draw_button(days, clicked_color if button1_clicked else button_color, "Days")
    draw_button(wind, clicked_color if button2_clicked else button_color, "Wind")
    draw_button(humidity, clicked_color if button3_clicked else button_color, "Humidity")
    draw_button(hours, clicked_color if button3_clicked else button_color, "Hours")

    # update the screen
    pygame.display.update()

# Quits the game
pygame.quit()