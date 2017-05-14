STEPS

site_scraper.py
    Uses requests and some other libraries to pull raw data off the site and build it into a CSV. Delimited on | (pipe) as this has the lowest overlap with the raw text. The 8 sightings that had this overlap were cleaned by hand.Produces sightings.csv

clean_data.py
    Removes entries without state, city, or summary data.
    Removes entries with invalid state or city data - specifically for cities any entry with 4+ spaces or non-alphanumeric
    Removes entries with invalid dates.



{'count': 46395, 'no_state': 4690, 'no_city': 38, 'no_summary': 27, 'bad_state': 2507, 'bad_city': 3486, 'error': 0, 'valid': 35647}

extract_terms.py was run to extract only the NN,VB,JJ from cleaned -> cleaned_with_terms.csv with terms delimited by pipes ;

command line python used to generate a list of unique locations

geocode.py contacts Google Geocode API and gets lat/long for each location. this was reshaped into a python dictionary with some quick regex.

build_index.py builds a term:incident index with the data from the csv and the geocodes and saves as json file.

we use a haversine algo package to calculate distnance

