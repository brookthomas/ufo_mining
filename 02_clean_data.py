"""
    CSV Columns: datetime,city,state,shape,duration,summary,posted
"""
import re
import pickle
import datetime

VALID_STATES = ["AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL",
                "IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE",
                "NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD",
                "TN","TX","UT","VT","VA","WA","WV","WI","WY"]

# Characters that make a potential city/state invalid
RE_NONALPHA = re.compile(r"\d|[!$%^&*()_+|~=`@{}\[\]:\";'<>?,\/]")

# The earliest date we will allow sightings for
EARLIEST_DATE = datetime.date(1979,1,1)

sightings = []

logs = {
    'count': 0,
    'no_state':0,
    'no_city':0,
    'no_summary': 0,
    'bad_state':0,
    'bad_city':0,
    'malformed_date':0,
    'invalid_date':0,
    'error':0,
    'valid':0
}

# Read file into memory
with open('sightings.csv') as f:
    for line in f.readlines():

        logs['count'] += 1

        try:
            line = line.strip().split('|')

            ## MISSING DATA ##

            # Skip entries with no state data
            if line[2] == '':
                logs['no_state'] += 1
                continue

            # Skip entries with no city data
            if line[1] == '':
                logs['no_city'] += 1
                continue

            # Skip entries with no summary data
            if line[5] == '':
                logs['no_summary'] += 1
                continue

            ## INVALID DATA ##

            # Skip entries with non-US state
            if str.upper(line[2]) not in VALID_STATES:
                logs['bad_state'] += 1
                continue

            # Skip entries with suspect invalid cities
            if len(line[1].split(' ')) > 3 or RE_NONALPHA.search(line[1]):
                logs['bad_city'] += 1
                continue

            # Build raw date into datetime object
            # The dates are mm/dd/yy so we need to account for 1900s or 2000s
            date = line[0].split(' ')[0].split('/')
            date = [i for i in map(int,date)]
            year = (2000 + date[2]) if date[2] < 17 else (1900 + date[2])

            try:
                date = datetime.date(year, date[0], date[1])
            except:
                logs['malformed_date'] += 1
                continue

            # Ensure date is >= EARLIEST_DATE
            if date < EARLIEST_DATE:
                logs['invalid_date'] += 1
                continue

            ## LIKELY VALID ##
            sightings.append([date, line[1], line[2], line[5]])
            logs['valid'] += 1

        except:
            logs['error'] += 1
            continue


file = open('sightings_cleaned.pickle', 'wb+')
pickle.dump(sightings, file)
file.close()

print(logs)