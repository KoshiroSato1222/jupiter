import pandas
import matplotlib.pyplot as plt

population = pandas.read_csv("population_csv.csv", index_col=2)
plot = population[population["Country Code"] == "WLD"].plot(
    title="World population", linewidth=2, marker=".", markersize=10)
plot.set_xlabel("Year")
plot.set_ylabel("Population")
plt.show()