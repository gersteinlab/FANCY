import numpy as np
import os

#preparing inputs
gue=open('../data/bias_depth_cov_tier_snv.txt','r')
bgvex=open('../data/braingvex.txt','r')
acet=open('../data/acet.txt','r')
atac=open('../data/humanfc.txt','r')

stad=[]
skew=[]
kurt=[]
depth=[]
cova=[]
overlap=[]
type1=[]
type2=[]
type3=[]
snv=[]


for line in gue:
    A=line.split('\t')
    A1=A[0].split(' ')
    A2=A[1].split(' ')
    A3=A2[3].split('\n')
    stad.append(float(A1[0]))
    skew.append(float(A1[1]))
    kurt.append(float(A1[2]))
    depth.append(float(A2[0]))
    cova.append(float(A2[1]))
    overlap.append(int(A3[0]))
    snv.append(int(A3[0]))
    type1.append(0)
    type2.append(0)
    type3.append(1)
    
for line in bgvex:
    A=line.split('\t')
    A1=A[0].split(' ')
    A2=A[1].split(' ')
    A3=A2[3].split('\n')
    stad.append(float(A1[0]))
    skew.append(float(A1[1]))
    kurt.append(float(A1[2]))
    depth.append(float(A2[0]))
    cova.append(float(A2[1]))
    overlap.append(int(A3[0]))
    snv.append(int(A3[0]))
    type1.append(0)
    type2.append(1)
    type3.append(0)    
    
for line in acet:
    A=line.split('\t')
    A1=A[0].split(' ')
    A2=A[1].split(' ')
    A3=A2[3].split('\n')
    stad.append(float(A1[0]))
    skew.append(float(A1[1]))
    kurt.append(float(A1[2]))
    depth.append(float(A2[0]))
    cova.append(float(A2[1]))
    overlap.append(int(A3[0]))
    snv.append(int(A3[0]))
    type1.append(0)
    type2.append(0)
    type3.append(1)
    
for line in atac:
    A=line.split('\t')
    A1=A[0].split(' ')
    A2=A[1].split(' ')
    A3=A2[3].split('\n')
    stad.append(float(A1[0]))
    skew.append(float(A1[1]))
    kurt.append(float(A1[2]))
    depth.append(float(A2[0]))
    cova.append(float(A2[1]))
    overlap.append(int(A3[0]))
    snv.append(int(A3[0]))
    type1.append(0)
    type2.append(1)
    type3.append(0)


#prepare trainign and test dataset
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
df = pd.DataFrame()
df['stad']=stad
df['skew']=skew
df['kurt']=kurt
df['depth']=depth
df['cova']=cova
df['t1']=type1
df['t2']=type2
df['t3']=type3
y = snv # define the target variable (dependent variable) as y
# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.5)
X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

import pyGPs

model = pyGPs.GPR() 
k = pyGPs.Core.cov.Matern(log_ell=[8.53571426347188,7.86273364470724,15.7314831784801,3.34023839973156,19.9733814918404,-1.75129842978112,-2.35921702690416,-1.40045612390735], d=3, log_sigma=12.6732)
model.setPrior(kernel=k)
model.setNoise( log_sigma = 3.61609724518 )
model.getPosterior(X_train, y_train)
ym, ys2, fm, fs2, lp = model.predict(X_test) 
#shape(ym)
# predict test cases
#plt.figure()
#plt.plot(y_test, ym, 'r.', markersize=10, label='Observations')
from sklearn.metrics import r2_score
print("test r-square is ",r2_score(y_test, ym))
import pickle
filename = 'FANCY.sav'
pickle.dump(model, open(filename, 'wb'))
