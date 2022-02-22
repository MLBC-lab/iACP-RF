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
    print('\nDatasets fetching done.')

    ############################################################################
    print('Features extraction begins. Be patient! The machine will take some time.')

    T = generateFeature.extract(args, X, Y)
    T_ind = generateFeature.extract(args, X_ind, Y_ind)

    feature = T[:, :-1]
    label = T[:, -1]

    feature_ind = T_ind[:, :-1]
    label_ind = T_ind[:, -1]


    X = feature[:, int(args.category1[0]):int(args.category1[1])]  
    Y = feature[:, int(args.category2[0]):int(args.category2[1])] 
    Z = feature[:, int(args.category3[0]):int(args.category3[1])] 

    X_ind = feature_ind[:, int(args.category1[0]):int(args.category1[1])]  
    Y_ind = feature_ind[:, int(args.category2[0]):int(args.category2[1])]  
    Z_ind = feature_ind[:, int(args.category3[0]):int(args.category3[1])]  

    Label1 = label
    Label2 = label
    Label3 = label
    
    learning.classifiers(X, Y, Z, X_ind, Y_ind, Z_ind, Label1, Label2, Label3, label_ind, sequences, args)

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Feature Geneation Tool from Protein Sequences')
    
    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt', default='Datasets/Main_TR.fasta')
    p.add_argument('-la', '--label', type=str, help='~/Labels.txt', default='Datasets/labelACP_Main_TR.txt')
    p.add_argument('-fa_i', '--fasta_ind', type=str, help='~/FASTA.txt', default='Datasets/Main_IND.fasta')
    p.add_argument('-la_i', '--label_ind', type=str, help='~/Labels.txt', default='Datasets/labelACP_Main_IND.txt')
    
    p.add_argument('-f1', '--category1', nargs='*', help='#s feature inclusive', default=[0, 24420])
    p.add_argument('-f2', '--category2', nargs='*', help='#s feature inclusive', default=[0, 24420])
    p.add_argument('-f3', '--category3', nargs='*', help='#s feature inclusive', default=[0, 24420])
    

    args = p.parse_args()

    main(args)