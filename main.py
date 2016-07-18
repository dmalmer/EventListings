
from parser import Parser
from util import output_html

if __name__ == '__main__':
    with open('./venue_urls') as f:
        venue_urls = [line.strip() for line in f if line[0] != '#']
    
    all_events = []
    for url in venue_urls:
        print('Parsing', url)
        venue_parser = Parser.factory(url)

        soup = venue_parser.retrieve_soup()
        all_events.extend(venue_parser.parse_events(soup))

    output_html(all_events, './shows.html')

