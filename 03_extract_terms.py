import nltk
import pickle
import re

RE_NUMSYM = re.compile(r"\d|[-!%^&*()_+|~=`@{}\[\]:\"'<>?,.\/]")

sightings = pickle.load(open('sightings_cleaned.pickle','rb'))

for s in sightings:

    # Extract the summary and tokenize
    tags = nltk.pos_tag( nltk.word_tokenize( s[3] ) )
        
    # Only retain Nouns, Adjectives, and Verbs
    tags = filter( lambda x: x[1] in ['NN', 'JJ', 'VRB'], tags )

    # Build a list from these terms and lowercase them
    tags = list(map( lambda x: str.lower(x[0]), tags ))

    # Remove terms with symbols, numbers
    tags = list(filter(lambda x: not RE_NUMSYM.search(x), tags))

    # Replace the existing block with the tags
    s[3] = tags


file = open('sightings_terms.pickle','wb+')
pickle.dump(sightings, file)
file.close()