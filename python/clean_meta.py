import pandas as pd
import re

PUNCT_RE = r'[\[\]\|!"#$%&\'()*+,./:;<=>?@\^_`{|}~]'

def clean_meta(meta):
    """ where meta is a list of dicts"""
    df = pd.DataFrame.from_records(meta)
    df["Location"].map(clean_locations)
    df["Date"].map(clean_dates)
    df["Author"].map(clean_authors)
    df["Keywords"].map(clean_keywords)
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
            "printed", "prynted", "imprinted", "enprynted", "imprynted",
            "imprented", "imprentit", "excusum", "printiedig",
            "anno domini", "anno", "are", "for", "of", "within", "by", "at",
            "the", "and", "in", "sic", "re", "im", "jm", "er", "em", "an", 
            "yn", "en", "a"]

    location = location.split()
    location = ' '.join([x for x in location if x not in blacklist])
    location = location.strip()

    # TODO: add manual mapping of locations based on Sam's corrected spelling list

    return location

def clean_dates(date):
    """ to be mapped to dates column """
    
def clean_authors:(author):
    """ to be mapped to authors column """

def clean_keywords: (keywords):
    """ to be mapped to keywords column """


