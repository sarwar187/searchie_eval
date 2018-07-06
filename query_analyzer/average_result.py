import os
import pandas as pd
from os.path import isfile, join
import numpy as np
import sys
import scipy.stats

dirname = "../data"
files = [join(dirname, file) for file in os.listdir(dirname) if isfile(join(dirname, file))]

indices = [1,2,4,5,6,7]

#sourcefile = "../data/bm25"
sourcefile = "../data/sentence_embedding_weighted"

df = pd.read_csv(sourcefile, sep='\t', header=None)
source_input = df.as_matrix()

for file in files:
    print file
    df = pd.read_csv(file, sep='\t', header=None)
    input = df.as_matrix()
    output = np.average(input[:, indices], axis=0)
    output = np.round(output.astype(np.double), decimals=3)
    result = "& "
    for i in output:
        result += str(i)
        if i!= len(output)-2:
            result+= " & "
    print result

    for i in np.asarray(indices):
        first_scores= input[:, i]
        second_scores = source_input[:, i]
        print scipy.stats.ttest_rel(first_scores, second_scores)