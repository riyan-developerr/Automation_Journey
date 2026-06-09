from error_utils import (Validate_city_name,EmptyStringError,InvalidInputError)
from api_caller import safe_fetch_weather
try:
    result=Validate_city_name("Riyan Ahmed")
    result=Validate_city_name(12)
    result=Validate_city_name("")
except InvalidInputError as e:
    print(f"error: {e}")
finally:
    print("[log] The program is finished")
    
test_location=[
    "Faisalabad",
    "London",
    12345,
    "",
    "Karachi"
]

for places in test_location:
    print(f"\n--- Testing input: {repr(places)} ---")
    result=safe_fetch_weather(places)
    if result:
        print(f"Weather in {result['city']}:")
        print(f"  Temp: {result['temperature_c']}°C")
        print(f"  Feels like: {result['feels_like_c']}°C")
        print(f"  Humidity: {result['humidity']}%")
        print(f"  Condition: {result['description']}")
        
    else:
        print("No result returned")