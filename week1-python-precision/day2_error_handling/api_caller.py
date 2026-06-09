from error_utils import Validate_city_name,InvalidAPICallError,InvalidInputError,EmptyStringError
import requests

def fetch_weather(city):
    try:
        Validate_city_name(city)
    except InvalidInputError as e:
        print(f"[INPUT ERROR]: {e}")
        return None
    
    url=f"https://wttr.in/{city}?format=j1"
    
    try:
        response=requests.get(url=url,timeout=5)
        #Raises HTTPError, if one occurred
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise InvalidAPICallError("API was not able to connect.Check your internet")
    except requests.exceptions.Timeout:
        raise InvalidAPICallError("Time out error occured")
    except requests.exceptions.HTTPError as e:
        raise InvalidAPICallError(f"API returned an error:{e}")
    
    #parsing (saving data from api as python list/dict to obtain info)
    try:
        data=response.json()
        
        if not data:
            raise EmptyStringError("API returned empty response")
        current = data["current_condition"][0]

        result = {
            "city": city,
            "temperature_c": current["temp_C"],
            "feels_like_c": current["FeelsLikeC"],
            "humidity": current["humidity"],
            "description": current["weatherDesc"][0]["value"]
        }
        # print(data)
        return result
    except (KeyError,IndexError) as e:
        raise EmptyStringError(f"API error some missing field :{e}")
    
        
    

def safe_fetch_weather(city):
    try:
        output=fetch_weather(city)
        return output
    except InvalidAPICallError as e:
        print(f"[API call error]: {e}")
        return None
    except EmptyStringError as e:
        print(f"[data error]: {e}")
        return None
    except Exception as e:
        print(f"[Unexpected error]: {e}")
        return None
    finally:
        print(f"[log] fetch attempt is finished for city {city}")