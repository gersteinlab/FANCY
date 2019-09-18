#!/usr/bin/python
import sys
import os
import warnings
import math
import string
import sys
import numpy as np

f1=open(sys.argv[1], 'r')

ss=[]
n=0
ind=[]

for i in range(0,int(sys.argv[2])):
	ss.append(0)
for line in f1:
	t=line.split('\t')
	k=t[2].split('\n')[0]
#	print(k)
	n=n+1
	ss[int(t[1])]=(float(k))

f1.close()

import scipy as sp 
from scipy import stats
from scipy.stats import kurtosis
from scipy.stats import skew


print np.var(ss), skew(ss), kurtosis(ss)
