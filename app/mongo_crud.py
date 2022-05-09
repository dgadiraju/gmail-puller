import pymongo
import os

MONGO_HOST = os.environ.get('MONGO_HOST')

client = pymongo.MongoClient(f'mongodb://{MONGO_HOST}:27017')
db = client.get_database('email_db')
collection = db.get_collection('emails')
d = {'email_id': 'dummy@email.com'}
collection.insert_one(d)

results = collection.find_one()
print(results)
