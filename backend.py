import requests

API_KEY = "0f879ce37195f20a8575ff242ad41b5d"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data['list'] # this is for 5 days and len of this dict is 40. So for 1 day we'll get 8 values or datapoints
    filter_data = filter_data[:8*days]
    nr_values = days * 8
    filter_data = filter_data[:nr_values]
    return filter_data


if __name__ == "__main__":
    print(get_data("mumbai", 3))


