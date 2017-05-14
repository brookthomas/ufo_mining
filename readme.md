STEPS

01_site_scraper.py
    Uses requests and some other libraries to pull raw data off the site and build it into a CSV. Delimited on | (pipe) as this has the lowest overlap with the raw text. The 8 sightings that had this overlap were cleaned by hand.Produces sightings.csv

02_clean_data.py
    Removes entries without state, city, or summary data.
    Removes entries with invalid state or city data - specifically for cities any entry with 4+ spaces or non-alphanumeric
    Removes entries with invalid dates.

    {'count': 46395, 'bad_city': 3486, 'no_city': 38, 'valid': 35647, 'invalid_date': 0, 'error': 0, 'malformed_date': 0, 'bad_state': 2507, 'no_summary': 27, 'no_state': 4690}

    Outputs file sightings_cleaned.pickle

03_extract_terms.py
    Uses nltk to extract nouns, adjectives, and verbs from the summary - discarding all others.

04_build_index.py
    Rebuilds the data into a term:position index, such that for a given term we have a listing of all sightings associated with that term.

05_analyze.py
    Uses a pearsons correlation coefficient to look for a correlation between distance from first sighting and time from first sighting.
    Distance is calculated using the haversine algorithm for finding the distance in miles between two Geographic Coordinates.

