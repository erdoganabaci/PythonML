#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 04:18:20 2018

@author: erdogan
"""

#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. Veri Onisleme

#2.1. Veri Yukleme
veriler = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")


#veri on isleme
aylar = veriler[['Aylar']]
#test
print(aylar)

satislar = veriler[['Satislar']]
print(satislar)


#verilerin egitim ve test icin bolunmesi
from sklearn.cross_validation import train_test_split
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#model inşası büyük harfli olanlar modeli anlamlı hale normalizasyon yapıyoruz.
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
#lr.fit(X_train,Y_train)
#tahmin = lr.predict(X_test) x modelini veriyoz y modelini tahmin ediyor.
lr.fit(x_train,y_train)    
tahmin = lr.predict(x_test)   
#tahmin ettiklerimiz random olarak aldığımız için değerler kötü geliyor çizdirdiğimizde ondan sort edip sıralı alıcaz değerleri.
x_train=x_train.sort_index()
y_train=y_train.sort_index()

plt.plot(x_train,y_train) #belli değerleri aldı çünkü split ederken 0.33 lük kısmı al dedik.
plt.plot(x_test,tahmin)

plt.title("Aylara göre Satış Grafiği")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
