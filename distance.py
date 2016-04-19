import doctest
doctest.testmod()

known_memo = {}
def levenshtein (a,b):
    """This function calculates the Levenshtein distance between two iterables
    a: first string
    b: second string
    returns: minimum levenshtein distance between the two strings as an integer
    >>> levenshtein ("alphabet", "alphabetsoup")
    4
    """
    # https://programmingpraxis.com/2014/09/12/levenshtein-distance/
    if a == b:
        return 0
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a) # so far, list compatible
    #known_memo = {a,b:0, b,a:0, a:b, b:a} # do I need b:a
    if (a,b) in known_memo:
        return known_memo[(a,b)]
    else:
        length1 = levenshtein(a[1:],b) + 1 #so it's 1 different in a, move on
        length2 = levenshtein(a, b[1:]) +1 #so it's 1 different in b, move on, add 1
        length3 = levenshtein(a[1:], b[1:]) + (a[0] != b[0])  #if a 0 and b 0 are not equal, that is = 1, otherwise 0 if false
        known_memo [(a,b)] = min (length1, length2, length3)
    #print known_memo
    return known_memo[(a,b)]


#val = levenshtein(a,b)
#print val

levenshtein ("alphabet", "alphabetsoup")
