import pandas as pd
from sklearn.model_selection import train_test_split

MEASURE_DATA = 'graph_info_all.tsv'
CLASS_DATA = 'movie_class.csv'


def combine_measure_class_data(measureCSV, classCSV):
    '''Combines network measure and action class data into single dataframe'''

    # Load Data
    measure_df = pd.read_csv(MEASURE_DATA, error_bad_lines=False, sep='\t',encoding='latin-1')
    measure_df.set_index
    class_df = pd.read_csv(CLASS_DATA, error_bad_lines=False, sep=',',encoding='latin-1', header=None)

    # Edit movie names for merge IDs
    for i, row in measure_df.iterrows():
        measure_df.loc[i, "Movie Name"] = measure_df.loc[i, "Movie Name"].replace("_results", "")

    # Merge the dataframes
    final_df = pd.merge(left=measure_df, right=class_df, how='left', left_on='Movie Name', right_on=0)

    return final_df

def filter_columns(exclusion_columns, dataframe):
    '''Filters out columns that will not be used in training data'''
    for column in exclusion_columns:
        del dataframe[column]

    return dataframe

def create_train_test(raw_dataframe):
    '''SPLITS RAW TRAINING DATA INTO TRAINING AND PERSONAL TEST DATA'''
    train_df, test_df = train_test_split(raw_dataframe, test_size = 0.2)
    return train_df.reset_index(), test_df.reset_index()

if __name__ == "__main__":

    dataframe = combine_measure_class_data(MEASURE_DATA, CLASS_DATA)
    exclusion_list = [0,"sorted out_degree centrality","sorted in_degree centrality","highest out_degree_node", \
    "highest in_degree node", "closeness_centrality","betweenness centrality","Movie Name"]

    filtered_dataframe = filter_columns(exclusion_list,dataframe)
    train_df, test_df = create_train_test(filtered_dataframe)
    
