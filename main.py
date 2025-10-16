import request
def get_weather():
    result = request.get("www.ambiente.com/api")
    return result.json()["temperature"]