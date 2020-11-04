import pandas as pd
import re

import ..cleaning_lists.locations_blacklist
import ..cleaning_lists.

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

    location = location.lower() # set to lower

    location = re.sub(r'\d+', '', location) # remove digits
    location = re.sub(PUNCT_RE, '', location) # remove punctuation
    location = re.sub(r'\s\s+', ' ', location)  # Handle excess whitespace
    location = location.strip()  # No whitespace at start and end of string


    # remove unwanted terms (stopwords, prepositions, variations of printed)
    blacklist = [
            "i", "a\'i", "printed", "prynted", "imprinted", "enprynted", "imprynted",
            "imprented", "imprentit", "excusum", "printiedig",
            "anno domini", "anno", "are", "for", "of", "within", "by", "at",
            "printio", "the", "and", "in", "sic", "re", "im", "jm", "er", "em", "an", 
            "yn", "en", "a", "ad", "briniwyd", "brintio", "brio"]

    location = location.split()
    location = ' '.join([x for x in location if x not in blacklist])
    location = location.strip()

    # then single word mapping
    # then phrases (without stopwrods)
    # then the ie londons (ie single word)

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
