import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=gRLHr664tXA"

result =requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")

p = soup.find_all("p")

print(p)

