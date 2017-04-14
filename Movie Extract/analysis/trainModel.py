import pandas as pd

MEASURE_DATA = 'graph_info_all.tsv'
CLASS_DATA = 'movie_class.csv'


def combine_measure_class_data(measureCSV, classCSV):
    dataframe = pd.read_csv(MEASURE_DATA, error_bad_lines=False, sep='\t',encoding='latin-1')
    dataframe.set_index
    dataframe_2 = pd.read_csv(CLASS_DATA, error_bad_lines=False, sep=',',encoding='latin-1', header=None)
    for i, row in dataframe.iterrows():
        dataframe.loc[i, "Movie Name"] = dataframe.loc[i, "Movie Name"].replace("_results", "")


    final_df = pd.merge(left=dataframe, right=dataframe_2, how='left', left_on='Movie Name', right_on=0)
    return final_df

if __name__ == "__main__":

    dataframe = combine_measure_class_data(MEASURE_DATA, CLASS_DATA)
