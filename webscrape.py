import requests

r = requests.get('https://www.csun.edu/calendar-events/day/9321/2018-09-17')
# print(r.text[0:500])

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

names = soup.find_all('span', attrs={'class': 'views-field views-field-title'})
starts = soup.find_all('span', attrs={'class': 'date-display-start'})
ends = soup.find_all('span', attrs={'class': 'date-display-end'})

named = []
started = []
ended = []
for name in names:
    name = name.find('a').text[0:]
    named.append(name)
for start in starts:
    start = start.contents[0]
    started.append(start)
for end in ends:
    end = end.contents[0]
    ended.append(end)

print(named)
print(started)
print(ended)


