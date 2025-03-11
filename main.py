import requests
import bs4

result = requests.get("http://www.example.com")

print(result.text) # in the past this would put a raw string not a beautifully organized string

soup = bs4.BeautifulSoup(result.text, "lxml")

print(soup.select('p')[0])

print(soup.select('title'))
