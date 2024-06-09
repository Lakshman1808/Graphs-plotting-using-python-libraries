import matplotlib
import matplotlib.pyplot as plt
from scipy import stats

x=[dataset] #enter your data values
y=[dataset] #enter your data values

slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope*x+intercept

mymodel=list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x,mymodel)

#Include the functionalities of your requirements included in matplotlib library

plt.show()
