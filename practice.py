#myplot.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
x
np.sin(x)
#fig = plt.figure()
plt.plot(x, np.sin(x))
plt.savefig('plot2.png')
plt.savefig('D:/pyworks/plots/plot1.png')
plt.show(); # import when running from script

