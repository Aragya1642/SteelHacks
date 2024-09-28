# code to import bs4
from bs4 import BeautifulSoup
import requests, time, json
from dateutil.parser import parse


# main code to get reques object
def get_request(url):
  response = requests.get(url)
  return response

# main code to get soup object
def get_soup(response: requests.models.Response) -> BeautifulSoup:
  soup = BeautifulSoup(response.text, 'html')
  return soup


# find all cards
def filter_cards(soup: BeautifulSoup) -> list:
  out = soup.find_all("div", class_="em-card_text")
  return out

def parse_date(date):
  return parse(date)

# from a div, find em-card-text class and return the text
def find_data_by_class(soup: BeautifulSoup):
  # gets title and url
  event_title = soup.find("h3", class_="em-card_title")
  if not event_title: return None

  for a in event_title.find_all('a', href=True):
    url = a['href']

  event_title = event_title.text.strip()
  ########################################################
  # gets date and location
  text = soup.find_all("p", class_="em-card_event-text")
  if len(text) >= 2:
    date, location = text[0], text[1]
    location = location.get_text().strip()
  else:
    date = text[0]
    location = None

  date = date.get_text().strip()
  if "am" in date or "pm" in date:
    date = " ".join(date.split(" ")[0:5])

  date = parse_date(date.strip())
  ########################################################
  # gets url
  return event_title, date, location, url

def export_json(data: dict, filename: str):
  with open(filename, 'w') as f:
    json.dump(data, f)


if __name__ == '__main__':
  output = [] 

  for i in range(2, 4):
    url = f'https://calendar.pitt.edu/calendar/{i}'

    response = get_request(url)

    print(url)

    soup = get_soup(response)

    cards = filter_cards(soup)
    for id, card in enumerate(cards):
      title, date, location, url = find_data_by_class(card)
      output.append({"id": id, "event data:" : {"title": title, "date": str(date), "location": location, "url": url}})    
  export_json(output, 'testing_output.json')