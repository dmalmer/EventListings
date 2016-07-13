
from parser import Parser

if __name__ == '__main__':
    with open('./venue_urls') as f:
        venue_urls = [line.strip() for line in f]
    
    for url in venue_urls:
        venue_parser = Parser.factory(url)

        soup = venue_parser.retrieve_soup()
        events = venue_parser.parse_events(soup)


