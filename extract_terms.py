import nltk
import re

re_numsym = re.compile(r"\d|[-!%^&*()_+|~=`@{}\[\]:\"'<>?,.\/]")

out = open('cleaned_with_terms.csv','w+')

with open('cleaned.csv') as f:
    for line in f.readlines():

        line = line.strip()

        try:

            summary = line.split('|')[-2]

            tags = nltk.pos_tag( nltk.word_tokenize( summary ) )
            
            # Only retain Nouns, Adjectives, and Verbs
            tags = filter( lambda x: x[1] in ['NN', 'JJ', 'VRB'], tags )

            # Build a list from these terms and lowercase them
            tags = map( lambda x: str.lower(x[0]), tags )

            # Remove terms with symbols, numbers
            tags = filter(lambda x: not re_numsym.search(x), tags)

            tags = ';'.join(tags)

            out.write(line + '|' + tags + '\n')
        except:
            print('Skipping : {}', line)
            continue