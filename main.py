import requests
from send_email import send_email

api_key = "af5753fe4c814362a643c9deefaaf072"
topic = "tesla"

url = (f"https://newsapi.org"
       f"/v2/everything?"
       f"q={topic}&"
       f"from=2025-05-20&"
       f"sortBy=publishedAt&"
       f"apiKey={api_key}&language=en")

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
# }

request = requests.get(url)
content = request.json()
articles = content["articles"]
articleSize = len(content["articles"])

#articleTitleList = []
#articleDescriptionList = []

#print(articles)
#print(articleSize)

# for article in articles:
#     #print(article)
#     #print(article["title"])
#     articleTitleList.append(article["title"])
#     articleDescriptionList.append(article["description"])
#     #print(article["description"])
#
# #print(articleTitleList)


message_body = ""

for article in articles[:5]:
    title = article.get("title", "No Title")
    description = article.get("description", "No Description")
    url = article.get("url")
    message_body += f"Title: {title}\nDescription: {description}\n {url} \n\n"

message = f"""\
Subject: Daily News for You!

{message_body}
"""

#print(message)
send_email(message)


