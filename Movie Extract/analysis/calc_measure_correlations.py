# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
import time
import sys
from scipy.stats.stats import pearsonr

TEST_DATA = 'test_data.csv'
MASTER_FILE = 'master_file.csv'

'''
Calculates correlations between screen transition network metrics and movie generes

A valid master file contains at least one pair consisting of Scene Transition Network Metric AND a Movie Genre

Sample Scene Transition Network Metric Column(s):
    - Average Degree Connectivtiy
    - Global Clustering Coefficient
    - Average Shortest Path

Movie Genre:
    - One Genre Column (Binary)
    - Multi-genre Column (Int - coded genre)
'''

# LOAD THE MASTER CSV FILE INTO PANDAS DATAFRAME
def load_master_file(master_data_file):
	master_df = pd.read_csv(master_data_file, error_bad_lines=False, encoding='latin-1',header=0)
	return master_df


#Calculates the pearson coefficient between a genre_column and a Scene Transition Network Metric column
#  data_file = a pandas dataframe (pandas df)
#  target_column = the column name of the dependent variables (string)
#  network_metric_columns =
#  output_path =  the intended path and name of the output file (string)
def calc_correlations(dataframe, genre_column, network_metric_columns, output_path=None):
    target_df = dataframe[genre_column]

    correlations = {}
    index = 0

    for column in network_metric_columns:
        try:
            trimmed_df = dataframe.filter(items=[genre_column, column])
            trimmed_df = trimmed_df[np.isfinite(trimmed_df[genre_column])]
            trimmed_df = trimmed_df[np.isfinite(trimmed_df[column])]
            trimmed_df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
            correlations[genre_column + '_|_' + column ] = pearsonr(trimmed_df[genre_column],trimmed_df[column])
        except:
            print "Error calculating correaltion"
        index += 1

    # Option: Print Correlations to CSV
    if output_path:
        with open(output_path, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Variable", "pearson", "p-value"])
            for key, value in correlations.items():
                writer.writerow([key, value[0],value[1]])

    return correlations


if __name__ == "__main__":
    master_df = load_master_file(TEST_DATA)
    print "Data Loaded"
    calc_correlations(master_df,'action',['average_shortest_path','clustering_coefficient']),output_path='test_analysis.csv')
