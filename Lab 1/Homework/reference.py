import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot
from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db['customers']

refs = ['events', 'wom', 'ads']
count = len([i for i in refs if i == 1])
colors = ["purple", "gold", "green"]
pyplot.pie(count, labels=refs, colors=colors)
pyplot.axis("equal")

pyplot.show()
