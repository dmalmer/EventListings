
from datetime import datetime

# Determine the most likely year for a datetime object with only month/day set. Choose the year of the next time that 
# month will occur. Eg.: in Nov '16, Dec likely refers to '16 and Jan likely refers to '17.
def determine_year(new_datetime):
    curr_datetime = datetime.now()
    curr_val = curr_datetime.month*100 + curr_datetime.day
    new_val = new_datetime.month*100 + new_datetime.day

    if new_val >= curr_val:
        return curr_datetime.year
    else:
        return curr_datetime.year + 1


def output_html(all_events, filename):
    with open(filename, 'w') as f:
        f.write('<center>\n'
                '<table style="width:90%; border-collapse:collapse" border="1">\n'
                '<col width="90">'
                '<col width="15%">'
                '<tr>\n'
                '   <th align="center">Date</th>\n'
                '   <th align="center">Venue</th>\n'
                '   <th align="center">Show</th>\n'
                '</tr>\n')
        for event in sorted(all_events):
            f.write('<tr>\n'
                    '   <td align="center">{0}</th>\n'
                    '   <td align="center"><a href="https://www.google.com/maps/search/{1}, Rochester, NY">{1}</a></th>\n'
                    '   <td style="padding-left:5px;padding-right:5px;"><a href="{2}">{3}</a></th>\n'
                    '</tr>\n'.format(event.datetime.strftime('%a, %-m/%d %-I:%M%p'), event.venue, event.details_page, event.title))
        f.write('</table>\n'
                '</center>\n')
