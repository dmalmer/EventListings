
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

