import pandas as pd
import numpy as np
import os

def get_index_from_list(a, ranked, index):
    if index >= len(a):
        return -1
    while(True):
        if a[index] in ranked:
            index+=1
            if index==len(a):
                return -1
        else:
            break
    return index

def merge_lists(a, b):
    ranked = []
    a_current_index = 0
    b_current_index = 0
    while(True):
        a_current_index = get_index_from_list(a, ranked, a_current_index)
        if a_current_index!=-1:
            ranked.append(a[a_current_index])
            a_current_index+=1

        b_current_index = get_index_from_list(b, ranked, b_current_index)
        if b_current_index !=-1:
            ranked.append(b[b_current_index])
            b_current_index+= 1

        if a_current_index==-1 and b_current_index==-1:
            break
        #print(ranked)
    #print len(ranked)
    return ranked



def write_dictionary_to_file(result_dictionary, transfer_to_flag=False):
    for file_to_transfer in result_dictionary.keys():
        f = open(file_to_transfer, "w+")
        for item in result_dictionary[file_to_transfer]:
            f.write(str(item))
            f.write("\n")
        f.close()
        if transfer_to_flag==True:
            os.system("scp " + file_to_transfer + " smsarwar@sydney.cs.umass.edu:/mnt/nfs/work1/smsarwar/searchie/ltr_sbatch/fold5/test/")

def read_predictions_from_file(file):
    dataframe = pd.read_csv(file, sep="\t", header=None)
    input = dataframe.as_matrix()
    print input.shape
    print input

    print np.unique(input[:, 0]).size
    input_formatted = np.empty(shape=[input.shape[0], 4], dtype=basestring)
    result = {}

    for line in open(file):
        a = line.split("\t")
        if result.has_key(mapping_dictionary[a[0]][0]) == False:
            result[mapping_dictionary[a[0]][0]] = []


    for line in open(file):
        # print line
        a = line.split("\t")
        file = mapping_dictionary[a[0]][0]
        result[file].append(int(mapping_dictionary[a[2]][1]))

    print len(result)
    file_to_rankedlist = {}
    output = "test_item = ["
    for key in result.keys():
        a = key.split("_")
        file_to_transfer = "/home/smsarwar/PycharmProjects/searchie_eval/data/mzdata/result/" + a[0] + "_" + a[
            1] + "_" + '1000' + ".jsonl.gz.result"
        file_to_rankedlist[file_to_transfer] = []
        for item in result[key]:
            file_to_rankedlist[file_to_transfer].append(item)
        #output += "'" + key + ".result', "
    return file_to_rankedlist
    #     input_formatted[i, 0] = mapping_dictionary[input[i, 0]]


os.system("scp smsarwar@goulburn.cs.umass.edu:/mnt/scratch/smsarwar/MatchZoo/data/searchie/ranking/corpus_aquaint_mapping.txt /home/smsarwar/")

mapping_dictionary = {}
file = "/home/smsarwar/corpus_aquaint_mapping.txt"
dataframe = pd.read_csv(file, sep=" ", header=None)
input = dataframe.as_matrix()
print input
for i in np.arange(input.shape[0]):
    mapping_dictionary[input[i,0]] = (input[i,1], input[i,2])

os.system("scp smsarwar@goulburn.cs.umass.edu:/mnt/scratch/smsarwar/MatchZoo/data/searchie/ranking/predict.test.arci_ranking.txt /home/smsarwar/")
average_file = "/home/smsarwar/predict_average.test.arci_ranking.txt"
neural_file = "/home/smsarwar/predict_neural.test.arci_ranking.txt"
current_file = "/home/smsarwar/predict.test.arci_ranking.txt"

ranked_average = read_predictions_from_file(average_file)
ranked_neural = read_predictions_from_file(neural_file)
ranked_current = read_predictions_from_file(current_file)
combined_result = {}

for key in ranked_average:
    list_reural = ranked_neural.get(key)
    list_average = ranked_average.get(key)
    list = merge_lists(list_average, list_reural)
    combined_result[key] = list

write_dictionary_to_file(combined_result, transfer_to_flag=True)
#write_dictionary_to_file(ranked_neural, transfer_to_flag=True)
#write_dictionary_to_file(ranked_average, transfer_to_flag=True)

#write_dictionary_to_file(ranked_current, transfer_to_flag=True)
