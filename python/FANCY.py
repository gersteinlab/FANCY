import pandas
import pickle
import numpy as np
import os
import sys
import argparse

def predictSNV(rr, dd, cc, assay, ss, ss2, kk):
    a1=0
    a2=0
    a3=0
    if (assay=='RNA-Seq' or assay=='RNASeq' or assay=='rna-seq' or assay=='rnaseq'):
        a1=0
        a2=0
        a3=1

    if (assay=='ATAC-Seq' or assay=='ATACSeq' or assay=='atac-seq' or assay=='atacseq'):
        a1=0
        a2=1
        a3=0

    if (assay=='CHIP-Seq' or assay=='CHIPSeq' or assay=='chip-seq' or assay=='chipseq'):
        a1=1
        a2=0
        a3=0

    if rr=="FANCY":
        loaded_model=pickle.load(open('FANCY.sav', 'rb'))
    if rr=="FANCY_low":
        loaded_model=pickle.load(open('FANCY_low.sav', 'rb'))

    X=np.array([[float(ss),float(ss2),float(kk),float(dd),int(cc),a1,a2,a3]])
    ym, ys2, fm, fs2, lp = loaded_model.predict(X)
    return(float(ym))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-regressor", "--reg",help="FANCY or FANCY_low for variants less than 1000")
    parser.add_argument("-depth", "--de",help="mean depth")
    parser.add_argument("-cov", "--co",help="coverage")
    parser.add_argument("-assay", "--a",help="assay as a string; options are RNA-Seq, ATAC-Seq and CHIP-Seq")
    parser.add_argument("-std", "--st",help="standard deviatiom")
    parser.add_argument("-skew", "--sk",help="skewness")
    parser.add_argument("-kurt", "--ku", help="kurtosis")
    args=parser.parse_args()

    #make the prediction
    print("\n--it is magic--")
    predicted=predictSNV(args.reg,args.de,args.co,args.a,args.st,args.sk,args.ku)
    rare1=predicted*0.19
    rare2=predicted*0.23
    if predicted<100:
        alert='green'
    if predicted>=100 and predicted<=1000:
        alert='yellow'
    if predicted>1000:
        alert='red'
    
    print("\nPredicted number of leaking variants are ",predicted,"\n")
    print("Between ",int(rare1)," and ",int(rare2)," of them are rare\n")
    print("Risk is ",alert,"\n")



if __name__=="__main__":
    main()
