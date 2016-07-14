
from parser import Parser

if __name__ == '__main__':
    with open('./venue_urls') as f:
        venue_urls = [line.strip() for line in f]
    
    #TODO: create database for event entries
    all_events = []
    for url in venue_urls:
        print('Parsing', url)
        venue_parser = Parser.factory(url)

        soup = venue_parser.retrieve_soup()
        all_events.extend(venue_parser.parse_events(soup))

    for event in sorted(all_events):
        print(event)

