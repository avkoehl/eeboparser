import pandas as pd
import re

from eeboparser.locations import locations_blacklist
from eeboparser.locations import single_word_variations
from eeboparser.locations import phrase_variations
from eeboparser.utils import is_roman
from eeboparser.utils import normalize_text
from eeboparser.utils import PUNCT_RE

def clean_meta(meta):
    """ where meta is a list of dicts"""
    #
    # FIELDS:
    #  ids [File_ID, EEBO_Citation, ESTC_ID, Proquest_ID, STC_ID, VID)
    #  Title - keep as is
    #  Publisher - keep as is
    #  Language  - keep as is
    #  Author - normalize text, and apply author specific cleaning
    #  Date - normalize to single 4 digit date if possible
    #  Keywords - aggregate terms
    #  Location - normalize text, and apply location specific normalization

    df = pd.DataFrame.from_records(meta)
    df["Location"] = df["Location"].map(clean_locations)
    df["Date"] = df["Date"].map(clean_dates)
    df["Author"] = df["Author"].map(clean_authors)
    df["Keywords"] = df["Keywords"].map(clean_authors)

    return df.to_records(index=False)

def clean_keywords(keywords):
    """ to be mapped to the keywords column """
    # from the xml - keywords are stored as a list
    # Each element in the list can be a series of associated terms delimited by --
    # for example
    # In [12]: meta["Keywords"][1]
    # Out[12]:
    #    ['Charles --  I, --  King of England, 1600-1649 --  Early works to 1800.',
    #     'Great Britain --  History --  Civil War, 1642-1649 --  Early works to 1800.',
    #     'Great Britain --  Foreign relations --  Scotland --  Early works to 1800.']
    #
    # For our uses we decided to aggregate the keywords, splitting on the --
    # The idea being there seems to be arbitrary variance of the order of related terms
    # and that the same information is captured if they are aggregated
    # Two things to note: first duplicates are removed such as Early works to 1800
    # and second for whatever reason the cataloguers put the regnal number after a double dash
    # so we work to attach that back to the monarch's name as a single keyword

    # split on --, find roman numerals and attach to index before
    # remove duplicates
    flat = "--".join(keywords)
    terms = flat.split('--')
    terms = [t.strip() for t in terms]

    cleaned = []
    index = 0
    for term in terms:
        if is_roman(term) and index != 0:
            cleaned[index-1] = cleaned[index-1] + " " + term
        else:
            cleaned.append(term)
            index += 1
    return list(set(cleaned))
    

def clean_locations(location):
    """ to be mapped to the locations column """

    def word_mapping(word):
        if word in locations_blacklist:
            return ""
        if word in single_word_variations:
            return single_word_variations[word]
        return word

    location = normalize_text(location)

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
        if len(d) == 4 and "/" not in d and int(d) > 1400 and int(d) < 1850:
            clean_date = d
            break
        if len(d) == 5 and "/" in d:
            d = d[0:4]
            if int(d) > 1400 and int(d) < 1850:
                clean_date = d
                break
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

        # normalize
        author = normalize_text(author)

        # remove extraneous expressions (not sure if necessary)
        blacklist = ["fl", "of", "or", "aut", "de", "d",
                "ca", "attributed", "name"]
        author = author.split()
        author = ' '.join([w for w in author if w not in blacklist])
        author = author.strip()

        cleaned_authors.append(author)

    return cleaned_authors
