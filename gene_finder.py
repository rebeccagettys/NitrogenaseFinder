# -*- coding: utf-8 -*-
"""
Last updated: April 11, 2016
Find Nitrogenase
@author: Erica Lee, Rebecca Gettys, Liv Kelley
"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful

#Importing the metagenome

from load import load_metagenome
metagenome = load_metagenome()
# metagenome = 'ATGGGAAAACTCCGGCAGATCGCTTTCTACGGCAAGGGCGGGATCGGCAAGTCGACGACCTCGCAGAACACCCTCGCGGCACTGGTCGAGATGGGTCAGAAGATCCTCATCGTCGGCTGCGATCCCAAGGCCGACTCGACCCGCCTGATCCTGAACACCAAGCTGCAGGACACCGTGCTTCACCTCGCCGCCGAAGCGGGCTCCGTCGAGGATCTCGAACTCGAGGATGTGGTCAAGATCGGCTACAAGGGCATCAAATGCACCGAAGCCGGCGGGCCGGAGCCGGGCGTGGGCTGCGCGGGCCGCGGCGTCATCACCGCCATCAACTTCCTGGAAGAGAACGGCGCCTATGACGACGTCGACTACGTCTCCTACGACGTGCTGGGCGACGTGGTCTGCGGCGGCTTCGCCATGCCGATCCGCGAGAACAAGGCGCAGGAAATCTACATCGTCATGTCGGGCGAGATGATGGCGCTCTATGCGGCCAACAACATCGCCAAGGGCATCCTGAAATACGCGAACTCGGGCGGCGTGCGCCTCGGCGGCCTGATCTGCAACGAGCGCAAGACCGACCGCGAGCTGGAACTGGCCGAGGCCCTCGCCGCGCGTCTGGGCTGCAAGATGATCCACTTCGTTCCGCGCGACAATATCGTGCAGCACGCCGAGCTCCGCCGCGAGACGGTCATCCAGTATGCGCCCGAGAGCAAGCAGGCGCAGGAATATCGCGAACTGGCCCGCAAGATCCACGAGAACTCGGGCAAGGGCGTGATCCCGACCCCGATCACCATGGAAGAGCTGGAAGAGATGCTGATGGATTTCGGCATCATGCAGTCCGAGGAAGACCGGCTCGCCGCCATCGCCGCCGCCGAGGCCTGA'



#Loading the nitrogenase

from load import load_seq
from load import load_nitrogenase_seq
nitrogenase = load_nitrogenase_seq()


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

    dnalist = list(dna) #dna in correct order
    # dnalist.reverse() #dna in complement order now
    # finallist = list() #create a totally empty list
    #for item in dnalist:
     #   item = get_complement(item)

    finallist = [get_complement(element) for element in dnalist]
    finalstring = ''.join(finallist)

    # for element in dnalist: #taking reversed element list, getting complement, putting it in final list
    #     element = get_complement(element) #now we have the complement
    #     finallist.append(element) #stick that one on the end
    #     finalstring = ''.join(finallist) #smoosh the list into a string
    return finalstring
 #FIXME: too slow a method nom nom memory

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
    #FIXED: this may not function correctly if there are multiple stop codons! all better



def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start
        codon and returns the sequence up to but not including the
        first in frame stop codon.  If there is no in frame stop codon,
        returns the whole string.
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGATGA'
    >>> rest_of_ORF("ATGAGTAGATAGTAG")
    'ATGAGTAGATGA'
    >>> rest_of_ORF("TGA")
    'TGA'
    >>> rest_of_ORF("AAAAA")
    'AAAAA'
    """

    stoplocation = find_stop(dna) #get where to stop
    if stoplocation > 0 or stoplocation == 0: #if it's a reasonable place to stop
        output_sequence = dna[:stoplocation+3] #slice the dna appropriately
        return output_sequence #and spit that out
    elif stoplocation <0: #otherwise just don't change the DNA and output it as is
        return dna


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
    # PYTHON COUNTS FROM ZERO



    for i in range(len(dna)):
        codon = dna[i:i+3] #get a codon
        if codon == 'ATG' and i%3 == 0: #make sure it's a start codon and it's lined up correctly
            return i #tell us the location

        #else:
        #   continue
    return -1 #for logic

    # when we get here, THERE ARE NO START CODONS SO WE ERROR

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
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("CCCATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("CCAATTA")
    []
    """
    # have to start from previous stop location
    startlocation =find_start(dna)
    dnalist = [] # blank list

    while  startlocation >= 0: # we want to stop after we get to the end
        orfout = rest_of_ORF(dna[startlocation:]) #get the rest of the orf
        dna = dna[startlocation + len(orfout):] #slice the orf off the dna
        dnalist.append(orfout) #add the orf to the list of orfs
        startlocation =find_start(dna) #get a new start location
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
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    >>> find_all_ORFs("")
    []
    """

    ORFs = []
    ORFs.extend((find_all_ORFs_oneframe(dna[0:])))
    ORFs.extend((find_all_ORFs_oneframe(dna[1:])))
    ORFs.extend((find_all_ORFs_oneframe(dna[2:])))



    return ORFs


    # dnalist1= find_all_ORFs_oneframe(dna) # use the default reading frame, find orfs
    # dnalist2 =find_all_ORFs_oneframe(dna[1:]) #shift by one, find orfs
    # dnalist3 = find_all_ORFs_oneframe(dna[2:]) #using C so that it can't add a start codon, just shifting it by two now, find ords
    # finaldnalist = []
    # finaldnalist.extend(dnalist1)
    # finaldnalist.extend(dnalist2) #and just make a big list
    # finaldnalist.extend(dnalist3)
    # return finaldnalist

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    >>> find_all_ORFs_both_strands("ATGCGAATG")
    ['ATGCGAATG']
    """
    regularorfs= find_all_ORFs(dna) # get all orfs on the regular strand
    revdna=get_reverse_complement(dna) # get the reverse complement
    revorfs = find_all_ORFs(revdna) #find the orfs of the reverse complement
    finaldnalist = [] #stick em together on a list!
    finaldnalist.extend(regularorfs)
    finaldnalist.extend(revorfs)
    return finaldnalist



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("AAAAAAAA")
    ''
    """
    lenlist = []
    orflist = find_all_ORFs_both_strands(dna)
    if orflist == []:
        return ''
    for i in orflist:
        lenlist.append(len(i)) #add length of that item in the orf list to the end of the length list
    longestorfloc=lenlist.index(max(lenlist))
    longestorf = orflist[longestorfloc]
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
        # randomdna=shuffle_string(dna)
        longestorf=longest_ORF(randomdna)
        #lengths.append(len(longestorf))
        if len(longestorf)>lengthy:
            lengthy = len(longestorf)
        #else: SO I know this is what it does:
        #    lengthy = lengthy
    #sortedlength = sorted(lengths)
    #finallongest = sortedlength[num_trials-1] #biggest length
    #return finallongest
    return lengthy



# def gene_finder(dna):
#     """ Returns the amino acid sequences that are likely coded by the specified dna

#         dna: a DNA sequence
#         returns: a list of all amino acid sequences coded by the sequence dna.
#     """
#     aminoacids = []
#     threshold = longest_ORF_noncoding (dna,1500)
#     orflist = find_all_ORFs_both_strands(dna)

#     # for i in orflist:
#     #     if len(i) >= threshold: #else ignore that item in the list
#     #         aminoacids.append(coding_strand_to_AA(i)) # get the amino acids for that dna sequence in the list and append that item to the list
#     return orflist


#GOING BEYOND CODE BEGINS HERE





if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # from load import load_seq
    # dna = "ATGCGAATGTAGCATCAAA"
    # dna = load_seq("./data/X73525.fa") #From earlier code.




    i = 0
    print len(metagenome)
    print metagenome[20000]
    # for a in metagenome:    #a is each tuple that is (label, DNA) in metagenome
    #     dna = a[1]
    #     snippet = find_all_ORFs_both_strands(dna)



    #     # snippet = longest_ORF(dna)
    #     # print len(snippet)


    #     #I looked through everything in snippet and there really is no nitrogenase in there.
    #     #But when given nitrogenase, it does return true
    #     #I also ran this last part with Oliver's code and it also all returns false
    #     #However, according to Jean, there should be multiple nitrogenase in here

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


