from itertools import *

def chainslice(begin, end, seq0, *seq1):
    return islice(chain(seq0, *seq1), begin, end)