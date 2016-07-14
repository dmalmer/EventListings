

class Event:
    def __init__(self, venue, title, bands, datetime, details_page):
        self.venue = venue
        self.title = title
        self.bands = bands
        self.datetime = datetime
        self.details_page = details_page
        self.sample_links = []


    def __lt__(self, other):
        return self.datetime < other.datetime
    

    def __str__(self):
        return '{}: {} - {}'.format(self.datetime.isoformat(' '), self.venue, self.title)

