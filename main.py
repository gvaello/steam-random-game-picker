from flask import Flask, request, jsonify, render_template
import requests
import random
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
STEAM_API_KEY = os.getenv("API_KEY")


def get_steam_id(vanity_url):
    url = f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={STEAM_API_KEY}&vanityurl={vanity_url}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Received response with status code {response.status_code}")
        return None

    try:
        data = response.json()
        if 'response' in data and 'steamid' in data['response']:
            return data['response']['steamid']
        else:
            print(f"Error: Unable to resolve Steam ID for vanity URL {vanity_url}")
            return None
    except ValueError as e:
        print(f"Error: JSON decoding failed: {e}")
        print(f"Response content: {response.content}")
        return None


def get_owned_games(steam_id):
    url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={STEAM_API_KEY}&steamid={steam_id}&format=json&include_appinfo=true&include_played_free_games=true'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Received response with status code {response.status_code}")
        print(f"Response content: {response.content}")
        return None

    try:
        return response.json()
    except ValueError as e:
        print(f"Error: JSON decoding failed: {e}")
        print(f"Response content: {response.content}")
        return None


@app.route('/')
def index():
    return render_template('index.html')


def get_game_details(appid):
    url = f'https://store.steampowered.com/api/appdetails?appids={appid}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if data and str(appid) in data:
                return data[str(appid)].get('data', {}).get('genres', [])
        except ValueError as e:
            app.logger.error(f"Error: JSON decoding failed: {e}")
            app.logger.error(f"Response content: {response.content}")


@app.route('/get_random_game', methods=['POST'])
def get_random_game():
    vanity_url = request.form['steam_id']
    min_hours = int(request.form['min_hours'])
    genres = request.form.getlist('genre')

    steam_id = get_steam_id(vanity_url)
    if steam_id is None:
        return jsonify({'error': 'Unable to resolve Steam ID for the provided username.'})

    data = get_owned_games(steam_id)
    if data is None or 'response' not in data or 'games' not in data['response']:
        return jsonify({'error': 'No games found for this user or an error occurred.'})

    games = data['response']['games']
    filtered_games = [
        {
            'appid': game['appid'],
            'name': game['name'],
            'img_icon_url': game['img_icon_url'],
            'playtime_forever': game['playtime_forever']/60
        }
        for game in games if (game['playtime_forever'] / 60) >= float(min_hours)
    ]

    if genres:
        filtered_games = [
            game for game in filtered_games
            if get_game_details(game['appid']) is not None and all(
                genre in get_game_details(game['appid']) for genre in genres)
        ]

    if not filtered_games:
        return jsonify({'error': 'No games match the criteria.'})

    random_game = random.choice(filtered_games)
    return jsonify(random_game)


if __name__ == '__main__':
    app.run(debug=True)
