from pymongo import MongoClient

mongo_uri = "mongodb://Dennis1328:Gagaga1995@ds119268.mlab.com:19268/dangerous_stuffs"

# 1: Open a connection to mlab
client = MongoClient(mongo_uri)

# 2: Get database
db = client.get_default_database()

# 3: Get collection
games = db['blogs'] #Retrieve collection

# 4: Create a new document
new_blog = {
    'title': 'Killing freely? No problem',
    'description': 'How to kill someone without being spotted'
}

# 5: Put the created document into collection
games.insert_one(new_blog)
