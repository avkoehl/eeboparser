import pandas as pd
import re

from eeboparser.locations import locations_blacklist
from eeboparser.locations import single_word_variations
from eeboparser.locations import phrase_variations

PUNCT_RE = r'[\[\]\|!"#$%&\'()*+,./:;<>?@\^_`{|}~]'

def clean_meta(meta):
    """ where meta is a list of dicts"""
    # keywords, Language already normalized
    # TODO: keywords need to be split on --
    # really just Date, Author, Locations

    df = pd.DataFrame.from_records(meta)
    df["Location"] = df["Location"].map(clean_locations)
    df["Date"] = df["Date"].map(clean_dates)
    df["Author"] = df["Author"].map(clean_authors)

    # TODO verify results with value_counts and nunique, and comparisons
    # such as print all the original values that mapped to london...
    return df.to_records(index=False)

def clean_locations(location):
    """ to be mapped to the locations column """

    def word_mapping(word):
        if word in locations_blacklist:
            return ""
        if word in single_word_variations:
            return single_word_variations[word]
        return word

    location = location.lower() # set to lower

    location = re.sub(r'\d+', '', location) # remove digits
    location = re.sub(PUNCT_RE, '', location) # remove punctuation
    location = re.sub(r'\s\s+', ' ', location)  # Handle excess whitespace
    location = location.strip()  # No whitespace at start and end of string

    location = location.split()
    location = ' '.join([word_mapping(w) for w in location])
    location = location.split()
    location = ' '.join(location)

    # then phrases (without stopwords)
    if location in phrase_variations:
        location = phrase_variations[location]

    # remove ie at beginning and end of location (e.g "ie london ie")
    location = re.sub('^ie ', '', location)
    location = re.sub(' ie$', '', location)
    location = location.strip()
    return location

def clean_dates(date):
    """ to be mapped to dates column """

    # remove non digits and spaces and dashes and slashes
    t = date
    date = str(date)
    date = re.sub("[^0-9 \/\\-]", "", date)
    date = date.replace("-", " ")
    dates = date.split()

    # TODO look for tri-dates (three digit dates)
    # TODO add Sam's manual corrections

    # loop through
    # once a 4 diit number is reached, keep that as the date
    # note that this keeps the first one, e.g in a date range
    # if 5 digits and has a / such as 1545/6 keep the first 4 digits
    # so that the date would be 1545
    clean_date = ""
    for d in dates:
        if len(d) == 4:
            clean_date = d
            break
        if len(d) == 5 and d.contains("/"):
            clean_date = date[0:4]
    return clean_date
    
def clean_authors(authors):
    """ to be mapped to authors column """

    cleaned_authors = []
    # split on authors
    # for each:
    for author in authors:
        # remove non capital words
        words = author.split()
        author = " ".join([w for w in words if w[0].isupper()])
        author = author.lower()

        # remove digits and punct
        author = re.sub(r'\d+', '', author) # remove digits
        author = re.sub(PUNCT_RE, '', author) # remove punctuation
        author = re.sub(r'\s\s+', ' ', author)  # Handle excess whitespace
        author = author.strip()  # No whitespace at start and end of string

        # remove extraneous expressions (not sure if necessary)
        blacklist = ["fl", "of", "or", "aut", "de", "d",
                "ca", "attributed", "name"]
        author = author.split()
        author = ' '.join([w for w in author if w not in blacklist])
        author = author.strip()

        cleaned_authors.append(author)

    return cleaned_authors
