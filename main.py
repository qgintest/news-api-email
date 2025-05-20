import requests

api_key = "af5753fe4c814362a643c9deefaaf072"

url = (f"https://newsapi.org"
       f"/v2/everything?q=tesla&from=2025-04-20&sortBy=publishedAt&"
       f"apiKey={api_key}")

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
# }

request = requests.get(url)
content = request.json()
articles = content["articles"]
articleSize = len(content["articles"])

print(articles)
print(articleSize)

for article in articles:
    #print(article)
    #print(article["description"])
    print(article["title"])
