# code to import bs4
from bs4 import BeautifulSoup
import requests
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
def find_data_by_class(soup):
  event_title = soup.find("h3", class_="em-card_title")
  if not event_title: return None
  event_title = event_title.text.strip()
  date = soup.find("p", class_="em-card_event-text").get_text().strip()
  # if date contains am or pm, then split date and time
  if "am" in date or "pm" in date:
    date = " ".join(date.split(" ")[0:5])
    print(date)

  date = parse_date(date.strip())
  return event_title, date


if __name__ == '__main__':
  url = 'https://calendar.pitt.edu/calendar/'
  response = get_request(url)
  soup = get_soup(response)
  cards = filter_cards(soup)

  for card in cards:
    title, date = find_data_by_class(card)
    print(f"{title} - {date}")
    input()