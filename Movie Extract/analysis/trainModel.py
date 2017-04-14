import pandas as pd

DATA = 'graph_info_all.tsv'


dataframe = pd.read_csv(DATA, error_bad_lines=False, sep='\t',encoding='latin-1')

print dataframe.set_index
