import pandas as pd
import numpy as np
from sklearn.svm import SVC
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

    # Removes columns from dataframe that are in exclusion list
    for column in exclusion_columns:
        del dataframe[column]

    return dataframe

def create_train_test():
    '''SPLITS RAW TRAINING DATA INTO TRAINING AND PERSONAL TEST DATA'''

    #Combines the two data files together
    dataframe = combine_measure_class_data(MEASURE_DATA, CLASS_DATA)

    # Exclusion list of non-numeric data columns
    exclusion_list = [0,"sorted out_degree centrality","sorted in_degree centrality","highest out_degree_node", \
    "highest in_degree node", "closeness_centrality","betweenness centrality","Movie Name"]

    # Filters dataframe using exclusion list
    filtered_dataframe = filter_columns(exclusion_list,dataframe)

    #Breaks master datarame into training and test data
    train_df, test_df = train_test_split(filtered_dataframe, test_size = 0.2)

    return train_df.reset_index(), test_df.reset_index()

def train_svm_model(training_df):
    X = []
    for column in training_df:
        X.append(training_df[column].tolist())
    length = len(X)
    y = X[length-1:][0]
    X = X[:length-1]

    X_final = []
    for i in range(0,len(X[0])):
        new_list = []
        for sublist in X:
            new_list.append(float(sublist[i]))
        X_final.append(new_list)
    clf = SVC()
    clf.fit(np.array(X_final), np.array(y))
    return clf

def svm_predict(model, test_df):
    X = []
    for column in test_df:
        X.append(test_df[column].tolist())
    length = len(X)
    y = X[length-1:][0]
    X = X[:length-1]

    X_final = []
    for i in range(0,len(X[0])):
        new_list = []
        for sublist in X:
            new_list.append(float(sublist[i]))
        X_final.append(new_list)
    print X_final[0]

    results = model.predict(np.array(X_final))

    return results

if __name__ == "__main__":


    train_df, test_df = create_train_test()

    svm = train_svm_model(train_df)

    results = svm_predict(svm, test_df)
    print results
    print test_df[1].tolist()
