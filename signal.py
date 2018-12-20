# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 21:01:01 2018

@author: Walid Ghanem
@ FAU university, walid.ghanem@fau.de
"""
import pylab as plp
import numpy as np
x=numpy.linspace(-1,1,100)
signal=2+x+2*x*x*x;
noise=np.random.normal(0,0.1,100)
y=signal+noise;
plp.plot(signal,'b')
plp.plot(y,'g')
plp.plot(noise,'r')
plp.xlabel("x")
plp.ylabel("y")
pylab.legend(["Without Noise", "With Noise", "Noise"], loc = 2)