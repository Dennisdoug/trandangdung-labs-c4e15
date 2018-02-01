import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

# 1: Prepare data
texts = ["Android", "iOS", "Web"]
values = [30, 25, 45]
colors = ["purple", "gold", "green"]
explode = [0, 0.2, 0]  #Seperate

# 2: Plot
pyplot.pie(values, labels=texts, colors=colors, explode=explode, shadow=True)
pyplot.axis("equal")

# 3: Show
pyplot.show()
