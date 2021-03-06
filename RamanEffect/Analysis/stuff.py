import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt

def hallEffectOpenTxtWithData(folder, taskName, startLine=4, xColumn=1, yColumn=2):
    text_file = open(folder + taskName, "r")
    lines = text_file.readlines()
    typeData = lines[startLine]
    data = lines[startLine:]
    data = [i.split("\t") for i in data]
    dat = pd.DataFrame(data)
    x = dat[dat.columns[xColumn]]
    y = dat[dat.columns[yColumn]]
    y = list(y.values)
    y = [float(i.replace(",", ".").replace("\n", "")) for i in y[1:] if i != '']
    x = list(x.values)
    x = [float(i.replace(",", ".").replace("\n", "")) for i in x[1:] if i != '']
    return x, y


class Fitting:
	def __init__(self, type):
		self.type=type
	def __repr__(self):
		return 'Fitting class'
fit1=Fitting("exponent")

print(fit1)
