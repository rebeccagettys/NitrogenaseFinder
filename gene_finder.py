# -*- coding: utf-8 -*-
"""
Last updated: April 15, 2016
Find Nitrogenase
@author: Erica Lee, Rebecca Gettys, Liv Kelley
"""



### FROM HERE DOWN IS CODE THAT IS COMMENTED OUT AND MOVING TO NITROGENASE FINDER
#import random
#from distance import levenshtein
#from amino_acids import aa, codons, aa_table   # you may find these useful
#import sys
#import pickle
##from os import path




#sys.setrecursionlimit(3000)


#Importing the metagenome

#from load import load_metagenome
#metagenome = load_metagenome()
# metagenome = 'ATGGGAAAACTCCGGCAGATCGCTTTCTACGGCAAGGGCGGGATCGGCAAGTCGACGACCTCGCAGAACACCCTCGCGGCACTGGTCGAGATGGGTCAGAAGATCCTCATCGTCGGCTGCGATCCCAAGGCCGACTCGACCCGCCTGATCCTGAACACCAAGCTGCAGGACACCGTGCTTCACCTCGCCGCCGAAGCGGGCTCCGTCGAGGATCTCGAACTCGAGGATGTGGTCAAGATCGGCTACAAGGGCATCAAATGCACCGAAGCCGGCGGGCCGGAGCCGGGCGTGGGCTGCGCGGGCCGCGGCGTCATCACCGCCATCAACTTCCTGGAAGAGAACGGCGCCTATGACGACGTCGACTACGTCTCCTACGACGTGCTGGGCGACGTGGTCTGCGGCGGCTTCGCCATGCCGATCCGCGAGAACAAGGCGCAGGAAATCTACATCGTCATGTCGGGCGAGATGATGGCGCTCTATGCGGCCAACAACATCGCCAAGGGCATCCTGAAATACGCGAACTCGGGCGGCGTGCGCCTCGGCGGCCTGATCTGCAACGAGCGCAAGACCGACCGCGAGCTGGAACTGGCCGAGGCCCTCGCCGCGCGTCTGGGCTGCAAGATGATCCACTTCGTTCCGCGCGACAATATCGTGCAGCACGCCGAGCTCCGCCGCGAGACGGTCATCCAGTATGCGCCCGAGAGCAAGCAGGCGCAGGAATATCGCGAACTGGCCCGCAAGATCCACGAGAACTCGGGCAAGGGCGTGATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGATGGATTTCGGCATCATGCAGTCCGAGGAAGACCGGCTCGCCGCCATCGCCGCCGCCGAGGCCTGA'


#from load import load_seq_paul

#pauls_seq = load_seq_paul()
#pauls_seq = 'GCCCGGACATTCTACATCTCCGCGAAAACACACACTTTTTCGTCTCCGGCGAAGCTTGGCACGCTCGTTGCAAAACAGGGATCAGCAAGGCGAGGGATGGTTGGCCGAGCAGTTACTGCAAAGGGCAACGTCCGCATCTGAGCCGTGCGACGGTTTTGAACGGAAGAAGGCTGCGCCTCGGCGCAAATCGATCAAGCGGCATTAGGTCAACGGAGAGAAAACATGGCACTTCGGCAAATCGCATTCTACGGCAAGGGCGGCATCGGCAAGTCGACCACCTCGCAGAACACCCTCGCGGCGCTGGTTGAGATGGGTCAGAAGATCCTGATCGTCGGCTGCGACCCCAAGGCGGACTCCACCCGTCTGATCCTCAACACCAAGATGCAGGACACGGTGCTGAGCCTCGCCGCGGAAGCGGGTTCGGTGGAAGACCTCGAACTCGAAGACGTGATGAAGATCGGCTACAAGGGCATCAAGTGCACCGAAGCCGGTGGCCCGGAGCCGGGCGTCGGCTGCGCCGGCCGCGGCGTTATCACCGCGATCAACTTCCTCGAAGAAAACGGCGCCTATGAAGACGTCGACTACGTCTCCTACGACGTGCTCGGCGACGTGGTGTGCGGCGGCTTCGCGATGCCGATCCGTGAAAACAAGGCGCAGGAAATCTACATCGTCATGTCCGGCGAGATGATGGCGCTGTATGCCGCCAACAACATCTCCAAGGGCATTCTGAAGTACGCTTCGTCGGGCGGCGTCCGTCTCGGCGGCCTGATCTGCAACGAGCGCCAGACCGACCGCGAGCTCGACCTCGCCGAAGCGCTGGCCAAGAAGCTGAACTCGAAGCTGATCCACTTCGTGCCGCGCGACAATATCGTGCAGCACGCCGAGCTGCGCCGCCAGACCGTGATCCAGTACGCGCCCGACAGCCAGCAGGCTAAGGAATATCGCGCCCTGGCCAACAAGGTCCATGCCAACTGCGGCAACGGCACCATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGCTCGACTTCGGCATCATGAAGACCGAGGAGCAGCAGCTCGCCGAGCTCGCCGCCAAGGAAGCCGCCAAGGCGGCCGCGTCCGCCTGATCGCATCAGCCAGGCCGGTCGCCTAGCGCGACCGGCCGCCATCCCGGCGGCCCCAGACACGAGGAACAACGATGAGCACCGCAGTCGCAGAATCCCCCGCGGACATCAAGGAACGTAACAAGAAGCTGATCGGCGAAGTCCTGGAGGCCTATCCGGACAAGTCGGCCAAGCGTCGCGCCAAGCATCTCAACACGTACGACGCCGAGAAGGCGGAGTGCTCGGTCAAGTCCAACATCAAGTCGATCCCGGGCGTGATGACGATCCGCGGTTGCGCCTACGCCGGCTCGAAGGGCGTGGTGTGGGGCCCGATCAAGGACATGGTCCACATCAGCCACGGCCCGGTCGGCTGCGGCCAGTATTCGTGGGGTTCGCGCCGCAACTATTACAAGGGAACCACCGGCGTCGACACTTTCGGCACGATGCAGTTCACCTCCGACTTCCAGGAGAAGGACATCGTTTTCGGCGGTGACAAGAAGCTCGGCAAGATCATCGACGAGATCCAGGAGCTGTTCCCGCTCTCCAAGGGCATCTCGGTGCAGTCGGAATGCCCGATCGGTCTGATCGGCGACGACATCGAGGCGGTCTCCAAGGCCAAGTCGAAGCAGTATGACGGCAAGCCGATCATCCCGGTCCGCTGCGAAGGCTTCCGCGGCGTGTCGCAGTCGCTCGGCCACCACATCGCCAACGACGTGATCCGTGACTGGGTGTTCGACAAGGCCGCCGAGAAGAACGCCGGCTTCCAGTCGACCCCCTACGACGTCGCGATCATCGGCGACTACAACATCGGCGGCGATGCCTGGGCCTCGCGCATCCTGCTCGAGGAAATGGGCCTCCGCGTGATCGCGCAGTGGTCCGGCGACGGCACCATCGCGGAGCTGGAGAACACCCCGAAGGCGAAGCTGAACATCCTGCACTGCTACCGCTCGATGAACTACATCACGCGGCACATGGAAGAGAAGTTCGGTATTCCGTGGGTTGAATACAACTTCTTCGGCCCGTCCAAGATCGA'

#Loading the nitrogenase

#from load import load_seq
#from load import load_nitrogenase_seq
#nitrogenase = load_nitrogenase_seq()


def get_complement(nucleotide):
    """ Returns the complementary nucleotide
        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    >>> get_complement('T')
    'A'
    >>> get_complement('L')
    -1
    """
    if nucleotide == 'A': #change A to T
        return 'T'
    elif nucleotide == 'T': # T to A
        return 'A'
    elif nucleotide == 'C': # C to G
        return 'G'
    elif nucleotide == 'G': # G to C
        return 'C'
#should I have a negative one, you didn't feed me a valid dna sequence
    else:
        return -1

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    >>> get_reverse_complement("CATCCCTAAATAACGGCACTC")
    'GAGTGCCGTTATTTAGGGATG'
    """

    #for character in(dna):
     #   print character

    #dnalist = list(dna) #dna in correct order
    #finallist = [get_complement(element) for element in dnalist]
    #finalstring = ''.join(finallist)
    #return finalstring

    dnalist = list (dna) #dna in correct order
    dnalist.reverse() #dna in complement order now
    finallist = list () #create a totally empty list
    #for item in dnalist:
     #   item = get_complement(item)
    for element in dnalist: #taking reversed element list, getting complement, putting it in final list
        element = get_complement(element) #now we have the complement
        finallist.append(element) #stick that one on the end
        finalstring = ''.join(finallist) #smoosh the list into a string
    return finalstring

def find_stop(dna):
    """
    Finds the location of the stop codon.
    dna: a dna sequence
    returns: the location of the first letter of the stop codon
    >>> find_stop("ATGTGAA")
    3
    >>> find_stop("ATGTGAATGA")
    3
    >>> find_stop("ATAAAA")
    -1
    """
    #try/except
    for i in range(len(dna)):
        codon = dna[i:i+3]
        if codon == 'TAG' and i%3 == 0: #if it's in the frame and is a stop codon
            return i # tell us where it is
        elif codon == 'TAA' and i%3 == 0: # same
            return i
        elif codon == 'TGA' and i%3 == 0: #same
            return i

    return -1 # if we get here, it means we didn't find a stop so we want a -1 for logic


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start
        codon and returns the sequence up to but not including the
        first in frame stop codon.  If there is no in frame stop codon,
        returns the whole string.
        dna: a DNA sequence
        returns: the open reading frame represented as a string
>>> rest_of_ORF("ATGTGAA")
['ATG', 3]
    >>> rest_of_ORF("ATGAGATAGG")
    ['ATGAGA', 6]
    >>> rest_of_ORF("ATGAGTAGATAGTAG")
    ['ATGAGTAGA', 9]
    >>> rest_of_ORF("ACCTGA")
    ['ACC', 3]
    >>> rest_of_ORF("AAAAA")
    ['AAAAA', -1]
    """

    stoplocation = find_stop(dna) #get where to stop
    if stoplocation > 0 or stoplocation == 0: #if it's a reasonable place to stop
        output_sequence = dna[:stoplocation] #slice the dna appropriately +3
        return [output_sequence, stoplocation] #and spit that out
    elif stoplocation <0: #otherwise just don't change the DNA and output it as is
        return [dna, stoplocation]


def find_start(dna):
    """
    Finds the location of the start codon.
    dna: a dna sequence
    returns: the location of the first letter of the start codon
    >>> find_start("AAGATGA")
    3
    >>> find_start("AAGATGGATG")
    3
    >>> find_start("ATG")
    0
    """

    for i in range(len(dna)):
        codon = dna[i:i+3] #get a codon
        if codon == 'ATG' and i%3 == 0: #make sure it's a start codon and it's lined up correctly
            return i #tell us the location

        #else:
        #   continue
    return -1 #for logic


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA
        sequence and returns them as a list.  This function should
        only find ORFs that are in the default frame of the sequence
        (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    [['ATGCATGAATGTAGA', 0, 15], ['ATGTGCCC', 3, -1]]
    >>> find_all_ORFs_oneframe("CCCATGCATGAATGTAGATAGATGTGCCC")
    [['ATGCATGAATGTAGA', 3, 15], ['ATGTGCCC', 3, -1]]
    >>> find_all_ORFs_oneframe("CCAATTA")
    []
    """
    # have to start from previous stop location
    startlocation =find_start(dna)
    dnalist = [] # blank list

    while  startlocation >= 0: # we want to stop after we get to the end
        rest_of_ORF_output = rest_of_ORF(dna[startlocation:])
        orfout =  rest_of_ORF_output[0] #get the rest of the orf
        end_of_this_orf = rest_of_ORF_output[1]
        start_of_this_orf = startlocation
        dna = dna[startlocation + len(orfout):] #slice the orf off the dna
        dnalist.append([orfout, start_of_this_orf, end_of_this_orf]) #add the orf and start/stop location to the list of orfs
        startlocation =find_start(dna) #get a new start location
        #print startlocation
    return dnalist



def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in
        all 3 possible frames and returns them as a list.  By non-nested we
        mean that if an ORF occurs entirely within another ORF and they are
        both in the same frame, it should not be included in the returned list
        of ORFs.
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs("ATGCATGAATGTAG")
    [['ATGCATGAATGTAG', 0, -1], ['ATGAATGTAG', 3, -1], ['ATG', 6, 3]]
    >>> find_all_ORFs("")
    []
    """

    ORFs = []
    ORFs.extend((find_all_ORFs_oneframe(dna[0:])))
    ORFs.extend((find_all_ORFs_oneframe(dna[1:])))
    ORFs.extend((find_all_ORFs_oneframe(dna[2:])))




    return ORFs



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    [['ATGCGAATG', 0, 9], ['ATGCTACATTCGCAT', 3, -1]]
    >>> find_all_ORFs_both_strands("ATGCGAATG")
    [['ATGCGAATG', 0, -1]]

    """
    regular_orfs= find_all_ORFs(dna) # get all orfs on the regular strand
    for item in regular_orfs:
        item.append(0) #0 for regular strand
    #print regularorfs

    rev_dna=get_reverse_complement(dna) # get the reverse complement
    rev_orfs = find_all_ORFs(rev_dna) #find the orfs of the reverse complement
    for item in rev_orfs:
        item.append(1) #1 for reverse strand

    finaldnalist = [] #stick em together on a list!
    finaldnalist.extend(regular_orfs)
    finaldnalist.extend(rev_orfs)
    #print finaldnalist
    return finaldnalist



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string #TAA TGA TAG
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    ['ATGCTACATTCGCAT', 3, -1]
    >>> longest_ORF("AAAAAAAA")
    ['']
    """
    # TAA TGA TAG
    lenlist = []
    orflist = find_all_ORFs_both_strands(dna)
    if orflist == []:
        return ['']
    for item in orflist:
        lenlist.append(len(item[0])) #add length of that item in the orf list to the end of the length list
        #print lenlist
    longestorfloc=lenlist.index(max(lenlist))
    longestorf = orflist[longestorfloc]
    #print orflist
    return longestorf


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    lengthy = 0
    i = 0

    while i < num_trials:
        i = i +1
        randomdna = dna
        longestorf=longest_ORF(randomdna)
        if len(longestorf)>lengthy:
            lengthy = len(longestorf)
    return lengthy





#GOING BEYOND CODE BEGINS HERE THIS IS ALL MOVING TO NITROGENASE





#if __name__ == "__main__":



    #i = 0

    ##for a in metagenome:    #a is each tuple that is (label, DNA) in metagenome
    ##    dna = a[1]
    # #   holder_dna = []
    # #   snippet = find_all_ORFs_both_strands(dna)
    # #   for item in snippet:
    # #       #print item
    # #       if len(item) > .8*len(nitrogenase):
    # #           holder_dna.append(item)
    # #   print str(len(holder_dna)) + " number of matches"
    # #   for item in holder_dna:
    # #       print str(len(item)) + " item length", str(len(nitrogenase)) + " nitrogenase length"
    # #       print levenshtein(item,nitrogenase) + " distance"

    #dna = pauls_seq
    ##print len(dna)
    #holder_dna = []
    #snippet = find_all_ORFs_both_strands(dna)
    ##print snippet
    #for item in snippet:
     #   #print item
     #   #for
      #  if len(item[0]) > .8*len(nitrogenase):
      #      holder_dna.append(item)
       # #holder_dna.append(item)


    #data_output_tuple_list = []
    ##print str(len(holder_dna)) + " number of matches"
    #for item in holder_dna:
     #   #print str(len(item)) + " item length", str(len(nitrogenase)) + " nitrogenase length"
     #   #print str(levenshtein(item,nitrogenase)) + " distance"
      #  #print str(abs(len(item)-levenshtein(item,nitrogenase))/len(item)) + '%'
      #  levenshtein_val = levenshtein(item[0], nitrogenase)
      #  percent_match = abs(float(len(item[0]))-float(levenshtein_val))/float(len(item[0])) * 100
      #  data_output_tuple_list.append( ( len(item), len(nitrogenase), levenshtein_val, percent_match )) #,loc_in_item_start, loc_in_item_end
    #print data_output_tuple_list

