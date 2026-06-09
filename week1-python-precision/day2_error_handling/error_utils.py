class InvalidInputError(Exception):
    pass

class InvalidAPICallError(Exception):
    pass

class EmptyStringError(Exception):
    pass

def Validate_city_name(name):
    if not isinstance(name,str):
        raise InvalidInputError(f"Input is not a string.Get {type(name).__name__}")
    if (len(name.strip())==0):
        raise InvalidInputError("Name cannot be empty")
    
    return f"Your entered value is: {name}"
    