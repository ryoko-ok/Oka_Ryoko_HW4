import matplotlib.pyplot as plt

years = [1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
pops1 = [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0]
pops2 = [1,0,0,0,1,0,1,0,0,0,5,1,0,0,0,5]
pops3 = [0,0,0,0,1,0,0,0,0,3,3,5,0,0,0,3]


plt.plot(years, pops1, color='#CD7F32', linewidth=3.0)
plt.plot(years, pops2, color= 'silver', linewidth=3.0)
plt.plot(years, pops3, color='gold', linewidth=3.0)

plt.ylabel("Number of Medals")
plt.xlabel("Olympic Years")
plt.title("Japanese Skiing Olympic Medals (Men)", pad=20)

# show the chart
plt.legend()
plt.show()
