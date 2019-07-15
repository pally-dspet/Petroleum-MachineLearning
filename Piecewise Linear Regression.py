# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:45:08 2019

@author: zulfadhli.zaki
"""

import pandas as pd
from scipy import optimize
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Source Data : C:\GIS\ORDA\OP\Hafiz\Digitization Request 20190618_2\RFT MDT.xlsx

RFT = (r"C:\Users\zulfadhli.zaki\OneDrive - Beicip Technology Solutions Sdn. Bhd\DS\RFT_Fake.xlsx")
df = pd.read_excel(RFT)

df2 = df[["Depth", "Pressure"]][df.WellName == "LEREK-1A"]
x = df2.Depth
y = df2["Pressure"]

#x = x.astype(np.float)
#y = y.astype(np.float)
#
#def piecewise_linear(x, x0, y0, k1, k2):
#    condlist = [x < x0]
#    funclist = [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0]
#    return np.piecewise(x, condlist, funclist)
#
#
##p , e = optimize.curve_fit(piecewise_linear, x, y, p0 = [20, 1000, -5, 130])
#p , e = optimize.curve_fit(piecewise_linear, x, y, bounds = ([0,1100,-np.inf,-np.inf],[35,1600,np.inf,np.inf]))
#
#xd = np.linspace(1, 35, 1000)
#plt.plot(x, y, "o")
#plt.plot(xd, piecewise_linear(xd, *p))
#
#print p


kmeans = KMeans().fit(df2)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(x, y, c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
