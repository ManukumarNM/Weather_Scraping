# Requests module allows you to send HTTP/1.1 requests quite easily
import requests 

# BeautifulSoup library scrap information from web pages
from bs4 import BeautifulSoup as bs

weathersearch_city = "weather in Bangalore"

# The web page you are trying to get store it in url variable
url = f"https://www.google.com/search?&q={weathersearch_city}"

# Now, let’s try to get a webpage and store it in response variable
res = requests.get(url).content

# getting raw data -> It will parse all the html content
soup = bs(res,"html.parser")

# Soup will return a heap of data with HTML tags from that take classes
# print(soup) 
results = soup.find("div", class_="BNeawe").text

# results = soup.find("div", class_="BNeawe s3v9rd vvjwJb AP7Wnd").text
print("######################################")

print("The Bangalore Temperature is -", results)

print("######################################")

# Complete code without comments

# import requests 
# from bs4 import BeautifulSoup as bs
# weathersearch_city = "weather in Bangalore"
# url = f"https://www.google.com/search?&q={weathersearch_city}"
# res = requests.get(url).content
# soup = bs(res,"html.parser")
# results = soup.find("div", class_="BNeawe").text
# print("The Bangalore Temperature is -", results)
