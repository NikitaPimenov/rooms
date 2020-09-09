from collections import defaultdict
def checkhash(seq, f, mod):
    a = defaultdict(int)
    for i in seq:
        a[f(i) % mod] += 1
    return max(a.values()), min(a.values())