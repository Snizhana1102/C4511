import requests

html = requests.get('https://books.toscrape.com/').text

parse_text = html.split('<a href="')

titles = []

for text in parse_text:
  if 'title="' in text:
    title = text.split('title="')[1].split('"')[0]
    titles.append(title)

for i, title in enumerate(titles, 1):
  print(f"{i}. {title}")