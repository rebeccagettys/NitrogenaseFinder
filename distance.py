def fib(iterate):
        #if iterate == 0:
        #    return 0
        #elif iterate ==1:
        #    return 1
        known = {0:0, 1:1} # basecases
        if iterate in known:
            return known[iterate]
        else:
            newfib = fib(iterate -1 ) + fib(iterate-2)
            known[iterate] = newfib
            return newfib
#fib(10) #should be 55
#fib(2) #should be 1

known_memo = {}
def levenshtein (a,b):
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
    return known_memo[(a,b)]







memo = {}
# https://programmingpraxis.com/2014/09/12/levenshtein-distance/
def levenshtein_distance_recursive(a, b):
    if a == b:
        return 0
    if a == "":
        return len(b)
    if b == "":
        return len(a)
    if (a, b) not in memo:
        l1 = levenshtein_distance_recursive(a[1:], b) + 1
        l2 = levenshtein_distance_recursive(a, b[1:]) + 1
        l3 = levenshtein_distance_recursive(a[1:], b[1:]) + (a[0] != b[0])
        memo[(a,b)] = min(l1, l2, l3)
        #print memo
    return memo[(a,b)]
    #print memo[(a,b)]

levenshtein_distance_recursive("alphabet", "alphabetsoup")