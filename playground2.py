import requests
from auth_data import key
import schedule


def get_data():
    s_city = "Moscow,RU"
    city_id = 524901
    appid = key
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        weather = data['main']['temp']
        cond = data['weather'][0]['description']
        min_t = data['main']['temp_min']
        max_t = data['main']['temp_max']

        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("temp_min:", data['main']['temp_min'])
        print("temp_max:", data['main']['temp_max'])
        return [weather, cond, min_t, max_t]
    except Exception as e:
        print("Exception (weather):", e)
        pass

def main():
    schedule.every(10).seconds.do(get_data)
    # schedule.every().day.at('22:10').do(get_data)
    # schedule.every().thursday.do(get_data)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()
