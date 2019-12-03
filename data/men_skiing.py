import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = [1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
bronzes = np.array([0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0])
silvers = np.array([1,0,0,0,1,0,1,0,0,0,5,1,0,0,0,5])
golds = np.array([0,0,0,0,1,0,0,0,0,3,3,5,0,0,0,3])
ind = [x for x, _ in enumerate(years)]
 
plt.bar(ind, golds, width=0.6, label='golds', color='gold', bottom=silvers+bronzes)
plt.bar(ind, silvers, width=0.6, label='silvers', color='silver', bottom=bronzes)
plt.bar(ind, bronzes, width=0.6, label='bronzes', color='#CD7F32')
 
plt.xticks(ind, years)
plt.ylabel("Medals")
plt.xlabel("Years")
plt.legend(loc="upper right")
plt.title("Japanese Olympic Medals (Men/Skiing")
plt.show()
 