import pandas as pd
import ast
from eeboparser import clean_meta

meta = pd.read_csv("./data/meta.csv", dtype={'Locations': str})
meta['Keywords'] = meta['Keywords'].apply(lambda x: ast.literal_eval(x))

    # TODO verify results with value_counts and nunique, and comparisons
    # such as print all the original values that mapped to london...
