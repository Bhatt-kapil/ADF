import requests
import mysql.connector

api_url = "https://api.jikan.moe/v4/anime?page=1&limit=25"
response = requests.get(api_url)
data = response.json()
anime_list = data.get('data', [])

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yuki_8686009',
    database='sekai'
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS anime (
        mal_id INT PRIMARY KEY,
        title VARCHAR(255),
        synopsis TEXT,
        episodes INT,
        score FLOAT,
        url VARCHAR(255)
    )
''')

for anime in anime_list:
    mal_id = anime.get('mal_id')
    title = anime.get('title')
    synopsis = anime.get('synopsis')
    episodes = anime.get('episodes')
    score = anime.get('score')
    url = anime.get('url')

    cursor.execute('''
        INSERT INTO anime (mal_id, title, synopsis, episodes, score, url)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            title = VALUES(title),
            synopsis = VALUES(synopsis),
            episodes = VALUES(episodes),
            score = VALUES(score),
            url = VALUES(url)
    ''', (mal_id, title, synopsis, episodes, score, url))

conn.commit()
conn.close()

print("Data successfully inserted into the MySQL database!")
