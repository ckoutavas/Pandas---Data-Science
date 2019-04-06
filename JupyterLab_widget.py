# create interactive Radio Buttons in jupyter using ipywidgets

from ipywidgets import interact
import ipywidgets as widgets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import scipy as sci

# create two datasets
x = np.linspace(0, 2*np.pi, 2000)
y1=np.sin(2*x)
y2=np.sin(4*x)
y3=np.sin(8*x)

f1=np.exp(-x**2)
f2=np.exp(-2*x**2)
f3=np.exp(-3*x**2)

ms=[y1,y2,y3]
mt=[f1,f2,f3]
ms=np.transpose(ms)
mt=np.transpose(mt)
dataset_1=pd.DataFrame(ms)
dataset_2=pd.DataFrame(mt)

# Selection parameter used in the if condition

def f(Dataset):
    control = Dataset
    if control == 'dataset 1': 
        data=dataset_1
        data.plot()
        plt.show()
    
    elif control== 'dataset 2':
        data=dataset_2
        data.plot()
        plt.show() 
    return Dataset


interact(f, Dataset = widgets.RadioButtons(
options=['dataset 1', 'dataset 2'],
description='Switching:',
disabled=False))


