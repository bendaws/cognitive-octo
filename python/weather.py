import python_weather as weather

def get_weather():
    with weather.Client(unit=weather.IMPERIAL) as client:
        weather = client.get("New York")
    
        print("Current Temperature (F): {}".format(weather.temperature))