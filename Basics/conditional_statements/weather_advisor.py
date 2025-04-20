# Here task is to create a function that provides a weather advisory message based on the current temperature.
# - If the temperature is below 0, return "It's freezing! Wear a heavy coat."
# - If the temperature is between 0 and 10 (inclusive), return "It's cold! Bundle up."
# - If the temperature is between 11 and 20 (inclusive), return "It's cool! A light jacket will do."
# - If the temperature is above 20, return "It's warm! Enjoy the day."

def provide_weather_advisory(temperature):
    if temperature < 0:
        return "It's freezing! Wear a heavy coat."
    elif temperature > 0 and temperature <= 10:
        return "It's cold! Bundle up."
    elif temperature > 10 and temperature <= 20:
        return "It's cool! A light jacket will do."
    else:
        return "It's warm! Enjoy the day."

print(provide_weather_advisory(-10))
