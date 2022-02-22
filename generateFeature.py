import warnings
def warn(*arg,**kwargs):pass
warnings.warn= warn

import itertools
import numpy as np

elements = 'ACDEFGHIKLMNPQRSTVWY'


def extract(args, X, Y):
    T = []  # All instance ...

    m3 = list(itertools.product(elements, repeat=3))

    def kmers(seq, k):
        v = []
        for i in range(len(seq) - k + 1):
            v.append(seq[i:i + k])

        return v

    def diMonoKGap(x, g):  # 2___1

        m = m3
        for i in range(1, x + 1, 1):
            V = kmers(g, i + 3)
    
            for gGap in m:
                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                t.append(C)

    def monoDiKGap(x, g):  # 1___2

        m = m3
        for i in range(1, x + 1, 1):
            V = kmers(g, i + 3)

            for gGap in m:
                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-2] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                t.append(C)



    def pseudoKmers(sequence):
        ### k-mer ###
        ### A, AA, AAA
        k = 3
        for i in range(1, k + 1, 1):
            v = list(itertools.product(elements, repeat=i))
            for i in v:
                t.append(sequence.count(''.join(i)) / len(sequence))


    for x, y in zip(X, Y):
        t = []
        pseudoKmers(x)
        diMonoKGap(1, x)
        monoDiKGap(1, x)

        t.append(y)
        t = np.array(t)
        T.append(t)

    return np.array(T)

