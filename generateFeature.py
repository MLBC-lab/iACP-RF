import warnings
def warn(*arg,**kwargs):pass
warnings.warn= warn

import itertools
import numpy as np

elements = 'ACDEFGHIKLMNPQRSTVWY'


def extract_k_mers(args, X, Y):
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

def extractBPF(args, seq_temp):
    seq = seq_temp
    tem_vec =[]
    bpf = []
    seq_len = []
    for seq in seq_temp:
        fea = []
        for i in range(len(seq)):
            seq_len.append(len(seq))
            if seq[i] =='A':
                tem_vec = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='C':
                tem_vec = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='D':
                tem_vec = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='E':
                tem_vec = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='F':
                tem_vec = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='G':
                tem_vec = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='H':
                tem_vec = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='I':
                tem_vec = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='K':
                tem_vec = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='L':
                tem_vec = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='M':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
            elif seq[i]=='N':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
            elif seq[i]=='P':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
            elif seq[i]=='Q':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
            elif seq[i]=='R':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
            elif seq[i]=='S':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
            elif seq[i]=='T':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
            elif seq[i]=='V':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
            elif seq[i]=='W':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
            elif seq[i]=='Y':
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            else:
                tem_vec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            fea.append(np.array(tem_vec))
        
        if len(seq)<50:
            temp_count = len(seq)
            while  temp_count < 50:
                fea.append(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
                temp_count += 1

        bpf.append(np.array(fea).flatten())

    return np.array(bpf)
