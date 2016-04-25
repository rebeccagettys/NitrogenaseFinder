import pickle
import sys
from distance import levenshtein
from gene_finder import *


from load import load_metagenome
metagenome = load_metagenome()

# pauls_seq = 'GCCCGGACATTCTACATCTCCGCGAAAACACACACTTTTTCGTCTCCGGCGAAGCTTGGCACGCTCGTTGCAAAACAGGGATCAGCAAGGCGAGGGATGGTTGGCCGAGCAGTTACTGCAAAGGGCAACGTCCGCATCTGAGCCGTGCGACGGTTTTGAACGGAAGAAGGCTGCGCCTCGGCGCAAATCGATCAAGCGGCATTAGGTCAACGGAGAGAAAACATGGCACTTCGGCAAATCGCATTCTACGGCAAGGGCGGCATCGGCAAGTCGACCACCTCGCAGAACACCCTCGCGGCGCTGGTTGAGATGGGTCAGAAGATCCTGATCGTCGGCTGCGACCCCAAGGCGGACTCCACCCGTCTGATCCTCAACACCAAGATGCAGGACACGGTGCTGAGCCTCGCCGCGGAAGCGGGTTCGGTGGAAGACCTCGAACTCGAAGACGTGATGAAGATCGGCTACAAGGGCATCAAGTGCACCGAAGCCGGTGGCCCGGAGCCGGGCGTCGGCTGCGCCGGCCGCGGCGTTATCACCGCGATCAACTTCCTCGAAGAAAACGGCGCCTATGAAGACGTCGACTACGTCTCCTACGACGTGCTCGGCGACGTGGTGTGCGGCGGCTTCGCGATGCCGATCCGTGAAAACAAGGCGCAGGAAATCTACATCGTCATGTCCGGCGAGATGATGGCGCTGTATGCCGCCAACAACATCTCCAAGGGCATTCTGAAGTACGCTTCGTCGGGCGGCGTCCGTCTCGGCGGCCTGATCTGCAACGAGCGCCAGACCGACCGCGAGCTCGACCTCGCCGAAGCGCTGGCCAAGAAGCTGAACTCGAAGCTGATCCACTTCGTGCCGCGCGACAATATCGTGCAGCACGCCGAGCTGCGCCGCCAGACCGTGATCCAGTACGCGCCCGACAGCCAGCAGGCTAAGGAATATCGCGCCCTGGCCAACAAGGTCCATGCCAACTGCGGCAACGGCACCATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGCTCGACTTCGGCATCATGAAGACCGAGGAGCAGCAGCTCGCCGAGCTCGCCGCCAAGGAAGCCGCCAAGGCGGCCGCGTCCGCCTGATCGCATCAGCCAGGCCGGTCGCCTAGCGCGACCGGCCGCCATCCCGGCGGCCCCAGACACGAGGAACAACGATGAGCACCGCAGTCGCAGAATCCCCCGCGGACATCAAGGAACGTAACAAGAAGCTGATCGGCGAAGTCCTGGAGGCCTATCCGGACAAGTCGGCCAAGCGTCGCGCCAAGCATCTCAACACGTACGACGCCGAGAAGGCGGAGTGCTCGGTCAAGTCCAACATCAAGTCGATCCCGGGCGTGATGACGATCCGCGGTTGCGCCTACGCCGGCTCGAAGGGCGTGGTGTGGGGCCCGATCAAGGACATGGTCCACATCAGCCACGGCCCGGTCGGCTGCGGCCAGTATTCGTGGGGTTCGCGCCGCAACTATTACAAGGGAACCACCGGCGTCGACACTTTCGGCACGATGCAGTTCACCTCCGACTTCCAGGAGAAGGACATCGTTTTCGGCGGTGACAAGAAGCTCGGCAAGATCATCGACGAGATCCAGGAGCTGTTCCCGCTCTCCAAGGGCATCTCGGTGCAGTCGGAATGCCCGATCGGTCTGATCGGCGACGACATCGAGGCGGTCTCCAAGGCCAAGTCGAAGCAGTATGACGGCAAGCCGATCATCCCGGTCCGCTGCGAAGGCTTCCGCGGCGTGTCGCAGTCGCTCGGCCACCACATCGCCAACGACGTGATCCGTGACTGGGTGTTCGACAAGGCCGCCGAGAAGAACGCCGGCTTCCAGTCGACCCCCTACGACGTCGCGATCATCGGCGACTACAACATCGGCGGCGATGCCTGGGCCTCGCGCATCCTGCTCGAGGAAATGGGCCTCCGCGTGATCGCGCAGTGGTCCGGCGACGGCACCATCGCGGAGCTGGAGAACACCCCGAAGGCGAAGCTGAACATCCTGCACTGCTACCGCTCGATGAACTACATCACGCGGCACATGGAAGAGAAGTTCGGTATTCCGTGGGTTGAATACAACTTCTTCGGCCCGTCCAAGATCGA'

#Loading the nitrogenase
from load import load_nitrogenase_seq
nitrogenase = load_nitrogenase_seq()

sys.setrecursionlimit(3000)



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
    for a in metagenome[9:10]:
        dna = a[1]
        snippet = find_all_ORFs_both_strands(dna)
        for item in snippet:
            if len(item[0]) > .8*len(nitrogenase):
                holder_dna.append(item)


    data_output_tuple_list = []
    #print str(len(holder_dna)) + " number of matches"
    for item in holder_dna:
        #print str(len(item)) + " item length", str(len(nitrogenase)) + " nitrogenase length"
        #print str(levenshtein(item,nitrogenase)) + " distance"
        #print str(abs(len(item)-levenshtein(item,nitrogenase))/len(item)) + '%'
        levenshtein_val = levenshtein(item[0], nitrogenase)
        percent_match = abs(float(len(item[0]))-float(levenshtein_val))/float(len(item[0])) * 100
        start = item[1]
        end = item[2]
        rev_flag = item[3]
        data_output_tuple_list.append(  [len(item[0]), len(nitrogenase), levenshtein_val, percent_match, start, end, rev_flag ]) #,loc_in_item_start, loc_in_item_end
    print data_output_tuple_list


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
    pickle.dump(data_output_tuple_list, save_file)
    save_file.close()



