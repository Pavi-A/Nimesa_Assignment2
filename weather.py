import requests
api_url ="https://api.openweathermap.org/data/2.5/weather?q=London,us&units=metric&appid=e6da7d971ac95cbe5b5cca04bd666b56"
def get_weather_data():
    response = requests.get(api_url) 
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data from the API.")
        return None
def get_temperature(data, date_time):
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['temp']
    return None
def get_wind_speed(data, date_time):
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['wind']['speed']
    return None
def get_pressure(data, date_time):
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['pressure']
    return None
while True:
    print("\nOptions:")
    print("1. Get Temperature")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        date_time = input("Enter date and time")
        data = get_weather_data()
        if data:
            temperature = get_temperature(data, date_time)
            if temperature:
                print(f"Temperature at {date_time}: {temperature}°C")
            else:
                print(f"No data available for {date_time}.")
    
    elif choice == '2':
        date_time = input("Enter date and time")
        data = get_weather_data()
        if data:
            wind_speed = get_wind_speed(data, date_time)
            if wind_speed:
                print(f"Wind Speed at {date_time}: {wind_speed} m/s")
            else:
                print(f"No data available for {date_time}.")
    
    elif choice == '3':
        date_time = input("Enter date and time")
        data = get_weather_data()
        if data:
            pressure = get_pressure(data, date_time)
            if pressure:
                print(f"Pressure at {date_time}: {pressure} hPa")
            else:
                print(f"No data available for {date_time}.")
    
    elif choice == '0':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")






