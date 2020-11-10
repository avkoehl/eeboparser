import pandas as pd
import ast

from eeboparser.clean_meta import clean_keywords
from eeboparser.clean_meta import clean_authors
from eeboparser.clean_meta import clean_dates

meta = pd.read_csv("./data/meta.csv", dtype={'Locations': str})
meta = meta[["Author", "Language", "Date", "Keywords"]]
meta['Keywords'] = meta['Keywords'].apply(lambda x: ast.literal_eval(x))
meta['Author'] = meta['Author'].apply(lambda x: ast.literal_eval(x))
meta['Language'] = meta['Language'].apply(lambda x: ast.literal_eval(x))

k = meta["Keywords"].map(clean_keywords)
a = meta["Author"].map(clean_authors)
d = meta["Date"].map(clean_dates)


    # TODO verify results with value_counts and nunique, and comparisons
    # such as print all the original values that mapped to london...
