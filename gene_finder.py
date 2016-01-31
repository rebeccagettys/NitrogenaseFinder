# -*- coding: utf-8 -*-
"""
YOUR HEADER COMMENT HERE

@author: YOUR NAME HERE

"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful
from load import load_seq


def shuffle_string(s):
    """Shuffles the characters in the input string
        NOTE: this is a helper function, you do not
        have to modify this in any way """
    return ''.join(random.sample(s, len(s)))

# YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


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
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'



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

    dnalist = list (dna) #dna in correct order
    dnalist.reverse() #dna in complement order now
    finallist = list () #create a totally empty list
    #for item in dnalist:
     #   item = get_complement(item)
    for element in dnalist: #taking reversed element list, getting complement, putting it in final list
        element = get_complement(element)
        #print element
        finallist.append(element)
        finalstring = ''.join(finallist)
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
    """
    for i in range(len(dna)):
        codon = dna[i:i+3]
        if codon == 'TAG' and i%3 == 0:
            return i
        elif codon == 'TAA' and i%3 == 0:
            return i
        elif codon == 'TGA' and i%3 == 0:
            return i
    return -1
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
    'ATGAGA'
    >>> rest_of_ORF("ATGAGTAGATAGTAG")
    'ATGAGTAGA'
    >>> rest_of_ORF("TGA")
    ''
    >>> rest_of_ORF("AAAAA")
    'AAAAA'
    """



    stoplocation = find_stop(dna)
    if stoplocation > 0 or stoplocation == 0:
        output_sequence = dna[:stoplocation]
        return output_sequence
    elif stoplocation <0:
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
    startcodon = 'ATG'
    # startloc = dna.find(startcodon)
    # if startloc != -1 and i%3 == 0:
    #location of the first phrase of the stop codon
    #   return startloc
    # elif startloc != -1 and i%3 != 0:
    #    dna.find(startcodon+3:end)
    #else:
    #   return -1

    for i in range(len(dna)):
        codon = dna[i:i+3]
        if codon == 'ATG' and i%3 == 0:
            return i

        #else:
        #   continue
    return -1

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
    """



    # have to start from previous stop location
    startlocation =find_start(dna)
    dnalist = []

    while  startlocation >= 0:
        orfout = rest_of_ORF(dna[startlocation:])
        dna = dna[startlocation + len(orfout):]
        dnalist.append(orfout)
        startlocation =find_start(dna)
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
    """
    dnalist1= find_all_ORFs_oneframe(dna)
    dnalist2 =find_all_ORFs_oneframe('C' + dna)
    dnalist3 = find_all_ORFs_oneframe('CC' + dna)
    finaldnalist = []
    finaldnalist.extend(dnalist1)
    finaldnalist.extend(dnalist3)
    finaldnalist.extend(dnalist2)
    return finaldnalist

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    regularorfs= find_all_ORFs(dna)
    revdna=get_reverse_complement(dna)
    revorfs = find_all_ORFs(revdna)
    finaldnalist = []
    finaldnalist.extend(regularorfs)
    finaldnalist.extend(revorfs)
    return finaldnalist

# stop here for week1

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
