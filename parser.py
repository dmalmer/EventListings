
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

from event import Event
from util import determine_year

# Parser superclass and factory
class Parser:
    def __init__(self, venue, url):
        self.venue = venue
        self.url = url


    def retrieve_soup(self):
        return BeautifulSoup(urlopen(self.url).read().decode('utf-8'), 'lxml')


    def parse_events(self, event_html):
        # parse out event title, date, and time from chunk of html
        raise Exception('Undefined parse_event function in Parser subclass')


    def band_names_from_title(self, title):
        # determine individual band names from an event title
        #  search over database of band names?
        #  generate list of band names from songkick?
        return None


    def retrieve_sample(self, band_name):
        # retrieve a soundcloud or youtube sample from the band(s)
        # will require parsing out the band names from the event title
        # --find giant list of band names to search over?
        return None


    @staticmethod
    def factory(url):
        if 'flourcitystation.com' in url:
            return FlourCityStationParser('Flour City Station', url)
        elif 'bugjar.com' in url:
            return BugJarParser('Bug Jar', url)
        elif 'dinosaurbarbque.com' in url:
            return DinosaurBBQParser('Dinosaur BBQ', url)
        elif 'rochester.edu/Eastman' in url:
            return EastmanParser('Eastman School of Music', url)
        else:
            raise Exception('Missing parser for: {}'.format(url))


# Venue subclasses
class FlourCityStationParser(Parser):
    def parse_events(self, soup):
        events = []
        for li in soup.find_all('li', 'twistercontent'):
            title = li.find('h5', 'cro_cust_font').string
            details_page = li.find('div', 'clarlabel').a['href']

            day = li.find('span', 'first').string
            month = li.find('span', 'second').string
            time = li.find('span', 'cro_foodprice').string
            dt = datetime.strptime('{} {} {}'.format(month, day, time), '%b %d %I:%M %p')
            dt = dt.replace(year=determine_year(dt))

            events.append(Event(self.venue, title, [], dt, details_page)) 
        return events


class BugJarParser(Parser):
    def parse_events(self, soup):
        events = []
        cal = soup.find('div', 'gigs-calendar')
        for tr in cal.find_all('tr'):
            a = tr.find('a')
            title = a.string
            details_page = a['href']

            datestr = tr.find('td', 'date').string
            time = tr.find('td', 'time').string 
            dt = datetime.strptime('{} {}'.format(datestr, time), '%m/%d/%y %I:%M%p')

            events.append(Event(self.venue, title, [], dt, details_page)) 
        return events


class DinosaurBBQParser(Parser):
    def parse_events(self, soup):
        events = []
        for div in soup.find_all('div', 'seven columns'):
            title = div.find('h1').string

            datestr = div.find_all('span')[1].string
            dt = datetime.strptime(datestr, '%B %d, %Y | %I%p')

            events.append(Event(self.venue, title, [], dt, self.url)) 
        return events


class EastmanParser(Parser):
    def parse_events(self, soup):
        events = []
        for chunk in soup.find_all('div', 'Event'):
            a = chunk.find('a')
            title = a.string

            datestr = a['href'].split('from=')[1].split('&')[0]
            timestr = chunk.find('div', 'EventTime').string
            try:
                dt = datetime.strptime('{} {}'.format(datestr, timestr), '%d%B%Y %I:%M %p')
            except ValueError:
                #for empty time fields
                dt = datetime.strptime(datestr, '%d%B%Y')
            
            events.append(Event(self.venue, title, [], dt, self.url)) 
        return events


