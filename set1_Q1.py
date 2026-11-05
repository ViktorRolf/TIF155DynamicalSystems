import matplotlib.pyplot as plt
import numpy as np

def f(x,r=1):
    dxdtau = (1/5) + (7/10)/(1 + np.exp(80*(1-x))) -r*x**4
    return dxdtau

def fp(x,r=1):
    dxdtau = (7/10)/(1 + np.exp(80*(1-x)))*( -80*np.exp(80*(1-x))) - 4*r*x**3
    return dxdtau