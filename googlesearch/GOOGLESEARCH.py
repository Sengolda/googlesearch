import bs4
import requests


def search_google(query):
    x = requests.get(f"https://google.com/search?q={query}")
    soup = bs4.BeautifulSoup(x.text,"html.parser")
    return soup.text

print(search_google("lion"))
