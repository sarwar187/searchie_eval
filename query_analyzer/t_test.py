"""Demonstrates how statistical significance tests can be ran using pytrec_eval."""

import argparse
import os
import scipy.stats
import sys
import pandas as pd
import numpy as np

#file_se = "/home/smsarwar/Desktop/significance/se"
#file_se = "/home/smsarwar/Desktop/significance/prf_all_word"
#file_se = "/home/smsarwar/Desktop/significance/prf_top_k"
#file_se = "/home/smsarwar/Desktop/significance/prf_all_word_rm3"
#file_se = "/home/smsarwar/Desktop/significance/prf_sentence_linear"
#file_se = "/home/smsarwar/Desktop/significance/prf_sentence_exponential"
#file_se = "/home/smsarwar/Desktop/significance/prf_sentence_uniform"
#file_se = "/home/smsarwar/Desktop/significance/prf_sentence_score"
#source = "../data/sentence_embedding_weighted"

file = "t_test_source"
df = pd.read_csv(file, sep='\t', header = None)
input_source = df.as_matrix()

#file_bm25 = "/home/smsarwar/Desktop/significance/bm25"
#destination = "../data/wrapper_adjustment_result"
destination = "t_test_destination"
df_destination = pd.read_csv(destination, sep='\t', header = None)
input_destination = df_destination.as_matrix()

indices = [0,1,2,3,4,5,6,8]
def main():
    for i in np.asarray(indices):
        first_scores= input_destination[:, i]
        second_scores = input_source[:, i]
        #print(first_scores)
        print(scipy.stats.ttest_rel(first_scores, second_scores))

if __name__ == "__main__":
    sys.exit(main())