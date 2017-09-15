import matplotlib.pyplot as plt

population_ages = [22, 44, 55, 62, 45, 21, 23, 34, 42, 4, 102, 110, 115, 59, 18, 129, 15, 8, 40, 50, 88]
# ids = [x for x in range(len(population_ages))]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()