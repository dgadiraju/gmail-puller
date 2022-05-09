import pymongo


def get_collection(MONGO_HOST):
    client = pymongo.MongoClient(f'mongodb://{MONGO_HOST}:27017')
    db = client.get_database('email_db')
    collection = db.get_collection('emails')
    return collection


def load_db(collection, mail_ids):
    for mail_id in mail_ids:
        collection.insert_one(mail_id)
