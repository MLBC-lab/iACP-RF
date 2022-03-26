import warnings
def warn(*arg,**kwargs):pass
warnings.warn= warn

import argparse
import read
import generateFeature
import learning
import numpy as np


def main(args):
    
    X, Y = read.fetchXY(args.fasta, args.label)
    X_ind, Y_ind = read.fetchXY(args.fasta_ind,args.label_ind)
    sequences = X_ind
    print('Datasets fetching done.')
    print('Features extraction begins. Be patient! The machine will take some time.')

    k_mers_train = generateFeature.extract_k_mers(args, X, Y)
    k_mers_ind = generateFeature.extract_k_mers(args, X_ind, Y_ind)

    bpf_train = generateFeature.extractBPF(args, X)
    bpf_ind = generateFeature.extractBPF(args, X_ind)

    label = k_mers_train[:, -1]
    label_ind = k_mers_ind[:, -1]
   
    X = k_mers_train[:, int(args.category1[0]):int(args.category1[1])]
    Y = bpf_train
    Z = k_mers_train[:, int(args.category2[0]):int(args.category2[1])]
    print('Feature extraction Completed.')

    X_ind = k_mers_ind[:, int(args.category1[0]):int(args.category1[1])]
    Y_ind = bpf_ind
    Z_ind = k_mers_ind[:, int(args.category2[0]):int(args.category2[1])]

    Label1 = label
    Label2 = label
    Label3 = label
    
    print('Preparing prediction file...')
    learning.classifiers(X, Y, Z, X_ind, Y_ind, Z_ind, Label1, Label2, Label3, label_ind, sequences, args)

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Feature Geneation Tool from Peptide Sequences')
    
    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt', default='Datasets/Main_TR.fasta')
    p.add_argument('-la', '--label', type=str, help='~/Labels.txt', default='Datasets/labelACP_Main_TR.txt')
    p.add_argument('-fa_i', '--fasta_ind', type=str, help='~/FASTA.txt', default='Datasets/Main_IND.fasta')
    p.add_argument('-la_i', '--label_ind', type=str, help='~/Labels.txt', default='Datasets/labelACP_Main_IND.txt')
    
    p.add_argument('-f1', '--category1', nargs='*', help='#s feature inclusive', default=[0, 8420])
    p.add_argument('-f2', '--category2', nargs='*', help='#s feature inclusive', default=[0, 24420])
    

    args = p.parse_args()

    main(args)