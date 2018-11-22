import requests
import click

# SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

@click.command()
@click.argument('location')
@click.option('--api-key', '-a')
def main(location, api_key):
    weather = current_weather(location, api_key)
    print(f"The weather in {location} right now: {weather}.")

if __name__ == "__main__":
    main()
