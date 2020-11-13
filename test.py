import pandas as pd
import ast

from eeboparser.clean_meta import clean_keywords
from eeboparser.clean_meta import clean_authors
from eeboparser.clean_meta import clean_dates
from eeboparser.clean_meta import clean_locations

meta = pd.read_csv("./data/meta.csv", dtype={'Location': str})
meta = meta[["Author", "Language", "Date", "Keywords", "Location"]]
meta['Keywords'] = meta['Keywords'].apply(lambda x: ast.literal_eval(x))
meta['Author'] = meta['Author'].apply(lambda x: ast.literal_eval(x))
meta['Language'] = meta['Language'].apply(lambda x: ast.literal_eval(x))
meta["Location"] = meta["Location"].astype(str)

k = meta["Keywords"].map(clean_keywords)
a = meta["Author"].map(clean_authors)
l = meta["Location"].map(clean_locations)
d = meta["Date"].map(clean_dates)

    # TODO verify results with value_counts and nunique, and comparisons
    # such as print all the original values that mapped to london...

# Keywords
keywords = pd.concat([meta["Keywords"],k], axis=1)

# Authors
authors = pd.concat([meta["Author"], a], axis=1)

# Location
location = pd.concat([meta["Location"], l], axis=1)

# Date
date = pd.concat([meta["Date"], d], axis=1)
