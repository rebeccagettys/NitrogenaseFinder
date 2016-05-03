import pickle
import sys
from distance import levenshtein
from gene_finder import *
import time

from load import load_metagenome
metagenome = load_metagenome()

# pauls_seq = 'GCCCGGACATTCTACATCTCCGCGAAAACACACACTTTTTCGTCTCCGGCGAAGCTTGGCACGCTCGTTGCAAAACAGGGATCAGCAAGGCGAGGGATGGTTGGCCGAGCAGTTACTGCAAAGGGCAACGTCCGCATCTGAGCCGTGCGACGGTTTTGAACGGAAGAAGGCTGCGCCTCGGCGCAAATCGATCAAGCGGCATTAGGTCAACGGAGAGAAAACATGGCACTTCGGCAAATCGCATTCTACGGCAAGGGCGGCATCGGCAAGTCGACCACCTCGCAGAACACCCTCGCGGCGCTGGTTGAGATGGGTCAGAAGATCCTGATCGTCGGCTGCGACCCCAAGGCGGACTCCACCCGTCTGATCCTCAACACCAAGATGCAGGACACGGTGCTGAGCCTCGCCGCGGAAGCGGGTTCGGTGGAAGACCTCGAACTCGAAGACGTGATGAAGATCGGCTACAAGGGCATCAAGTGCACCGAAGCCGGTGGCCCGGAGCCGGGCGTCGGCTGCGCCGGCCGCGGCGTTATCACCGCGATCAACTTCCTCGAAGAAAACGGCGCCTATGAAGACGTCGACTACGTCTCCTACGACGTGCTCGGCGACGTGGTGTGCGGCGGCTTCGCGATGCCGATCCGTGAAAACAAGGCGCAGGAAATCTACATCGTCATGTCCGGCGAGATGATGGCGCTGTATGCCGCCAACAACATCTCCAAGGGCATTCTGAAGTACGCTTCGTCGGGCGGCGTCCGTCTCGGCGGCCTGATCTGCAACGAGCGCCAGACCGACCGCGAGCTCGACCTCGCCGAAGCGCTGGCCAAGAAGCTGAACTCGAAGCTGATCCACTTCGTGCCGCGCGACAATATCGTGCAGCACGCCGAGCTGCGCCGCCAGACCGTGATCCAGTACGCGCCCGACAGCCAGCAGGCTAAGGAATATCGCGCCCTGGCCAACAAGGTCCATGCCAACTGCGGCAACGGCACCATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGCTCGACTTCGGCATCATGAAGACCGAGGAGCAGCAGCTCGCCGAGCTCGCCGCCAAGGAAGCCGCCAAGGCGGCCGCGTCCGCCTGATCGCATCAGCCAGGCCGGTCGCCTAGCGCGACCGGCCGCCATCCCGGCGGCCCCAGACACGAGGAACAACGATGAGCACCGCAGTCGCAGAATCCCCCGCGGACATCAAGGAACGTAACAAGAAGCTGATCGGCGAAGTCCTGGAGGCCTATCCGGACAAGTCGGCCAAGCGTCGCGCCAAGCATCTCAACACGTACGACGCCGAGAAGGCGGAGTGCTCGGTCAAGTCCAACATCAAGTCGATCCCGGGCGTGATGACGATCCGCGGTTGCGCCTACGCCGGCTCGAAGGGCGTGGTGTGGGGCCCGATCAAGGACATGGTCCACATCAGCCACGGCCCGGTCGGCTGCGGCCAGTATTCGTGGGGTTCGCGCCGCAACTATTACAAGGGAACCACCGGCGTCGACACTTTCGGCACGATGCAGTTCACCTCCGACTTCCAGGAGAAGGACATCGTTTTCGGCGGTGACAAGAAGCTCGGCAAGATCATCGACGAGATCCAGGAGCTGTTCCCGCTCTCCAAGGGCATCTCGGTGCAGTCGGAATGCCCGATCGGTCTGATCGGCGACGACATCGAGGCGGTCTCCAAGGCCAAGTCGAAGCAGTATGACGGCAAGCCGATCATCCCGGTCCGCTGCGAAGGCTTCCGCGGCGTGTCGCAGTCGCTCGGCCACCACATCGCCAACGACGTGATCCGTGACTGGGTGTTCGACAAGGCCGCCGAGAAGAACGCCGGCTTCCAGTCGACCCCCTACGACGTCGCGATCATCGGCGACTACAACATCGGCGGCGATGCCTGGGCCTCGCGCATCCTGCTCGAGGAAATGGGCCTCCGCGTGATCGCGCAGTGGTCCGGCGACGGCACCATCGCGGAGCTGGAGAACACCCCGAAGGCGAAGCTGAACATCCTGCACTGCTACCGCTCGATGAACTACATCACGCGGCACATGGAAGAGAAGTTCGGTATTCCGTGGGTTGAATACAACTTCTTCGGCCCGTCCAAGATCGA'

#Loading the nitrogenase
from load import load_nitrogenase_seq
nitrogenase = load_nitrogenase_seq()

sys.setrecursionlimit(20000)



if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # from load import load_seq
    # dna = "ATGCGAATGTAGCATCAAA"
    # dna = load_seq("./data/X73525.fa") #From earlier code.




    i = 0

    #for a in metagenome:    #a is each tuple that is (label, DNA) in metagenome
    #    dna = a[1]
    #    holder_dna = []
    #    snippet = find_all_ORFs_both_strands(dna)
    #    for item in snippet:
    #        #print item
    #        if len(item) > .8*len(nitrogenase):
    #            holder_dna.append(item)
    #    print str(len(holder_dna)) + " number of matches"
    #    for item in holder_dna:
    #        print str(len(item)) + " item length", str(len(nitrogenase)) + " nitrogenase length"
    #        print levenshtein(item,nitrogenase) + " distance"

    holder_dna = []
    for a in metagenome[1:5]:
        dna = a[1]
        snippet = find_all_ORFs_both_strands(dna)
        for item in snippet:
            if len(item[0]) > .8*len(nitrogenase):
                holder_dna.append(item)


    data_output = []

    #print str(len(holder_dna)) + " number of matches"
    print 'length of holder_dna', len(holder_dna)
    lengths = [len(item[0]) for item in holder_dna]
    longest_idx = lengths.index(max(lengths))
    start = time.time()
    dist = levenshtein(holder_dna[longest_idx][0], nitrogenase)
    print "time to calculate distance for longest", time.time() - start
    for item in holder_dna:
        #print str(len(item)) + " item length", str(len(nitrogenase)) + " nitrogenase length"
        #print str(levenshtein(item,nitrogenase)) + " distance"
        #print str(abs(len(item)-levenshtein(item,nitrogenase))/len(item)) + '%'
        #print item[0]
        # print nitrogenase
        levenshtein_val = levenshtein(item[0], nitrogenase)

        percent_match = abs(float(len(item[0]))-float(levenshtein_val))/float(len(item[0])) * 100
        start = item[1]
        end = item[2]
        rev_flag = item[3]
        #data_output.append(  [len(item[0]), len(nitrogenase), levenshtein_val, percent_match, start, end, rev_flag ]) #,loc_in_item_start, loc_in_item_end
        items_data_dict = { }
        items_data_dict['length_item'] = len(item[0])
        items_data_dict['length_nitrogenase'] = len(nitrogenase)
        items_data_dict["levenshtein_dist"] = levenshtein_val
        items_data_dict["percent_match"] = percent_match
        items_data_dict["start"] = start
        items_data_dict["end"] = end
        items_data_dict["rev_flag"]= rev_flag
        #print items_data_dict
        data_output.append(items_data_dict)
    #print data_output


    #     # snippet = longest_ORF(dna)
    #     # print len(snippet)

    #     i += 1

    #     if nitrogenase in snippet:
    #         print 'True',   i #dna
    #     else:
    #         print 'False'

    # snippet = gene_finder(metagenome[10][1])
    # if nitrogenase in snippet:
    #     print i #dna
    # else:

    #     print 'False'


    # i = 0
    # snippet = gene_finder(metagenome)
    # for c in snippet:
    #     print c #no stop codon
    # print nitrogenase
    # if nitrogenase in snippet:
    #     print 'True', i #dna
    # else:
    #     i += 1
    #     print 'False'

    save_file = open('genes_found.pickle', 'w')
    pickle.dump(data_output, save_file)
    save_file.close()



