import requests

universe = "https://upload.wikimedia.org/wikipedia/commons/7/7d/2MASS_LSS_chart-NEW_Nasa.jpg"

response = requests.get(universe)

with open("universe.jpg", "wb")as file:
        file.write(response.content)
