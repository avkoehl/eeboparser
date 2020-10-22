import pandas as pd
import re

PUNCT_RE = r'[\[\]\|!"#$%&\'()*+,./:;<=>?@\^_`{|}~]'

def clean_meta(meta):
    """ where meta is a list of dicts"""
    # keywords, Language already normalized
    # really just Date, Author, Locations

    df = pd.DataFrame.from_records(meta)
    df["Location"] = df["Location"].map(clean_locations)
    df["Date"] = df["Date"].map(clean_dates)
    df["Author"] = df["Author"].map(clean_authors)
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

        # additional cleaning TODO from https://github.com/datalab-dev/quintessence_corpus/blob/master/meta_cleaning.R#L206
        cleaned_authors.append(author)

    return cleaned_authors
