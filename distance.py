import doctest
doctest.testmod()

def levenshtein (a_full,b_full, a_start=0, b_start= 0, known_memo=None):
    """This function calculates the Levenshtein distance between two iterables
    a: first string
    b: second string
    a_start: the index in a to start from
    b_start: the index in b to start from
    returns: minimum levenshtein distance between the two strings starting from
             the specified positions a_start and b_start as an integer
    Credit for understanding/example code:  https://programmingpraxis.com/2014/09/12/levenshtein-distance/
    >>> levenshtein ("alphabet", "alphabetsoup")
    4
    """
    if known_memo == None:
        known_memo = {}

    if a_start >= len(a_full):
        return len(b_full)-b_start+1
    if b_start >= len(b_full):
        return len(a_full)- a_start+1 # so far, list compatible
    if (a_start,b_start) in known_memo:
        return known_memo[(a_start,b_start)]
    else:
        length1 = levenshtein(a_full,b_full, a_start, b_start+1, known_memo) + 1 #so it's 1 different in a, move on
        length2 = levenshtein(a_full, b_full, a_start+1, b_start, known_memo) +1 #so it's 1 different in b, move on, add 1
        length3 = levenshtein(a_full, b_full, a_start+1, b_start+1, known_memo) + (a_full[a_start] != b_full[b_start])  #if a 0 and b 0 are not equal, that is = 1, otherwise 0 if false

        known_memo [(a_start,b_start)] = min (length1, length2, length3)
    return known_memo[(a_start,b_start)]